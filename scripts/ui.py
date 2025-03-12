import pygame

class TradeMenu:
    def __init__(self, screen):
        """Initialisiert das Handelsmenü"""
        self.screen = screen
        self.width = 300
        self.height = 200
        self.x = (screen.get_width() - self.width) // 2
        self.y = (screen.get_height() - self.height) // 2
        self.color = (50, 50, 50)  # Dunkelgrauer Hintergrund
        self.border_color = (200, 200, 200)  # Hellgrauer Rand
        self.font = pygame.font.Font(None, 24)

        # Handelswaren (Item-Name, Preis)
        self.items = [("Schwert", 10), ("Trank", 5), ("Schild", 15)]
        self.selected_index = 0  # Aktuell ausgewähltes Item

        self.active = False  # Handelsmenü ist standardmäßig deaktiviert

    def toggle(self):
        """Aktiviert oder deaktiviert das Handelsmenü"""
        self.active = not self.active

    def draw(self):
        """Zeichnet das Handelsmenü auf den Bildschirm"""
        if not self.active:
            return

        # Zeichne Hintergrund
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, self.border_color, (self.x, self.y, self.width, self.height), 3)

        # Zeichne Items
        for i, (item, price) in enumerate(self.items):
            color = (255, 255, 255) if i == self.selected_index else (180, 180, 180)
            text = self.font.render(f"{item} - {price} Coins", True, color)
            self.screen.blit(text, (self.x + 20, self.y + 30 + i * 30))

        # Hinweistext
        hint = self.font.render("Pfeiltasten: Auswahl | ENTER: Kaufen | ESC: Schließen", True, (255, 255, 255))
        self.screen.blit(hint, (self.x + 10, self.y + self.height - 30))

    def handle_input(self, keys, player):
        """Verarbeitet Tasteneingaben im Handelsmenü"""
        if keys[pygame.K_DOWN]:
            self.selected_index = (self.selected_index + 1) % len(self.items)
        elif keys[pygame.K_UP]:
            self.selected_index = (self.selected_index - 1) % len(self.items)
        elif keys[pygame.K_RETURN]:  # Kaufen
            item, price = self.items[self.selected_index]
            if player.coins >= price:
                player.coins -= price
                print(f"Du hast {item} gekauft!")  # Später durch UI-Dialog ersetzen
            else:
                print("Nicht genug Coins!")
        elif keys[pygame.K_ESCAPE]:  # Menü schließen
            self.toggle()
