class Pokemon:
    _total_pokemon= 0
    def __init__(self, _name, _type,_level, _hp):
        self._name = _name
        self._type = _type
        self._level = _level
        self._hp= _hp
        Pokemon._total_pokemon += 1

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    def getLevel(self):
        return self._level

    def getHp(self):
        return self._hp

    def total_pokemon_caught():
        return Pokemon._total_pokemon


class Charmander(Pokemon):
    def __init__(self, _name, _type,_level, _hp):
        Pokemon.__init__(self, _name, _type,_level, _hp)
    def emberAttack(self):
        print("charmander spits dat fire")
