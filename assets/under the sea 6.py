


#effetti sonori diversi del level up 






import pygame 
import random
import sys
import os

# Inizializza Pygame
pygame.init()

# Costanti generali
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Percorsi file
ASSETS_DIR = os.path.join(os.getcwd(), "assets")
HIGHSCORE_FILE = os.path.join(os.getcwd(), "highscores.txt")

# Inizializza la finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evita i Nemici Ultra-Avanzato")
clock = pygame.time.Clock()

# Suoni
pygame.mixer.init()
collision_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "drowning.wav"))
powerup_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "power up_drip.wav"))
pygame.mixer.music.set_volume(1.0)  
level_up_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "level_up_3.mp3"))

# Font
font_large = pygame.font.Font(None, 72)
font_small = pygame.font.Font(None, 36)

# Classe Giocatore
class Player:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(ASSETS_DIR, "player.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 10

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# Classe Nemico
class Enemy:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(ASSETS_DIR, "enemy.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(-100, -40)))
        self.speed = random.randint(1, 3)  # Ridotto il range da 3-6 a 1-3


    def move(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(50, WIDTH - 50)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# Classe Power-Up
class PowerUp:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(ASSETS_DIR, "powerup.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
        self.type = random.choice(["speed", "points"])

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# Classe Boss
class Boss:
    def __init__(self, level):
        self.image = pygame.image.load(os.path.join(ASSETS_DIR, "boss.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH // 2, -100))
        self.speed = level
        self.health = level * 5

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = -100

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def take_damage(self):
        self.health -= 1

# Classe Gioco principale
class AvoidEnemiesGame:
    def __init__(self): 
        self.player = Player()
        self.enemies = [Enemy() for _ in range(3)]
        self.power_ups = []
        self.boss = None

        self.score = 0
        self.level = 1
        self.running = True
        self.highscores = self.load_highscores()

        # Carica l'immagine dello sfondo
        self.background = pygame.image.load(os.path.join(ASSETS_DIR, "background.gif")).convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        # Musica di sottofondo
        pygame.mixer.music.load(os.path.join(ASSETS_DIR, "background_music.wav"))
        pygame.mixer.music.set_volume(0.1)  # Imposta il volume (da 0.0 a 1.0)
        pygame.mixer.music.play(-1)  # Riproduce la musica in loop infinito

    def load_highscores(self):
        if not os.path.exists(HIGHSCORE_FILE):
            return [0] * 5
        with open(HIGHSCORE_FILE, "r") as f:
            return [int(line.strip()) for line in f.readlines()]

    def save_highscores(self):
        with open(HIGHSCORE_FILE, "w") as f:
            for score in self.highscores:
                f.write(f"{score}\n")

    def update_highscores(self):
        self.highscores.append(self.score)
        self.highscores = sorted(self.highscores, reverse=True)[:5]
        self.save_highscores()

    def check_collisions(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                collision_sound.play()
                self.running = False

        for power_up in self.power_ups:
            if self.player.rect.colliderect(power_up.rect):
                powerup_sound.play()
                if power_up.type == "speed":
                    self.player.speed += 2
                elif power_up.type == "points":
                    self.score += 100
                self.power_ups.remove(power_up)

        if self.boss and self.player.rect.colliderect(self.boss.rect):
            collision_sound.play()
            self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        for enemy in self.enemies:
            enemy.move()

        if self.boss:
            self.boss.move()

        self.check_collisions()

        self.score += 1

        if self.score % 500 == 0:  # Ridotto il punteggio per far apparire il boss più frequentemente
            level_up_sound.play()
            self.level += 1
            self.enemies.append(Enemy())
            if self.level % 2 == 0:  # Modifica: Boss appare ogni 2 livelli
                self.boss = Boss(self.level)

        if random.randint(1, 200) == 1:
            self.power_ups.append(PowerUp())

    def draw(self):
        # Disegna lo sfondo
        screen.blit(self.background, (0, 0))

        # Disegna il giocatore
        self.player.draw(screen)

        # Disegna i nemici
        for enemy in self.enemies:
            enemy.draw(screen)

        # Disegna i power-up
        for power_up in self.power_ups:
            power_up.draw(screen)

        # Disegna il boss
        if self.boss:
            self.boss.draw(screen)

        # Mostra il punteggio e il livello
        score_text = font_small.render(f"Punteggio: {self.score}", True, BLACK)
        level_text = font_small.render(f"Livello: {self.level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
    def game_over(self):
        self.update_highscores()
        # Disegna lo sfondo
        screen.blit(self.background, (0, 0))
        
        # Testo "Game Over"
        game_over_text = font_large.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

        # Mostra punteggio
        score_text = font_small.render(f"Punteggio: {self.score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))

        # Mostra la classifica
        highscore_text = font_small.render("Classifica:", True, WHITE)
        screen.blit(highscore_text, (WIDTH // 2 - 100, HEIGHT // 2 + 100))

        for i, score in enumerate(self.highscores):
            score_entry = font_small.render(f"{i + 1}. {score}", True, WHITE)
            screen.blit(score_entry, (WIDTH // 2 - 100, HEIGHT // 2 + 140 + i * 30))

        # Aggiorna lo schermo
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

    def run(self):
        while self.running:
            # Gestisci gli eventi
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Aggiorna lo stato del gioco
            self.update()

            # Disegna tutto sullo schermo
            self.draw()

            # Aggiorna lo schermo
            pygame.display.flip()

            # Imposta il framerate
            clock.tick(FPS)

        # Game over
        self.game_over()

# Avvia il gioco
if __name__ == "__main__":
    game = AvoidEnemiesGame()
    game.run()

