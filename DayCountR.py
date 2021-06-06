from datetime import datetime

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import RTextBase, RText

PLUGIN_METADATA = {
    'id': 'day_count_reforged',
    'version': '1.0.3',
    'name': 'DayCountR',
    'description': 'Use command "!!day" to get day count since server set up',
    'author': [
        'Van_Nya',  # Reforged to fit MCDR 1.x
        'Fallen_Breath'  # Source of inspiration
    ],
    'link': 'https://github.com/Van-Nya/DayCountR',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}


class Config:
    """
    Edit config here
    """
    START_DATE = '2019-09-07'  # format: YYYY-MM-DD
    REPLY_MSG = '今天已经开服 §e{}§r 天了!' # use {} as the key


class GetDayCount:
    """
    DO NOT edit here
    """
    def __init__(self):
        self.today_date = datetime.today()
        self.start_date = datetime.strptime(Config.START_DATE, '%Y-%m-%d')
        self.reply_msg = Config.REPLY_MSG

    @property
    def days(self) -> str:
        return str((self.today_date - self.start_date).days)

    def __call__(self) -> RTextBase:
        return RText(self.reply_msg.format(self.days))\
            .h(f'§l{self.start_date.date()}§r -> §l{self.today_date.date()}§r')


def getday() -> str:
    """
    An API for https://github.com/eagle3236/joinMOTD_Plus

    :return: A string shows days from server setup
    """
    return GetDayCount().days


def get_day_count() -> RTextBase:
    """
    An API for https://github.com/Van-Nya/JoinMOTDR

    :return: A formatted RText object
    """
    return GetDayCount()()


def on_load(server: ServerInterface, prev):
    server.register_help_message('!!day', '显示开服至今的天数')
    server.register_command(
        Literal('!!day').runs(lambda src: src.reply(GetDayCount()()))
    )
