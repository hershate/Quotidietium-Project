# 🛜 Lobfile

**用户友好** **免费**

对于初学者来说，Lobfile 实际上是一个非常不错的资源托管解决方案。它在大多数地区运行良好 —— 当然，像中国大陆这样的网络限制较重的地区除外。

<details>
  <summary>获取 API 密钥</summary>

1️⃣ 访问 **https://lobfile.com/** 并注册一个账号  
2️⃣ 点击 `Account` -> `Settings`  
3️⃣ 点击 **Copy API Key to Clipboard**

</details>

```yaml
resource-pack:
  delivery:
    hosting:
      - type: "lobfile"
        api_key: "abcdefghijkl"
        # 可选选项
        use_environment_variables: false # 是否使用环境变量提供机密信息，默认为 false
```

<details>
  <summary>可用环境变量</summary>
  - CE_LOBFILE_API_KEY
</details>
