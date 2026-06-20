---
description: PackLayer 通过阻止重复发送资源包来优化代理网络上的资源包分发。
---

# PackLayer - 代理资源包优化

PackLayer 是一个 **Velocity 和 BungeeCord 代理插件**，用于优化多服务器网络上的资源包分发。

## 问题

当玩家在代理网络的各个后端服务器之间切换时，每个服务器通常都会发送自己的资源包请求。如果多个服务器使用**相同的资源包**（例如 Oraxen 的资源包），客户端每次切换时都会被迫重新下载并重新应用——从而导致：

- 切换服务器时的**不必要的延迟**
- 玩家和服务器的**带宽浪费**
- 带有加载画面的**糟糕玩家体验**

## 解决方案

PackLayer 在代理层面拦截发出的 `ResourcePackSend` 数据包，并**取消重复项**。如果玩家已经拥有具有匹配哈希值的资源包，该数据包将被丢弃，从而使服务器切换瞬间完成。

## 安装

1. 从 [GitHub Releases](https://github.com/oraxen/bungee-pack-layer/releases) 下载最新的 `bungee-pack-layer-X.X.X.jar`
2. 将其放入你的**代理的 plugins 文件夹**（Velocity 或 BungeeCord）
3. 重启你的代理
4. （可选）编辑生成的 `config.yml` 以自定义行为

**注意：** 这是一个**代理插件**，而不是后端服务器插件。它安装到 Velocity/BungeeCord 上，而不是 Paper/Spigot 上。

## 配置

PackLayer 在其数据文件夹中生成一个 `config.yml`，包含合理的默认值：

```yaml
# PackLayer 配置

# Skip Mode - 决定 PackLayer 如何决定跳过重复的资源包
# 选项：
#   HASH_ONLY    - 如果 SHA-1 哈希值匹配则跳过（默认，推荐）
#   URL_ONLY     - 如果 URL 匹配则跳过
#   HASH_OR_URL  - 如果哈希值或 URL 任一匹配则跳过
#   HASH_AND_URL - 只有当哈希值和 URL 都匹配时才跳过
#   ALWAYS_SKIP  - 始终跳过资源包发送（仅用于测试）
#   NEVER_SKIP   - 永不跳过（相当于禁用插件）
skip-mode: HASH_ONLY

# Server Filter - 控制 PackLayer 应用于哪些后端服务器
server-filter:
  # 模式：DISABLED（所有服务器）、WHITELIST 或 BLACKLIST
  mode: DISABLED
  # 服务器名称列表（如 Velocity/BungeeCord 配置中定义的）
  servers:
    - lobby
    - hub

# Trusted Domains - 始终跳过来自这些域名的资源包
# 支持通配符：*.example.com, cdn.example.com/*
trusted-domains:
  # - atlas.oraxen.com
  # - cdn.example.com

# 服务器切换后应用跳过逻辑之前的宽限期（毫秒）
# 设置为 0 以禁用。当后端服务器有意重新发送资源包时有用。
server-switch-grace-ms: 0

# 启用调试日志
debug: false

# 启用统计追踪（已跳过的资源包数量、节省的带宽）
statistics-enabled: true
```

## 跳过模式说明

| 模式 | 何时使用 |
|------|-------------|
| `HASH_ONLY` | **默认。** 最适合大多数设置。跳过具有相同 SHA-1 哈希值的资源包。 |
| `URL_ONLY` | 当不同的资源包版本共享相同的 URL 时使用（例如，使用静态 URL 自行托管）。 |
| `HASH_OR_URL` | 最激进。如果哈希值或 URL 任一匹配则跳过。 |
| `HASH_AND_URL` | 最保守。只有当两者完全匹配时才跳过。 |
| `ALWAYS_SKIP` | 仅用于测试/调试。跳过所有资源包发送。 |
| `NEVER_SKIP` | 相当于禁用 PackLayer。 |

## 服务器过滤

你可以将 PackLayer 限制到特定的后端服务器：

```yaml
server-filter:
  mode: WHITELIST
  servers:
    - survival
    - creative
    - minigames
```

或排除特定服务器：

```yaml
server-filter:
  mode: BLACKLIST
  servers:
    - auth  # 不应用于验证服务器
```

## 受信任的域名

跳过来自特定域名的所有资源包，无需检查哈希值：

```yaml
trusted-domains:
  - atlas.oraxen.com      # Oraxen 的默认资源包托管
  - cdn.myserver.com      # 你的 CDN
  - "*.example.com"       # 通配符匹配
```

当你信任资源包来源并希望最小化开销时，这非常有用。

## 命令

所有命令都需要 `packlayer.admin` 权限。

| 命令 | 说明 |
|---------|-------------|
| `/packlayer reload` | 重新加载配置 |
| `/packlayer stats` | 显示跳过统计信息 |
| `/packlayer clear <player\|*>` | 清除玩家的资源包缓存 |
| `/packlayer info <player>` | 显示玩家的已缓存资源包信息 |
| `/packlayer debug` | 显示调试模式状态 |

## Oraxen 网络的最佳实践

### 所有服务器使用单一资源包

如果你的所有后端服务器都使用相同的 Oraxen 资源包：

1. 在你的代理上安装 PackLayer
2. 使用默认设置（`skip-mode: HASH_ONLY`）
3. 完成！玩家只需下载一次资源包。

### 每个服务器使用不同的资源包

如果某些服务器有不同的资源包：

```yaml
server-filter:
  mode: WHITELIST
  servers:
    - survival    # 这些服务器共享相同的资源包
    - creative
    - lobby
```

不在列表中的服务器将始终发送其资源包。

### 使用 Polymath（atlas.oraxen.com）

将 Oraxen 的资源包托管添加到受信任域名以获得最佳性能：

```yaml
trusted-domains:
  - atlas.oraxen.com
```

## 开发者 API

PackLayer 为其他插件提供了事件 API：

```java
// 获取服务（Velocity 示例）
PackLayerVelocityPlugin plugin = /* 获取插件实例 */;
PackLayerService service = plugin.getService();

// 注册事件处理器
service.registerEventHandler(event -> {
    // 在即将发生资源包跳过时调用
    if (shouldForceResend(event.getPlayerId())) {
        event.setCancelled(true); // 强制发送资源包
    }
});

// 手动控制资源包缓存
service.clearPlayer(playerId);
```

## 故障排除

### 资源包仍然被重新发送

1. 在配置中设置 `debug: true` 以查看发生了什么
2. 验证所有后端服务器使用完全相同的资源包（检查 SHA-1 哈希值）
3. 确保 PackLayer 安装在**代理**上，而不是后端服务器上

### 玩家看到旧版本的资源包

清除他们的资源包缓存：
```
/packlayer clear PlayerName
```

### 需要强制重新下载

临时为某个玩家禁用：
```
/packlayer clear PlayerName
```

他们将在下次服务器切换时收到资源包。

## 性能

PackLayer 被设计为轻量级的：

- 正常运行时**零磁盘 I/O**
- **最小内存**占用（仅存储每个玩家的资源包哈希值）
- **无网络开销**（仅拦截数据包，不修改它们）

典型影响：每次资源包检查 **< 1ms 延迟**。

## 兼容性

- **Velocity:** 3.0.0+
- **BungeeCord:** 1.20+
- **Minecraft:** 1.8 - 1.21.x（支持所有版本）

PackLayer 使用 [PacketEvents](https://github.com/retrooper/packetevents) 进行数据包拦截，提供了广泛的版本兼容性。
