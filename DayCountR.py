# -*- coding: UTF-8 -*-

from yaml import load, FullLoader
from datetime import date
from pathlib import Path

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal

PLUGIN_METADATA = {
    'id': 'day_count_reforged',
    'version': '1.0.0',
    'name': 'DayCountR',
    'description': 'Use command "!!days" to get day count since server set up',
    'author': [
        'Van_Involution',  # Reforged to fit MCDR 1.x
        'Fallen_Breath'  # Source of inspiration
    ],
    'link': 'https://github.com/Van-Involution/DayCountR',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}

NAME = PLUGIN_METADATA['name']
DEFAULT_CONFIG_PATH = f'config/{NAME}.yml'
DEFAULT_CONFIG = '''# Configure file for DayCountR

# Date when server set up like "YYYY-MM-DD"
# 开服日期，形如 “YYYY-MM-DD”
start_date: {today}

# Customize your reply msg to cmd-src, use {{days}} as format key
# 自定义回复消息，用 {{days}} 作为格式化键名
reply_msg: Today, server has been set up for \u00a7e{{days}}\u00a7r days!
'''.format(today=date.today().strftime('%Y-%m-%d'))


def get_config(server: ServerInterface):
    if not Path(DEFAULT_CONFIG_PATH).is_file():
        server.logger.info('Fail to read config file, using default value')
        with open(file=DEFAULT_CONFIG_PATH, mode='w') as cfg_0:
            cfg_0.write(DEFAULT_CONFIG)
    with open(file=DEFAULT_CONFIG_PATH, mode='r') as cfg:
        return load(stream=cfg, Loader=FullLoader)


def get_day_count(start_date: date):
    today_date = date.today()
    return (today_date - start_date).days


def format_reply_msg(server: ServerInterface):  # You can call this function in other modules
    config = get_config(server)
    day_count = get_day_count(config['start_date'])
    return config['reply_msg'].format(days=day_count)


def on_load(server: ServerInterface, prev):
    server.register_help_message(prefix='!!days', message='Get day count since server set up')
    server.register_command(
        Literal('!!days').runs(lambda src: src.reply(format_reply_msg(server)))
    )
