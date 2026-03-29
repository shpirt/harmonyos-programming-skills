# HarmonyOS 编程 Skills

中文说明：当前文件  
English version: [README.en.md](./README.en.md)

这个仓库收录了五个可复用的 HarmonyOS / OpenHarmony 编程辅助 skill：

- `harmonyos-project-builder`
- `harmonyos-sdk-build-deploy`
- `harmonyos-arkts-v2-assistant`
- `harmonyos-test-kit`
- `harmonyos-ui-ux-guidelines`

它们被设计为一组协同工作的能力，分别覆盖项目搭建、官方 SDK 构建部署、ArkTS / `.ets` 编写指导、官方 Test Kit 测试工作流，以及 HarmonyOS 官方 UI/UX 设计规范审查。

## 包含的 skill

### `harmonyos-project-builder`

适用于将空项目或半成品 HarmonyOS 项目逐步补齐为可工作的完整项目。

重点覆盖：

- 项目脚手架与目录结构
- DevEco 与 hvigor 工程布局
- 架构分层与边界划分
- 分阶段验证与交付推进

### `harmonyos-sdk-build-deploy`

适用于需要使用 HarmonyOS 官方 SDK 工具链完成以下任务的场景：

- 编译
- 打包
- 安装
- 启动
- 查看日志
- 签名
- 真机调试

重点覆盖：

- `hdc`
- `bm`
- `aa`
- `packing-tool`
- `binary-sign-tool`

### `harmonyos-arkts-v2-assistant`

适用于 ArkTS 或 `.ets` 编写、修改和排错场景。

重点覆盖：

- ArkUI V2
- ArkUI V1 旧项目维护
- ArkTS 与 TypeScript 语法差异
- `.ets` 日常编写模式
- MVVM 与组件边界

### `harmonyos-test-kit`

适用于 HarmonyOS 官方 Test Kit 测试相关任务。

重点覆盖：

- `@ohos/hypium` 单元测试
- `@kit.TestKit` / `@ohos.UiTest` UI 测试
- `PerfTest` 白盒性能测试
- `ohosTest` / `testRunner` / `module.json5` 接线
- `aa test` 命令行执行与筛选

### `harmonyos-ui-ux-guidelines`

适用于 HarmonyOS / OpenHarmony 应用的 UI/UX 设计决策、设计评审和实现验收场景。

重点覆盖：

- 应用导航结构
- 页面结构与多设备布局
- 自适应与响应式设计
- 多模态输入与交互一致性
- 视觉规范、动效规范与控件状态检查
- 基于官方设计规范的实现前约束与实现后审查

## 环境变量

## 推荐本地参考仓库

为了获得更稳定的官方文档检索和官方样例对照，建议在本地准备以下仓库：

```sh
git clone https://gitee.com/openharmony/docs.git
git clone https://gitee.com/openharmony/applications_app_samples.git
```

然后将环境变量指向对应目录：

```sh
export HARMONYOS_DOCS_ROOT="/path/to/docs-repo-or-zh-cn"
export HARMONYOS_SAMPLES_ROOT="/path/to/applications_app_samples"
```

说明：

- `docs` 既可以把 `HARMONYOS_DOCS_ROOT` 指向仓库根目录，也可以直接指向其中的 `zh-cn/` 子目录
- 如果没有本地 docs，skill 会降级到官方 HarmonyOS 文档站
- 如果没有本地 samples，skill 仍可覆盖核心流程；只有在任务确实依赖官方样例时，才会损失部分效果

这些 skill 不依赖硬编码本地路径。

建议在 shell 启动配置中设置以下环境变量，然后重启你的编码助手：

```sh
export HARMONYOS_DOCS_ROOT="/path/to/docs-repo-or-zh-cn"
export HARMONYOS_SAMPLES_ROOT="/path/to/applications_app_samples"
```

示例：

```sh
export HARMONYOS_DOCS_ROOT="$HOME/playground/docs"
export HARMONYOS_SAMPLES_ROOT="$HOME/playground/applications_app_samples"
```

约定如下：

- `HARMONYOS_DOCS_ROOT` 可以指向 docs 仓库根目录，也可以直接指向其中的 `zh-cn/` 子目录
- `HARMONYOS_SAMPLES_ROOT` 应指向 `applications_app_samples` 仓库根目录
- 如果本地 docs 不可用，skill 会降级到官方 HarmonyOS 文档站搜索
- 如果本地 samples 不可用，skill 仍可覆盖核心流程；只有当任务确实依赖样例时，才需要本地 sample

## 如何使用这些 skill

将以下目录复制或同步到你的技能目录：

- `harmonyos-project-builder/`
- `harmonyos-sdk-build-deploy/`
- `harmonyos-arkts-v2-assistant/`
- `harmonyos-test-kit/`
- `harmonyos-ui-ux-guidelines/`

如果你的环境使用集中式技能目录，例如 `$CODEX_HOME/skills`，直接把这些 skill 目录放进去即可。

## 为什么放在一个仓库里

这五个 skill 共享：

- 彼此之间的引用关系
- 相同的环境变量约定
- 一条完整的 HarmonyOS 开发工作流

把它们放在同一个仓库里，可以避免项目架构指导、SDK 构建部署指导、ArkTS 编写指导、测试工作流指导、以及 UI/UX 设计规范指导之间发生版本漂移。
