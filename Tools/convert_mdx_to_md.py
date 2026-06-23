#!/usr/bin/env python3
"""
CraftEngine Wiki MDX → Markdown converter v2

Converts Docusaurus MDX files to clean Markdown, handling:
- Frontmatter → H1 heading
- All JSX components (Tabs, TabItem, Highlight, ColoredLink, Comment,
  PluginFileTree, UrlCard, SkriptCard, DiffViewer, Yellow)
- HTML elements (div, img with require(), p, details/summary)
- Import removal
- Admonition passthrough (:::info etc.)
- Link rewriting (.mdx → .md)
"""

import re
import json
import shutil
from pathlib import Path
from typing import Optional, Tuple

SRC_DIR = Path(__file__).parent / "CraftEngine Wiki" / "current"
DST_DIR = Path(__file__).parent / "CraftEngine Wiki Markdown"


# ═══════════════════════════════════════════════════════════════════════════════
# Core: balanced tag extraction
# ═══════════════════════════════════════════════════════════════════════════════

def extract_tag_content(text: str, start: int, tag_name: str) -> Tuple[Optional[str], int]:
    """
    Extract inner content of a JSX/HTML tag.
    `start` points at the '<' of the opening tag.
    Returns (inner_content, position_after_closing_tag) or (None, -1).
    Handles nested same-name tags; ignores tags inside fenced code blocks.
    """
    # Skip past the opening tag: <TagName ... >
    i = start + len(tag_name) + 1  # skip '<TagName'
    in_string = False
    string_char = None

    while i < len(text):
        ch = text[i]
        if in_string:
            if ch == '\\':
                i += 2
                continue
            if ch == string_char:
                in_string = False
            i += 1
            continue
        if ch in ('"', "'", '`'):
            in_string = True
            string_char = ch
            i += 1
            continue
        if ch == '/' and i + 1 < len(text) and text[i + 1] == '>':
            # Self-closing tag
            return None, i + 2
        if ch == '>':
            tag_open_end = i + 1
            break
        i += 1
    else:
        return None, -1

    # Now find matching closing tag, respecting fenced code blocks
    close_tag = f'</{tag_name}>'
    depth = 1
    j = tag_open_end
    in_fence = False
    fence_char = None

    while j < len(text):
        # Handle fenced code blocks
        if text[j:j + 3] == '```':
            if not in_fence:
                in_fence = True
                fence_char = '`'
                j += 3
                # Find end of this fence line (language specifier)
                while j < len(text) and text[j] != '\n':
                    j += 1
                continue
            else:
                in_fence = False
                fence_char = None
                j += 3
                continue

        if text[j:j + 3] == '~~~':
            if not in_fence:
                in_fence = True
                fence_char = '~'
                j += 3
                while j < len(text) and text[j] != '\n':
                    j += 1
                continue
            else:
                in_fence = False
                fence_char = None
                j += 3
                continue

        if not in_fence:
            # Check for nested opening tag
            if text[j:j + len(tag_name) + 1] == f'<{tag_name}':
                next_ch = text[j + len(tag_name) + 1]
                if next_ch in (' ', '>', '\n', '\t', '\r', '/'):
                    depth += 1
            # Check for closing tag
            if text[j:j + len(close_tag)] == close_tag:
                depth -= 1
                if depth == 0:
                    return text[tag_open_end:j], j + len(close_tag)
        j += 1

    return None, -1


def find_next_tag(text: str, pos: int, tag_names: list) -> Tuple[Optional[str], int, int]:
    """
    Find the next occurrence of any tag in `tag_names`.
    Returns (tag_name, start_pos, end_pos_after_content) or (None, -1, -1).
    """
    best_pos = len(text)
    best_name = None
    for name in tag_names:
        idx = text.find(f'<{name}', pos)
        if idx != -1 and idx < best_pos:
            # Verify it's actually the tag (next char is space, >, /, newline)
            next_idx = idx + len(name) + 1
            if next_idx < len(text) and text[next_idx] in (' ', '>', '\n', '\t', '\r', '/'):
                best_pos = idx
                best_name = name
    if best_name is None:
        return None, -1, -1

    _, end = extract_tag_content(text, best_pos, best_name)
    return best_name, best_pos, end


# ═══════════════════════════════════════════════════════════════════════════════
# Component converters (order-sensitive: multi-line before inline)
# ═══════════════════════════════════════════════════════════════════════════════

def convert_tabs(text: str) -> str:
    """Convert <Tabs><TabItem>...</TabItem></Tabs> to labeled markdown sections."""
    result = []
    i = 0
    while i < len(text):
        # Find <Tabs
        idx = text.find('<Tabs', i)
        if idx == -1:
            result.append(text[i:])
            break

        # Verify it's a tag start
        next_ch_pos = idx + 5
        if next_ch_pos >= len(text) or text[next_ch_pos] not in (' ', '>', '\n', '\t', '\r'):
            result.append(text[i:idx + 5])
            i = idx + 5
            continue

        result.append(text[i:idx])
        content, end = extract_tag_content(text, idx, 'Tabs')
        if content is not None and end != -1:
            result.append(_convert_tab_items(content))
            i = end
        else:
            result.append(text[idx:idx + 5])
            i = idx + 5
    return ''.join(result)


def _convert_tab_items(content: str) -> str:
    """Extract <TabItem> children from <Tabs> content."""
    result = []
    i = 0
    while i < len(content):
        idx = content.find('<TabItem', i)
        if idx == -1:
            result.append(content[i:])
            break
        next_ch = idx + 8
        if next_ch < len(content) and content[next_ch] not in (' ', '>', '\n', '\t', '\r'):
            result.append(content[i:idx + 8])
            i = idx + 8
            continue

        result.append(content[i:idx])
        inner, end = extract_tag_content(content, idx, 'TabItem')
        if inner is not None and end != -1:
            # Extract label from opening tag
            tag_text = content[idx:content.index('>', idx) + 1]
            label_match = re.search(r'label=["\']([^"\']+)["\']', tag_text)
            label = label_match.group(1) if label_match else ''
            if label:
                result.append(f'\n**{label}:**\n')
            result.append(inner.strip())
            result.append('\n')
            i = idx + end
        else:
            result.append(content[i:idx + 8])
            i = idx + 8
    return ''.join(result)


def convert_diff_viewer(text: str) -> str:
    """Convert <DiffViewer>...</DiffViewer> to a note placeholder."""
    result = []
    i = 0
    while i < len(text):
        idx = text.find('<DiffViewer', i)
        if idx == -1:
            result.append(text[i:])
            break
        next_ch = idx + 11
        if next_ch < len(text) and text[next_ch] not in (' ', '>', '\n', '\t', '\r'):
            result.append(text[i:idx + 11])
            i = idx + 11
            continue

        result.append(text[i:idx])
        _, end = extract_tag_content(text, idx, 'DiffViewer')
        if end != -1:
            result.append('\n> ⚠️ *Diff comparison — see original documentation*\n\n')
            i = end
        else:
            result.append(text[i:idx + 11])
            i = idx + 11
    return ''.join(result)


def convert_plugin_file_tree(text: str) -> str:
    """Convert <PluginFileTree ... /> to ASCII file tree."""
    result = []
    i = 0
    while i < len(text):
        idx = text.find('<PluginFileTree', i)
        if idx == -1:
            result.append(text[i:])
            break
        next_ch = idx + 15
        if next_ch < len(text) and text[next_ch] not in (' ', '>', '\n', '\t', '\r'):
            result.append(text[i:idx + 15])
            i = idx + 15
            continue

        result.append(text[i:idx])
        content, end = extract_tag_content(text, idx, 'PluginFileTree')
        end_pos = end if end != -1 else idx + 15

        if content is not None:
            tree_data = _extract_tree_data(content)
        else:
            # Self-closing form — look for initialTreeData in the tag itself
            tag_text = text[idx:text.index('>', idx) + 1] if '>' in text[idx:] else text[idx:]
            tree_data = _extract_tree_data(tag_text)

        if tree_data:
            ascii_tree = _generate_ascii_tree(tree_data)
            result.append(f'\n```\n{ascii_tree}\n```\n')
        else:
            result.append('\n> 📁 *Interactive file tree — see original documentation*\n\n')

        i = end_pos if end != -1 else text.index('>', idx) + 1

    return ''.join(result)


def _extract_tree_data(tag_text: str) -> Optional[list]:
    """Extract tree data JSON from PluginFileTree/initialTreeData."""
    match = re.search(r'initialTreeData=\{(\[.+?\])\}', tag_text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def _generate_ascii_tree(nodes: list, prefix: str = '', is_root: bool = True) -> str:
    """Generate ASCII tree from PluginFileTree data."""
    lines = []
    for idx, node in enumerate(nodes):
        is_last = idx == len(nodes) - 1
        name = node.get('name', '')
        is_leaf = node.get('isLeaf', False)

        if is_root and idx == 0:
            connector = ''
        elif is_last:
            connector = '└── '
        else:
            connector = '├── '

        icon = '📄 ' if is_leaf else '📁 '
        lines.append(f'{prefix}{connector}{icon}{name}')

        children = node.get('children', [])
        if children:
            new_prefix = prefix + ('' if (is_root and idx == 0) else ('    ' if is_last else '│   '))
            lines.append(_generate_ascii_tree(children, new_prefix, False))

    return '\n'.join(lines)


def convert_url_card(text: str) -> str:
    """Convert <UrlCard url="..." title="..." ... /> to markdown link."""
    def repl(m):
        attrs = m.group(1)
        url_match = re.search(r'url=["\']([^"\']+)["\']', attrs)
        title_match = re.search(r'title=["\']([^"\']+)["\']', attrs)
        subtitle_match = re.search(r'subtitle=["\']([^"\']*)["\']', attrs)
        url = url_match.group(1) if url_match else ''
        title = title_match.group(1) if title_match else ''
        subtitle = subtitle_match.group(1) if subtitle_match else ''
        link = f'[{title}]({url})'
        if subtitle and subtitle.strip():
            link += f' — *{subtitle}*'
        return link
    return re.sub(
        r'<UrlCard\b([^>]*?)\s*/?>',
        repl,
        text,
        flags=re.DOTALL
    )


def convert_skript_card(text: str) -> str:
    """Convert <SkriptCard ... /> to a markdown code block with title."""
    def repl(m):
        attrs = m.group(1)
        title_match = re.search(r'title=["\']([^"\']+)["\']', attrs)
        code_match = re.search(r'code=["\']([^"\']*)["\']', attrs)
        title = title_match.group(1) if title_match else ''
        code = code_match.group(1) if code_match else ''
        # Unescape common escapes
        if code:
            code = code.replace('\\n', '\n').replace('\\t', '\t')
        result = ''
        if title:
            result += f'**{title}**\n\n'
        if code:
            result += f'```\n{code}\n```\n'
        return result
    return re.sub(
        r'<SkriptCard\b([^>]*?)\s*/?>',
        repl,
        text,
        flags=re.DOTALL
    )


def convert_highlight(text: str) -> str:
    """
    Convert <Highlight color="...">text</Highlight>.
    Strips tags, keeping inner content. If inner content is already
    bold (**...**), don't double-wrap.
    """
    def repl(m):
        inner = m.group(1)
        return inner
    return re.sub(r'<Highlight[^>]*>(.+?)</Highlight>', repl, text, flags=re.DOTALL)


def convert_colored_link(text: str) -> str:
    """Convert <ColoredLink to="..." color="...">text</ColoredLink> to [text](to)."""
    def repl(m):
        attrs = m.group(1)
        inner = m.group(2)
        href_match = re.search(r'to=["\']([^"\']+)["\']', attrs)
        href = href_match.group(1) if href_match else ''
        return f'[{inner}]({href})'
    return re.sub(r'<ColoredLink\b([^>]*)>(.+?)</ColoredLink>', repl, text, flags=re.DOTALL)


def convert_comment(text: str) -> str:
    """
    Convert <Comment text="...">content</Comment> → content
    and <Comment text="..." /> → text value.
    """
    # Non-self-closing: <Comment text="...">content</Comment>
    def repl_full(m):
        attrs = m.group(1)
        inner = m.group(2)
        return inner
    text = re.sub(
        r'<Comment\b([^>]*)>(.+?)</Comment>',
        repl_full, text, flags=re.DOTALL
    )
    # Self-closing: <Comment text="..." />
    def repl_self(m):
        return m.group(1)
    text = re.sub(
        r'<Comment\s+text=["\']([^"\']+)["\']\s*/>',
        repl_self, text
    )
    return text


def convert_yellow(text: str) -> str:
    """Convert <Yellow>text</Yellow> — just strip the tags."""
    return re.sub(r'</?Yellow>', '', text)


# ═══════════════════════════════════════════════════════════════════════════════
# Image / HTML converters
# ═══════════════════════════════════════════════════════════════════════════════

def convert_images_and_divs(text: str) -> str:
    """
    Convert:
    1. <div style={{textAlign: 'center'}}> with <img> + <p> caption → ![](path) + caption
    2. Standalone <img src={require(...).default} ... /> → ![](path)
    3. Remove empty spacer divs
    """
    result = []
    i = 0
    while i < len(text):
        # Check for <div style={{textAlign:
        div_match = re.match(
            r"<div\s+style=\{\{textAlign:\s*'center'\}\}\s*>", text[i:]
        )
        if div_match:
            # Find matching </div>
            _, div_end = extract_tag_content(text, i, 'div')
            if div_end != -1:
                inner = text[i + div_match.end():div_end - len('</div>')]
                converted = _convert_image_block(inner)
                result.append(converted)
                i = div_end
                continue
            else:
                result.append(text[i])
                i += 1
                continue

        # Check for standalone <img ... />
        img_match = re.match(r'<img\s+([^>]+?)\s*/?>', text[i:])
        if img_match:
            attrs = img_match.group(1)
            converted = _img_attrs_to_markdown(attrs)
            result.append(converted)
            i += img_match.end()
            continue

        # Remove empty div spacers
        empty_div = re.match(
            r"<div\s+style=\{\{[^}]+\}\}\s*>\s*</div>\s*", text[i:]
        )
        if empty_div:
            i += empty_div.end()
            continue

        result.append(text[i])
        i += 1

    return ''.join(result)


def _convert_image_block(inner: str) -> str:
    """Convert inner content of a centered div block (img + optional caption)."""
    img_match = re.search(r'<img\s+([^>]+?)\s*/?>', inner)
    if not img_match:
        return inner.strip()

    md_img = _img_attrs_to_markdown(img_match.group(1))

    # Extract caption
    caption = ''
    p_match = re.search(r'<p[^>]*>(.+?)</p>', inner, re.DOTALL)
    if p_match:
        caption = '\n*' + p_match.group(1).strip() + '*'

    return md_img + caption


def _img_attrs_to_markdown(attrs: str) -> str:
    """Convert img tag attributes to ![](path) markdown."""
    # Try require() syntax first
    src_match = re.search(
        r"src=\{require\((['\"])([^'\"]+)\1\)\.default\}", attrs
    )
    if src_match:
        path = src_match.group(2)
    else:
        # Try plain src
        src_match = re.search(r'src=["\']([^"\']+)["\']', attrs)
        path = src_match.group(1) if src_match else ''

    alt_match = re.search(r'alt=["\']([^"\']*)["\']', attrs)
    alt = alt_match.group(1) if alt_match else ''

    return f'![{alt}]({path})'


def convert_standalone_require_images(text: str) -> str:
    """Convert any remaining {require('path').default} references to the path."""
    return re.sub(
        r"\{require\((['\"])([^'\"]+)\1\)\.default\}",
        r'\2',
        text
    )


# ═══════════════════════════════════════════════════════════════════════════════
# Text-level conversions
# ═══════════════════════════════════════════════════════════════════════════════

def remove_imports(text: str) -> str:
    """Remove ES6 import statements."""
    text = re.sub(r'^import\s+.+?\s+from\s+[\'"][^\'"]+[\'"];?\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^import\s+[\'"][^\'"]+[\'"];?\s*$', '', text, flags=re.MULTILINE)
    return text


def convert_frontmatter(text: str) -> Tuple[dict, str]:
    """Extract frontmatter; return (metadata, body)."""
    meta = {}
    body = text
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            line = line.strip()
            if ':' in line:
                key, _, value = line.partition(':')
                meta[key.strip()] = value.strip()
        body = text[fm_match.end():]
    return meta, body


def convert_relative_links(text: str) -> str:
    """Rewrite .mdx links to .md."""
    return re.sub(r'\[([^\]]*)\]\(([^)]+)\.mdx\)', r'[\1](\2.md)', text)


def clean_whitespace(text: str) -> str:
    """Collapse excessive blank lines, strip trailing whitespace."""
    text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text


# ═══════════════════════════════════════════════════════════════════════════════
# Main pipeline
# ═══════════════════════════════════════════════════════════════════════════════

def convert_mdx_to_md(text: str) -> str:
    """Full MDX → Markdown conversion pipeline."""

    # 0. Extract frontmatter
    meta, body = convert_frontmatter(text)

    # 1. Remove imports
    body = remove_imports(body)

    # 2. Convert multi-line JSX components (order matters!)
    body = convert_diff_viewer(body)        # Before Tabs (DiffViewer may contain Tabs-like content)
    body = convert_plugin_file_tree(body)    # Before Tabs
    body = convert_tabs(body)               # Tabs/TabItem

    # 3. Convert inline JSX components (before HTML/image processing)
    body = convert_skript_card(body)         # Self-closing, may contain \n escapes
    body = convert_url_card(body)            # Self-closing
    body = convert_colored_link(body)        # Must come BEFORE highlight
    body = convert_highlight(body)           # Strip highlight tags
    body = convert_comment(body)             # Comment text extraction
    body = convert_yellow(body)              # Strip Yellow tags

    # 4. Convert images and divs
    body = convert_images_and_divs(body)
    body = convert_standalone_require_images(body)

    # 5. Convert links
    body = convert_relative_links(body)

    # 6. Clean up
    body = clean_whitespace(body)
    body = body.strip()

    # 7. Build output
    parts = []
    if meta.get('title'):
        parts.append(f"# {meta['title']}\n")
    parts.append(body)

    return '\n'.join(parts)


# ═══════════════════════════════════════════════════════════════════════════════
# File processing
# ═══════════════════════════════════════════════════════════════════════════════

def process_directory(src_dir: Path, dst_dir: Path):
    """Recursively convert all .mdx files to .md."""
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)

    if dst_dir.exists():
        shutil.rmtree(dst_dir)

    count = 0
    for src_file in sorted(src_dir.rglob('*.mdx')):
        rel_path = src_file.relative_to(src_dir)
        dst_file = dst_dir / rel_path.with_suffix('.md')
        dst_file.parent.mkdir(parents=True, exist_ok=True)

        print(f'  {rel_path}')
        try:
            content = src_file.read_text(encoding='utf-8')
            converted = convert_mdx_to_md(content)
            dst_file.write_text(converted, encoding='utf-8')
            count += 1
        except Exception as e:
            print(f'    ERROR: {e}')

    return count


if __name__ == '__main__':
    print(f'Source: {SRC_DIR}')
    print(f'Destination: {DST_DIR}')
    print()
    n = process_directory(SRC_DIR, DST_DIR)
    print(f'\nDone! Converted {n} files -> {DST_DIR}')
