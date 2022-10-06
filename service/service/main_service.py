import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import skyfield
from skyfield.api import load

class Planeta():

    def __init__(self):
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo VADER a ser usado
        """

        self.planets = load('de421.bsp')



    def executar_rest(self, planetas):
        response = {}
        ts = load.timescale()
        t = ts.now()


        astrometric = self.planets[str(planetas['planeta1']).upper()+' BARYCENTER']\
        .at(t).observe(self.planets[str(planetas['planeta2']).upper()+' BARYCENTER'])
        ra, dec, distance = astrometric.radec()

        response['Tempo terrestre'] = t.tt_strftime()
        response['Coordenadas H'] = json.dumps(ra.__dict__)
        response['Coordenadas G'] = json.dumps(dec.__dict__)
        response['Distancia'] = json.dumps(distance.__dict__)



        return response
