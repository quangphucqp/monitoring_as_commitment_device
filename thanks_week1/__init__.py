from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'thanks_week1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class ThanksWeek1(Page):
    pass


page_sequence = [ThanksWeek1]
