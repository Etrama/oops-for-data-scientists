import sys 

class Pokemon():
    def __init__(self):
        self._hp = 100
        self._attack = 0
        self._defense = 0

    @property
    def attack(self): # attack getter
        return self._attack
    
    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def defense(self): # defense getter
        return self._defense
    
    @defense.setter
    def defense(self, value):
        self._defense = value

if __name__ == "__main__":
    print(sys.executable)
    print(sys.version)
    pokemon = Pokemon()
    print(f"The pokemon's attack stat is: {pokemon.attack}") #using the getter
    print(f"The pokemon's defense stat is: {pokemon.defense}") #using the getter
    pokemon.attack = 50 #using the setter
    pokemon.defense = 30 #using the setter
    print(f"The pokemon's attack stat is: {pokemon.attack}") #using the getter
    print(f"The pokemon's defense stat is: {pokemon.defense}") #using the getter