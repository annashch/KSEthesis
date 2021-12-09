from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

import numpy as np

doc = """
One player decides whether to demand a bribe, chooses a bribe amount, and then may get rejected"""


class Constants(BaseConstants):
    name_in_url = 'version1'
    players_per_group = 2
    num_rounds = 1
    punishment_cost = 5
    punish_size = 20
    citizen_role = 'Citizen'
    official_role = 'Official'

class Subsession(BaseSubsession):

    def creating_session(subsession: Subsession):
        players = subsession.get_players()

for p in players:
    p.is_official =  Constants.official_role
    p.is_citizen= Constants.citizen_role

if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            participant.endowment = random.choice([50, 100, 150])

import itertools
treatments = itertools.cycle(
    itertools.product([50, 100, 150])
    for p in subsession.get_players():
    if p.is_citizen:
        p.endowment = next(treatments)


class Group(BaseGroup):
    pass

class Official(Page):
    @staticmethod
    def is_displayed(player):
        return player.role == Constants.official_role

class Citizen(Page):

    @staticmethod
    def is_displayed(player):
        return player.role == Constants.citizen_role

class RoleAssignment(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    title_text = 'Waiting Room'
    body_text = 'Please wait! The experiment will continue momentarily'


class Player(BasePlayer):
    choice = models.BooleanField(
        labels=" Please choose if you want to demand a bribe or not ",
        choices=[
            [True, "Demand a bribe"],
            [False, "Pay the amount they earned"]
        ]
    )
    amount_demanded = models.CurrencyField(label='Please indicate the amount of bribe demanded', max=20, min=0)

    offer_accepted = models.BooleanField(
        labels=" Please if you are willing to accept the bribe requested",
        choices=[
            [True, "Pay the bribe requested"],
            [False, "Pay the amount they earned"]
        ]
    )
    punish_choice = models.BooleanField(
        choices=[
            [True, "Punish"],
            [False, "Do not punish"]
        ]
    )



# FUNCTIONS
def set_payoffs(group:Group):
    official = group.get_player_by_role(Constants.official_role)
    citizen = group.get_player_by_role(Constants.citizen_role)

for player.role == Constants.agent_role
    official.payoff = participant.endowment + self.amount_demanded - Constants.punish_size

    citizen.payoff = participant.endowment - amount_demanded - Constants.punishment_cost

for amount_demanded in range (0,20)
    punish_prob = amount_demanded*0.04
    ##punishment probability
    nopunish_prob = 1-punish_prob
    result = np.random.choice(['Punish', 'No punish'], p = [punish_prob, nopunish_prob])

# PAGES
class DECISION(Page):
    form_model = "player"
    form_fields = ["choice"]
    def is_displayed(player: Player):
        return player.role == Constants.official_role

class WaitForExtortion(WaitPage) :
    def is_displayed(player: Player) :
        return player.role == Constants.citizen_role

class AMOUNT(Page):
    form_model = "player"
    form_fields = ["amount_demanded"]
    def is_displayed(player: Player):
        return player.role == Constants.official_role

class WaitForAmount(WaitPage) :
    def is_displayed(player: Player) :
        return  player.role == Constants.citizen_role

class RESPONSE(Page):
    form_model = "player"
    form_fields = ["offer_accepted"]
    def is_displayed(player: Player):
        return Constants.citizen_role

class WaitForEngagement(WaitPage) :
    def is_displayed(player: Player) :
        return Constants.official_role

class Punishment(Page):
    form_model = "player"
    form_fields = ["punish_choice"]
    def is_displayed(player: Player):
        return Constants.citizen_role

class WaitForPunishment(WaitPage) :
    def is_displayed(player: Player) :
        return Constants.official_role

class ResultsWaitPage(WaitPage):
    @staticmethod
    after_all_players_arrive(group:Group):
    if





page_sequence = [Official,Citizen, DECISION, WaitForExtortion,
                 AMOUNT, WaitForAmount, RESPONSE,
                 WaitForEngagement, Punishment, WaitForPunishment,
                 ResultsWaitPage, ResultsWaitPage]