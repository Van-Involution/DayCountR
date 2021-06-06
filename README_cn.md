# DayCountR

[English](README.md) | **中文**

> **注意**：DayCountR 基于 [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged) 开发，并且**不支持** MCDR v0.x

**DayCountR** 是一个 MCDR 插件，由 [Fallen_Breath](https://github.com/Fallen-Breath) / [**daycount**](https://github.com/TISUnion/daycount) 重制而成，提供获取开服天数的 `!!days` 命令，以及对应函数 `get_day_count()`。

使用配置文件 `config/DayCountR.yml`，可设置服务器的 **开服日期**，并自定义服务端**回复的消息**。

## 安装插件

### 最新发布

在 [**Releases 页面**](https://github.com/Van-Nya/DayCountR/releases)下载最新的 `DayCountR-<版本号>.zip`，解压后将 `DayCountR.py` 放入 `plugins/` 目录中。

### 最新源码

将仓库克隆（`git clone`）至 `plugins/` 目录中，并按如下代码块编辑 **MCDR 实例**的 `config.yml`：

```YAML
# The list of directory path where MCDR will search for plugin to load
# Example: "path/to/my/plugin/directory"
plugin_directories:
- plugins
- plugins/DayCountR
```

## 使用插件

### 配置

编辑插件的 `Config` 类修改配置：

```Python
class Config:
    START_DATE = '2019-09-07'  # 格式：YYYY-MM-DD
    REPLY_MSG = '今天已经开服 §e{}§r 天了！' # 用 {} 作为替换键名
```

### 命令

插件提供 `!!days` 命令获取开服日期，回复的消息带有内容为 `<开服日期> -> <今天日期>` 悬停文本。

### 函数

插件定义了一个可供引用的函数：

```Python
def get_day_count() -> RTextBase:
    ...
```

返回值为生成的 **RText** 对象。
