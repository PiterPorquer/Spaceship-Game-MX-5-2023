from game.components.enemies.ship import Ship
from game.components.enemies.mboss import MiniBoss

class EnemyHandler:
    
    def __init__(self):
        self.enemies = []
    
    def update (self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)
                
    
    def draw (self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy (self):
        if len(self.enemies) <= 5:
            self.enemies.append(Ship())
        if len (self.enemies) < 5:
            self.enemies.append(MiniBoss())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

        