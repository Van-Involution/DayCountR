# DayCountR

**English** | [中文](README_cn.md)

> **Note**: DayCountR is developed based on [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged), and **DO NOT** support MCDR v0.x

**DayCountR** is a MCDR plugin, which is reforged from [Fallen_Breath](https://github.com/Fallen-Breath)/[**daycount**](https://github.com/TISUnion/daycount), provide command `!!days` and callable function `get_day_count()` to get day count since server set up.

Use `config/DayCountR.yml` as configure file, you can set **start date** of your server, and customize the **reply message**.

## Installation

### Latest Release

Download latest `DayCountR-<version>.zip` from [**Releases Page**](https://github.com/Van-Involution/DayCountR/releases) and unzip it, then put `DayCountR.py` into `plugins/` directory.

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

Plugin will generate reply message with reading config file in `cinfig/DayCountR.yml`, if failed to read config file, then write the following as default content of config file:

```YAML
# Configure file for DayCountR
# Check https://github.com/Van-Involution/DayCountR for detail

# Date of server set up like "YYYY-MM-DD"
start_date: <today>

# Customize reply message, use {days} as format key
reply_msg: Today, server has been set up for §e{days}§r days!
```
The following are explanations of all config items:

- `start_date`: Date of server set up, when generate default config file, `<today>` will be replaced by date of generation
- `reply_msg`: Content of reply message, support [**Formatting codes**](https://minecraft.gamepedia.com/Formatting_codes), when generate text, `{days}` in the string will be replaced by day count

### Command

Plugin provides command `!!days` to get day count of server has been set up, reply message with hover text `<start_date> -> <today_date>`.

### Function

Plugin defines a callable function:

```Python
def get_day_count(server: ServerInterface) -> Union[RText, str]
```
Default return is generated **RText** object, if some exceptions are raised while function running, it will return the exception message string.
