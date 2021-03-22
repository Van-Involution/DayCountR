from datetime import date
from pathlib import Path

from ruamel.yaml import load, Loader

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import RText

PLUGIN_METADATA = {
    'id': 'day_count_reforged',
    'version': '1.0.3',
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

config: dict
today_date: date
start_date: date


def get_config(server: ServerInterface):
    if not Path(DEFAULT_CONFIG_PATH).is_file():
        server.logger.info('Fail to read config file, using default value')
        with open(DEFAULT_CONFIG_PATH, 'w') as default_cfg:
            default_cfg.write(DEFAULT_CONFIG)
    with open(DEFAULT_CONFIG_PATH, 'r') as cfg:
        return load(cfg, Loader)


def getday():
    """
    An API for https://github.com/eagle3236/joinMOTD_Plus

    :return: A string shows days from server setup
    """
    global config, today_date, start_date
    today_date = date.today()
    start_date = config.get('start_date', today_date)
    return str((today_date - start_date).days)


def get_day_count():
    global config, today_date, start_date
    days = getday()
    return RText(
        config.get('reply_msg', 'Today, server has been set up for §e{days}§r days!')
        .format(days=days)
    ).h(f'§l{start_date}§r -> §l{today_date}§r')


def on_load(server: ServerInterface, prev):
    global config
    config = get_config(server)
    server.register_help_message('!!days', 'Get day count since server set up')
    server.register_command(
        Literal('!!days').runs(lambda src: src.reply(get_day_count()))
    )
