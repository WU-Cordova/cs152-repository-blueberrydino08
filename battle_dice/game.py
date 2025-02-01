import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        self._player1 = player1
        self._player2 = player2 
        pass

    def attack(self, attacker: Character, defender: Character) -> None:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack."""
        
        random_roll = random.randint(1, 6)
        #                                    accesses attack_power within the attacker 
        attack_value = random_roll * attacker.attack_power
        print(f"{attacker.name} attacks {defender.name} with {attack_value}.")
        defender.health -= attack_value
        print(f"{defender.name}'s health is {defender.health}")
        if defender.health <= 0: 
            #     format string; same as print(str(defender) + "...")
            print(f"{defender.name} has been defeated.")
    
    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """
        while self._player1.health and self._player2.health > 0: 
            self.attack(self._player1, self._player2)
            if self._player2.health <= 0: 
                break 
            self.attack(self._player2,self._player1)
            if self._player1.health <= 0: 
                break 
     
                

