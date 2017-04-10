class Pokemon:
    _total_pokemon= 0
    def __init__(self, _name, _type):
        self._name = _name
        self._type = _type
        Pokemon._total_pokemon += 1

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    @staticmethod
    def total_pokemon_caught():
        return Pokemon._total_pokemon
