import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52
PIPE_HEIGHT = 320
PIPE_GAP = 150
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
FPS = 20
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flying Bird Game")

# Load images
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill(BLUE)

# Function to create pipes
def create_pipe():
    height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
    return (SCREEN_WIDTH, height)
 
def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, PIPE_WIDTH, pipe[1]))  # Top pipe
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))  # Bottom pipe

# Main game function
def main():   
    clock = pygame.time.Clock()
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    gravity = 1
    pipes = [create_pipe()]
    score = 0
    pipe_speed = -4

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -10  # Make the bird jump

        # Update bird position
        bird_velocity += gravity
        bird_y += bird_velocity

        # Move pipes
        for i in range(len(pipes)):
            pipes[i] = (pipes[i][0] + pipe_speed, pipes[i][1])
        
        # Add new pipes
        if pipes[-1][0] < SCREEN_WIDTH - 200:  # Spawn a new pipe every 200 pixels
            pipes.append(create_pipe())
        
        # Remove off-screen pipes
        if pipes[0][0] < -PIPE_WIDTH:
            pipes.pop(0)
            score += 1  # Increment score for passing a pipe

        # Check for collisions
        if bird_y < 0 or bird_y > SCREEN_HEIGHT:
            print("Game Over! Your score:", score)
            pygame.quit()
            sys.exit()
        
        for pipe in pipes:
            if (pipe[0] < BIRD_WIDTH and pipe[0] + PIPE_WIDTH > 0 and
                (bird_y < pipe[1] or bird_y + BIRD_HEIGHT > pipe[1] + PIPE_GAP)):
                print("Game Over! Your score:", score)
                pygame.quit()
                sys.exit()

        # Clear screen
        screen.fill(WHITE)

        # Draw everything
        screen.blit(bird_image, (50, bird_y))
        draw_pipes(pipes)

        # Display score
        font = pygame.font.SysFont("Arial", 25)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Refresh the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
