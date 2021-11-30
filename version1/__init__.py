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
    base_endowment=100

class Subsession(BaseSubsession):
# group and types are defined in the Subsession class
    def creating_session(self):
    # to set initial values in the subsession
        self.group_randomly(fixed_id_in_group = True)
        # built-in function that  shuffles players randomly but keeps the id constant
        for g in self.get_groups():
        # returns a list of all the groups in the subsession
        # loop through the groups in the subsession
            for p in g.get_players():
            # get_players() -> returns a list of all the players in the subsession.
            # loop through the players in the subsession (p is a player)
                if p.id_in_group % 2 == 0:
                  # id_in_group -> player's attribute (unique identifier)
                  # if the id is even (via modulo operator)
                  p.participant.vars['type']= 'OFFICIAL'
                    # the participant is assigned to type "OFFICIAL"
                else:
                # if the participant id is odd
                    p.participant.vars['type'] = 'CITIZEN'
                    # the participant is assigned to type "CITIZEN"
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        return self.participant.vars['type']
    type = models.StringField()

    choice = models.BooleanField(
        labels=" Please choose if you want to demand a bribe or not ",
        choices=[
            [True, "Demand a bribe"],
            [False, "Pay the amount they earned"]
        ]
    )
    amount_demanded = models.CurrencyField()
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
def set_payoffs(self):
    p1 = self.get_player_by_id(1)
    p2 = self.get_player_by_id(2)
    p1.payoff = Constants.base_endowment + self.amount_demanded - Constants.punish_size
    p2.payoff = Constants.base_endowment - amount_demanded - Constants.punishment_cost

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
        return player.id_in_group == 2

class WaitForExtortion(WaitPage) :
    def is_displayed(player: Player) :
        return player.id_in_group == 1

class AMOUNT(Page):
    form_model = "player"
    form_fields = ["amount_demanded"]
    def is_displayed(player: Player):
        return player.id_in_group == 2

class WaitForAmount(WaitPage) :
    def is_displayed(player: Player) :
        return player.id_in_group == 1

class RESPONSE(Page):
    form_model = "player"
    form_fields = ["offer_accepted"]
    def is_displayed(player: Player):
        return player.id_in_group == 1

class WaitForEngagement(WaitPage) :
    def is_displayed(player: Player) :
        return player.id_in_group == 2

class Punishment(Page):
    form_model = "player"
    form_fields = ["punish_choice"]
    def is_displayed(player: Player):
        return player.id_in_group == 1

class WaitForPunishment(WaitPage) :
    def is_displayed(player: Player) :
        return player.id_in_group == 2

class ResultsWaitPage(WaitPage):
    @staticmethod
    after_all_players_arrive = set_payoffs





page_sequence = [MyPage, DECISION, WaitForExtortion,
                 AMOUNT, WaitForAmount, RESPONSE,
                 WaitForEngagement, Punishment, WaitForPunishment,
                 ResultsWaitPage, Results]