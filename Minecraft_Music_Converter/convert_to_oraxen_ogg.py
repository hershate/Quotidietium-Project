"""
将 nugalaetiter_light.ogg 和 nugalaetiter_thick.ogg
转换为与 welcome.ogg 相同的音频参数：
  - 编码: Vorbis (libvorbis)
  - 采样率: 44100 Hz
  - 声道: 立体声 (stereo)
  - 码率: ~96 kbps

依赖: ffmpeg (需在 PATH 中可用)
"""

import subprocess
import json
import sys
import io
from pathlib import Path

# Windows GBK 终端兼容
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ---------- 配置 ----------
SCRIPT_DIR = Path(__file__).parent
REFERENCE_FILE = SCRIPT_DIR / "welcome.ogg"
TARGET_FILES = [
    SCRIPT_DIR / "nugalaetiter_light.ogg",
    SCRIPT_DIR / "nugalaetiter_thick.ogg",
]
OUTPUT_SUFFIX = "_converted.ogg"  # 输出文件后缀，例如 nugalaetiter_light_converted.ogg
# -------------------------


def probe_audio_params(file_path: Path) -> dict | None:
    """使用 ffprobe 获取音频流的参数"""
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        "-select_streams", "a:0",
        str(file_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        streams = data.get("streams", [])
        if not streams:
            print(f"  ❌ 未找到音频流: {file_path.name}")
            return None

        s = streams[0]
        return {
            "codec": s.get("codec_name"),
            "sample_rate": int(s.get("sample_rate", 0)),
            "channels": s.get("channels"),
            "channel_layout": s.get("channel_layout", "stereo"),
            "bit_rate": s.get("bit_rate"),
        }
    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"  ❌ 无法探测音频参数: {file_path.name} — {e}")
        return None


def convert_to_match(src: Path, dst: Path, ref_params: dict) -> bool:
    """使用 ffmpeg 将 src 转换为与 ref_params 一致的参数，输出到 dst"""
    cmd = [
        "ffmpeg",
        "-y",                              # 覆盖已存在的输出文件
        "-i", str(src),
        "-c:a", "libvorbis",               # 编码: Vorbis
        "-ar", str(ref_params["sample_rate"]),  # 采样率: 44100
        "-ac", str(ref_params["channels"]),     # 声道数: 2
        "-b:a", str(ref_params["bit_rate"]),    # 码率: 96000
        "-q:a", "3",                       # Vorbis 质量等级 (0-10, 3≈96kbps)
        "-vn",                             # 无视频流
        str(dst),
    ]
    print(f"  🎵 执行: ffmpeg -i {src.name} -c:a libvorbis "
          f"-ar {ref_params['sample_rate']} -ac {ref_params['channels']} "
          f"-b:a {ref_params['bit_rate']} {dst.name}")

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ 转换失败: {src.name}")
        print(f"     stderr: {e.stderr[:500]}")
        return False


def main():
    print("=" * 60)
    print("  Minecraft Music Converter — 统一音频参数")
    print("=" * 60)

    # 1. 探测参考文件的参数
    print(f"\n📖 探测参考文件: {REFERENCE_FILE.name}")
    ref_params = probe_audio_params(REFERENCE_FILE)
    if ref_params is None:
        print("错误: 无法读取参考文件参数，终止。")
        sys.exit(1)

    print(f"   ✅ 参考参数:")
    print(f"      - 编码:       {ref_params['codec']}")
    print(f"      - 采样率:     {ref_params['sample_rate']} Hz")
    print(f"      - 声道:       {ref_params['channels']} ({ref_params['channel_layout']})")
    print(f"      - 码率:       {ref_params['bit_rate']} bps")

    # 2. 依次转换目标文件
    success_count = 0
    for target in TARGET_FILES:
        if not target.exists():
            print(f"\n⚠️  跳过: 文件不存在 — {target.name}")
            continue

        print(f"\n📝 处理: {target.name}")

        # 探测源文件参数（仅供展示）
        src_params = probe_audio_params(target)
        if src_params:
            print(f"   🔸 源参数: {src_params['codec']}, {src_params['sample_rate']} Hz, "
                  f"{src_params['channels']}ch, {src_params['bit_rate']} bps")

        # 输出文件名
        stem = target.stem  # 去掉 .ogg 后缀
        output_path = target.with_name(stem + OUTPUT_SUFFIX)

        if convert_to_match(target, output_path, ref_params):
            # 验证输出文件
            out_params = probe_audio_params(output_path)
            if out_params and out_params["codec"] == ref_params["codec"]:
                print(f"   ✅ 转换成功: {output_path.name}")
                print(f"      - 编码: {out_params['codec']}")
                print(f"      - 采样率: {out_params['sample_rate']} Hz")
                print(f"      - 声道: {out_params['channels']}")
                print(f"      - 码率: {out_params['bit_rate']} bps")
                success_count += 1
            else:
                print(f"   ⚠️  文件已生成但参数验证异常: {output_path.name}")
        else:
            print(f"   ❌ 转换失败: {target.name}")

    # 3. 汇总
    print("\n" + "=" * 60)
    print(f"  完成: {success_count}/{len(TARGET_FILES)} 个文件转换成功")
    print("=" * 60)


if __name__ == "__main__":
    main()
