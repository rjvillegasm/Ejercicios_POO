from enemy import *

class Zombie(Enemy):
    
    def __init__(self,type_of_enemy ,healt_points, attack_damage):
        super().__init__(type_of_enemy=type_of_enemy,
                         health_points=healt_points,
                         attack_damage=attack_damage)
        