import pygame

class NPC:
    def __init__(self, x, y, width, height, color, name, dialogue):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.name = name
        self.dialogue = dialogue
        self.interaction_range = 50  # Reichweite für Interaktion

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def interact(self, player_rect):
        if self.rect.colliderect(player_rect.inflate(self.interaction_range, self.interaction_range)):
            return self.dialogue
        return None
