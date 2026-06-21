# 音频格式转换说明

> 说明：
> 该脚本以oraxen插件提供的 `welcome.ogg` 为参考标准，将当前目录下**所有其他 `.ogg` 文件**（自动跳过已转换的 `*_converted.ogg`）的音频参数统一为与参考文件一致的格式。
> 适用于 Oraxen 资源包需要统一旧版 Vorbis 编码格式的场景。

该脚本由正版ID为 **ZTF3** 的玩家编写与维护。

转换参数对照如下：

| 参数 | 源文件 | 转换后 |
|------|:-----:|:------:|
| 编码 | Opus | Vorbis (libvorbis) |
| 采样率 | 48000 Hz | 44100 Hz |
| 声道 | 立体声 | 立体声 |
| 码率 | ~128 kbps | ~96 kbps |

使用前提：

- 系统需安装 [ffmpeg](https://ffmpeg.org/) 并确保可在命令行中直接调用
- Python 3.12

使用方法：

```bash
python convert_to_oraxen_ogg.py
```

运行后会在同目录下为每个源文件生成对应的 `*_converted.ogg` 文件（例如 `nugalaetiter_light_converted.ogg`）。

该文件夹内容和仓库中其他内容一样，统一采用 Apache License 2.0 协议开源。
