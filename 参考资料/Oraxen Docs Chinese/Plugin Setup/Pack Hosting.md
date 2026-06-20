# 资源包托管

Oraxen 允许多种方式托管您的资源包。资源包必须被托管，才能发送给其他玩家。



## 概述

在 Oraxen 生成资源包后，它会自动将资源包上传到一个服务器，该服务器托管资源包并允许其他玩家下载。
资源包可以托管在远程服务器（atlas）上，或使用内置的网页服务器在本地托管。



## Oraxen Atlas（Polymath）

### 一个由 Oraxen 托管的外部服务器，无需开放端口或任何设置即可轻松分发资源包。

Oraxen Atlas 是由 Oraxen 自身托管的外部服务器（Polymath 实例）。它免费、易于使用，是首次设置 Oraxen 时的默认选项。
我们推荐大多数用户使用此方法，因为它简单且大部分可靠。它也不需要额外的服务器端口，是免费 Minecraft 服务器托管商的最佳选择。

### 配置
Oraxen Atlas 默认通过以下配置进行设置。

```yml
upload:
    enabled: true
    type: polymath #transfer.sh、polymath 或 self-host
    polymath:
      server: atlas.oraxen.com # 您也可以托管自己的 polymath 实例
      secret: "oraxen" # 如果您托管自己的 polymath，请更改此项以限制资源包上传访问
```

### 限制与优点
✓ 免费使用
✓ 易于设置
✓ 无需额外端口或设置

✗ 在某些国家可能不可用（俄罗斯、中国）
✗ 可能会偶尔出现停机



## 自托管 Polymath 实例

### 一个必须由您自己托管的服务器。

Oraxen 允许您托管自己的 Polymath 实例并将其连接到 Oraxen。这使您独立于 Oraxen 的 atlas，并解决大多数与国家相关的问题。

### 配置
您可以按照[此指南](https://github.com/oraxen/polymath)托管自己的 Polymath 实例。Polymath 是开源的，设置相对简单。
成功运行自己的 Polymath 实例后，您需要配置 Oraxen 指向它而非默认的实例。

```yml
upload:
    enabled: true
    type: polymath #transfer.sh、polymath 或 self-host
    polymath:
      server: atlas.oraxen.com # 这是您的 polymath 实例运行的域名
      secret: "oraxen" # 这是用于验证请求的密钥，防止其他人向您的 polymath 上传资源包
```

### 限制与优点
✓ 独立于 Oraxen Atlas
✓ 在所有国家可用（包括俄罗斯、中国）

✗ 需要一个网页服务器
✗ 需要额外设置
✗ 需要端口且必须可从外部网络访问



## 自托管 Minecraft 服务器（带开放端口）

### 在您的 Minecraft 服务器上使用 Java 内置的 `com.sun.net.httpserver` 运行。

Oraxen 允许您直接在 Minecraft 服务器上通过开放端口托管自己的资源包服务器。

### 配置

```yml
upload:
    enabled: true
    type: self-host
    self-host:
      host: "0.0.0.0" # HTTP 服务器绑定的 IP 地址（0.0.0.0 = 监听所有网络接口）
      port: 8080 # HTTP 服务器监听的端口
      domain: "localhost:8080" # 玩家用来下载资源包的域名/IP:端口（例如 "my-server.com:8080" 或 "192.168.1.100:8080"）
```

### 限制与优点
✓ 独立于 Oraxen Atlas
✓ 在所有国家可用（包括俄罗斯、中国）

✗ 需要端口且必须可从外部网络访问
✗ 可能使用更多服务器资源（CPU/RAM，但通常不明显）



## 默认设置

```yml
Pack:
  upload:
  enabled: true
  type: polymath #transfer.sh、polymath 或 self-host
  polymath:
    server: atlas.oraxen.com # 您也可以托管自己的 polymath 实例
    secret: "oraxen" # 如果您托管自己的 polymath，请更改此项以限制资源包上传访问
  self-host:
    host: "0.0.0.0" # HTTP 服务器绑定的 IP 地址（0.0.0.0 = 监听所有网络接口）
    port: 8080 # HTTP 服务器监听的端口
    domain: "localhost:8080" # 玩家用来下载资源包的域名/IP:端口（例如 "my-server.com:8080" 或 "192.168.1.100:8080"）
```