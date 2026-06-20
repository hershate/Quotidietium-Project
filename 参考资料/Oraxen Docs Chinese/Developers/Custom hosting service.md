---
description: 本教程由 Karlatemp 提供
cover: https://www.nosolohacking.info/wp-content/uploads/2017/11/error2.jpg
coverY: 0
---

# 自定义托管服务

## 第一步

创建一个实现 HostingProvider 接口的新类。

## 第二步

在 settings.xml/Pack.upload.options 中插入一个空的配置节。

## 第三步

将 settings.xml/Pack.upload.options.class 设置为外部托管提供者类的路径。

## 最后一步

将 settings.xml/Pack.upload.type 设置为 "external"（必须）。