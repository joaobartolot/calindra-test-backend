from ..model.endereco import EnderecoModel
from ..model.distancia import DistanciaModel
from utils.geometria import calcular_distancia_euclidiana
import requests
import os

from dotenv import load_dotenv
load_dotenv()


class EnderecoService():
    def get_geocoding(self, endereco_str: str):
        maps_api_response = requests.get(
            url=f"https://maps.googleapis.com/maps/api/geocode/json?address={endereco_str}&key={os.environ['API_KEY']}").json()

        if maps_api_response['status'] == "OK":
            result = maps_api_response['results'][0]

            location = result['geometry']['location']

            endereco = EnderecoModel(
                endereco_str, location['lat'], location['lng'])

            return endereco

        raise Exception(maps_api_response['status'])

    def calcular_distancia_cidades(self, cidades: list[EnderecoModel], euclidiana: bool = False):
        distancias: list[DistanciaModel] = list()

        for i in range(len(cidades)):
            distancia = DistanciaModel(cidades[i])
            for j in range(i + 1, len(cidades)):
                distancia.endereco_b = cidades[j]
                distancia.calcular_distancia(euclidiana)

                distancias.append(distancia)

        return distancias
