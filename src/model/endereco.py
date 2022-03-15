

from select import select


class EnderecoModel():
    def __init__(self, endereco: str, lat: int, lng: int):
        self.endereco: str = endereco
        self.lat: int = lat
        self.lng: int = lng

    def ponto_cartesiano(self):
        return self.lat, self.lng

    def to_json(self):
        return {
            'endereco': self.endereco,
            'lat': self.lat,
            'lng': self.lng,
        }
