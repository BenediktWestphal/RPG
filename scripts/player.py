import pygame

class Player:
    def __init__(self, x, y, speed, player_width=50, player_height=50):
        self.rect = pygame.Rect(x, y, player_width, player_height)
        self.width = player_width
        self.height = player_height
        self.speed = speed 
        self.color = (0, 0, 255)
        self.coins = 20
        

    def handle_movement(self, keys, walls, screen_width, screen_height):
        new_x, new_y = self.rect.x, self.rect.y

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            new_x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < screen_width - self.width:
            new_x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            new_y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < screen_height - self.height:
            new_y += self.speed

        new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)
        
        if not any(new_rect.colliderect(wall) for wall in walls):
            self.rect.x, self.rect.y = new_x, new_y


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)