from Enemy import *
import random

class Ogre(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around!")

def special_attack(self):
        did_special_attack_works = random.random() < 0.20
        if did_special_attack_works:
              self.attack_damage += 4
              print(' Ogre gets angry and increases attack by 4 units')