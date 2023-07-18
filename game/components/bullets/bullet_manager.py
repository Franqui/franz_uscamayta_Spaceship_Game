import pygame

class BulletManager:
    
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        
    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != 'enemy':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            # colliderect verifica si el objeto coliciona con otro q le pasa como parametro
            # en este caso especifico bullet.rect.colliderect tiene como argumento l player.rect
            # si bullet rect coliciona con player,rect entonces retorna Verdadero y Falso si no colicionan 
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                #si colicionan entonces bullet es removido y el juego termina
                self.enemy_bullets.remove(bullet)
                #poniendo en falso playing de game el juego termina
                game.playing = False
                # espera con delay un segundo antes de terminar todo
                pygame.time.delay(1000)
                break
            
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
           self.enemy_bullets.append(bullet) 