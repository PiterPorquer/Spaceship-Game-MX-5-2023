import pygame
from game.components.enemies.enemymboss import EnemyMiniBoss
from game.utils.constants import ENEMY_2

class MiniBoss(EnemyMiniBoss):
    WIDTH = 65
    HEIGHT = 85

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        super().__init__(self.image)