# 开发者 API

:::danger
该 API 仍在开发中，未来可能会发生变化。使用风险自负！<br/>
> 加入我们的 [Discord 服务器](https://pixelstudios.dev/discord) 以获取最新动态。
:::

### 依赖
将插件的 jar 文件放入项目中的某个文件夹内：

:::note
**Maven：**
```xml
<dependency>
  <groupId>dev.pixelstudios</groupId>
  <artifactId>EpicAchievements</artifactId>
  <version>{version}</version>
  <scope>system</scope>
  <systemPath>${project.basedir}/libs/EpicAchievements.jar</systemPath>
</dependency>
```

**Gradle：**
```groovy
dependencies {
  compileOnly files('libs/EpicAchievements.jar')
}
```
:::

## 用法

### 事件
您可以监听 `dev.pixelstudios.achievements.api.events` 包中的事件。

### 方法
`AchievementsAPI` 类提供了注册自定义任务、奖励和条件的方法（以内置实现为参考）以及其他实用的工具方法。
