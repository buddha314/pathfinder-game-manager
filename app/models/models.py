# -*- coding: utf-8 -*-
from flask import current_app
from sqlalchemy import func

from . import db

class PlayerCharacter(object):
    def ability_bonus(self, ascore):
        abonus = {(1):-5,
            (2):-4,
            (3):-4,
            (4):-3,
            (5):-3,
            (6):-2,
            (7):-2,
            (8):-1,
            (9):-1,
            (10):0,
            (11):0,
            (12):1,
            (13):1,
            (14):2,
            (15):2,
            (16):3,
            (17):3,
            (18):4,
            (19):4,
            (20):5,
            (21):5,
            (22):5,
            (23):6,
            (24):6,
            }

        return abonus.get(ascore)



