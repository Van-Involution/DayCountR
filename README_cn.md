# DayCountR

[English](README.md) | **中文**

> **注意**：DayCountR 基于 [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged) 开发，并且**不支持** MCDR v0.x

**DayCountR** 是一个 MCDR 插件,由 [Fallen_Breath](https://github.com/Fallen-Breath)/[**daycount**](https://github.com/TISUnion/daycount) 重制而成, 提供获取开服天数的 `!!days` 命令，以及对应函数 `get_day_count()`。

使用配置文件 `config/DayCountR.yml`，可设置服务器的 **开服日期**，并自定义服务端**回复的消息**。

## 安装插件

### 最新发布

在 [**Releases 页面**](https://github.com/Van-Involution/DayCountR/releases)下载最新的 `DayCountR-<版本号>.zip`，解压后将 `DayCountR.py` 放入 `plugins/` 目录中。

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

插件在生成回复消息时会读取路径为 `cinfig/DayCountR.yml` 配置文件，若找不到配置文件，则写入如下的默认配置文件内容：

```YAML
# Configure file for DayCountR
# Check https://github.com/Van-Involution/DayCountR for detail

# Date of server set up like "YYYY-MM-DD"
start_date: <today>

# Customize reply message, use {days} as format key
reply_msg: Today, server has been set up for §e{days}§r days!
```
以下为各配置项的解释：

- `start_date`：开服日期，默认配置文件生成时，`<today>` 会被替换成当天日期
- `reply_msg`：回复的消息正文，支持[**格式化代码**](https://minecraft-zh.gamepedia.com/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)，生成文本时字符串中的 `{days}` 会被替换成开服天数

### 命令

插件提供 `!!days` 命令获取开服日期，回复的消息带有内容为 `<开服日期> -> <今天日期>` 悬停文本。

### 函数

插件定义了一个可供引用的函数：

```Python
def get_day_count(server: ServerInterface) -> Union[RText, str]
```
默认返回值为生成的 **RText** 对象，如果函数运行时出现异常则返回字符串格式的异常消息。
