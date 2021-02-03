# -*- coding: UTF-8 -*-

from datetime import date
from pathlib import Path

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import RText

PLUGIN_METADATA = {
    'id': 'day_count_reforged',
    'version': '1.0.1',
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
# Check https://github.com/Van-Involution/DayCountR for detail

# Date of server set up like "YYYY-MM-DD"
start_date: {today}

# Customize reply message, use {{days}} as format key
reply_msg: Today, server has been set up for §e{{days}}§r days!
'''.format(today=date.today().strftime('%Y-%m-%d'))


def get_config(server: ServerInterface):
    try:
        from yaml import load, FullLoader
    except Exception:
        server.logger.warning('Failed to import package PyYAML (https://pypi.org/project/PyYAML), install it by command "pip install PyYAML"')
        return None
    else:
        if not Path(DEFAULT_CONFIG_PATH).is_file():
            server.logger.info('Fail to read config file, using default value')
            with open(DEFAULT_CONFIG_PATH, 'w') as default_cfg:
                default_cfg.write(DEFAULT_CONFIG)
        with open(DEFAULT_CONFIG_PATH, 'r') as cfg:
            return load(cfg, FullLoader)


def get_day_count(server: ServerInterface):
    config = get_config(server)
    if config is not None:
        today_date = date.today()
        start_date = config.get('start_date', today_date)
        return RText(
            config.get('reply_msg', 'Today, server has been set up for §e{days}§r days!')
            .format(days=(today_date - start_date).days)
        ).h(f'§l{start_date}§r -> §l{today_date}§r')
    else:
        return f'§cSomething of plugin {NAME} is going wrong, please let admins look up the console!§r'


def on_load(server: ServerInterface, prev):
    server.register_help_message('!!days', 'Get day count since server set up')
    server.register_command(
        Literal('!!days').runs(lambda src: src.reply(get_day_count(server)))
    )
