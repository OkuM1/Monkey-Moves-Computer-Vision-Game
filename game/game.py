import pygame
import mediapipe as mp
import cv2
import random
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Murat's Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

# Initialize the camera capture object
desired_width = 1280
desired_height = 720

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)  # Set desired width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)  # Set desired height

# Game states
START_SCREEN = 0
GAME_RUNNING = 1
END_SCREEN = 2

# Initialize game state
game_state = START_SCREEN

# Level
level = 1
timer = 0

cx, cy = 0, 0  # Initialize cx and cy outside the loop

# Score
score = 0
font = pygame.font.Font(None, 36)

# Fonts
font_large = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

# Texts
start_text = font_large.render("Monkey Moves", True, WHITE)
start_subtext = font_small.render("Press SPACE to start", True, WHITE)
end_text = font_large.render("Ooops, Monkey die", True, WHITE)
end_subtext = font_small.render("Try again? Press Space", True, WHITE)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('images', 'player.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize the image
        self.rect = self.image.get_rect()
        self.target_pos = (screen_width // 2, screen_height - 50)  # Initial position
        self.rect.center = self.target_pos
        self.speed = 15  # Adjust the speed as needed
        self.interpolation_factor = 0.2  # Adjust the interpolation factor for smoother movement

    def update(self, x, y):
        # Update the target position
        self.target_pos = (x, y)
        # Calculate the distance to move towards the target
        dx = self.target_pos[0] - self.rect.x
        dy = self.target_pos[1] - self.rect.y
        # Interpolate the movement
        self.rect.x += dx * self.interpolation_factor
        self.rect.y += dy * self.interpolation_factor

# Hand position indicator class
class HandIndicator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Create a simple square image
        # Draw a red circle on the surface
        pygame.draw.circle(self.image, RED, (10, 10), 10)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update_position(self, x, y):
        # Update the position of the indicator
        self.rect.center = (x, y)

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('images', 'banana.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8  # Adjust the speed as needed

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > screen_height:
            self.kill()

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(os.path.join('images', 'obstacle.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 100))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8  # Adjust the speed as needed

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > screen_height:
            self.kill()

# Background class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

# StartScreen class
class StartScreen(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
collectibles_group = pygame.sprite.Group()

# Load background image
background = Background(os.path.join('images', 'background.png'))
all_sprites.add(background)

# Load start screen image
start_screen = StartScreen(os.path.join('images', 'start_screen.png'))
all_sprites.add(start_screen)

# Create player sprite
player = Player()
all_sprites.add(player)

# Create hand indicator sprite
hand_indicator = HandIndicator()
all_sprites.add(hand_indicator)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if game_state == START_SCREEN or game_state == END_SCREEN:
                    game_state = GAME_RUNNING
                    player.rect.center = (screen_width // 2, screen_height - 50)
                    # Clear the sprites
                    all_sprites.empty()
                    obstacles_group.empty()
                    collectibles_group.empty()
                    # Add the background, player, and hand indicator back to sprites
                    all_sprites.add(background, player, hand_indicator)
                    score = 0
                elif game_state == GAME_RUNNING:
                    game_state = END_SCREEN

    if game_state == GAME_RUNNING:
        timer += 1

        speed_increment = (score // 10) * 3  # Adjust the increment based on the score
        # Spawn obstacles
        if random.randint(0, 100) < 5:
            x = random.randint(0, screen_width - 50)
            y = -50
            # Check if the newly generated position overlaps with existing obstacles
            while any(obstacle.rect.colliderect(pygame.Rect(x, y, 50, 50)) for obstacle in obstacles_group):
                x = random.randint(0, screen_width - 50)
                y = -50
            obstacle = Obstacle(x, y)
            obstacle.speed += speed_increment
            obstacles_group.add(obstacle)
            all_sprites.add(obstacle)

        # Move obstacles
        for obstacle in obstacles_group:
            obstacle.update()
            if obstacle.rect.y > screen_height:
                obstacle.kill()
                score += 1

            # Collision detection
            if pygame.sprite.spritecollide(player, obstacles_group, False):
                game_state = END_SCREEN

        # Spawn collectibles (bananas) less frequently
        if random.randint(0, 100) < 2:
            x = random.randint(0, screen_width - 50)
            y = -50
            # Check if the newly generated position overlaps with existing collectibles
            while any(collectible.rect.colliderect(pygame.Rect(x, y, 50, 50)) for collectible in collectibles_group):
                x = random.randint(0, screen_width - 50)
                y = -50
            collectible = Collectible(x, y)
            collectible.speed += speed_increment
            collectibles_group.add(collectible)
            all_sprites.add(collectible)

        # Move collectibles
        for collectible in collectibles_group:
            collectible.update()
            if collectible.rect.y > screen_height:
                collectible.kill()

            # Collision detection
            if pygame.sprite.spritecollide(player, collectibles_group, True):
                score += 5
        
        # Capture video from camera
        _, frame = cap.read()
        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(frame)

        # Move the player based on hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for idx, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand_indicator.update_position(cx, cy)
                    break

        # Draw the frame on the Pygame screen
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))

        # Update the player position towards the hand indicator
        player.update(cx, cy)

    # Draw everything on the screen
    screen.fill(BLACK)

    if game_state == START_SCREEN:
        all_sprites.draw(screen)
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 200))
        screen.blit(start_subtext, (screen_width // 2 - start_subtext.get_width() // 2, 300))
    elif game_state == GAME_RUNNING or game_state == END_SCREEN:
        all_sprites.draw(screen)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

    if game_state == END_SCREEN:
        screen.blit(end_text, (screen_width // 2 - end_text.get_width() // 2, 200))
        screen.blit(end_subtext, (screen_width // 2 - end_subtext.get_width() // 2, 300))
        score_text = font.render("Final Score: " + str(score), True, WHITE)
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 400))
        all_sprites.empty()
        obstacles_group.empty()

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Release the camera and close Pygame
cap.release()
pygame.quit()
