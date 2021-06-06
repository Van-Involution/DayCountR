# DayCountR

**English** | [中文](README_cn.md)

> **Note**: DayCountR is developed based on [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged), and **DO NOT** support MCDR v0.x

**DayCountR** is a MCDR plugin, which is reforged from [Fallen_Breath](https://github.com/Fallen-Breath) / [**daycount**](https://github.com/TISUnion/daycount), provide command `!!days` and callable function `get_day_count()` to get day count since server set up.

Use `config/DayCountR.yml` as configure file, you can set **start date** of your server, and customize the **reply message**.

## Installation

### Latest Release

Download latest `DayCountR-<version>.zip` from [**Releases Page**](https://github.com/Van-Nya/DayCountR/releases) and unzip it, then put `DayCountR.py` into `plugins/` directory.

### Latest Source Code

Clone this repository (`git clone`) into `plugins/` directory, then edit `config.yml` of **MCDR instance** as the following codeblock:

```YAML
# The list of directory path where MCDR will search for plugin to load
# Example: "path/to/my/plugin/directory"
plugin_directories:
- plugins
- plugins/DayCountR
```

## Usages

### Config

Configs are in class `Config` of the plugin:

```Python
class Config:
    START_DATE = '2019-09-07'  # format: YYYY-MM-DD
    REPLY_MSG = 'Today, server has been set up for §e{}§r days!' # use {} as the key
```

### Command

Plugin provides command `!!day` to get day count of server has been set up, reply message with hover text `<start_date> -> <today_date>`.

### Function

Plugin defines a callable function:

```Python
def get_day_count() -> RTextBase:
    ...
```

Returns generated **RText** object.
