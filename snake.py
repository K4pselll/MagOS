import pygame, random
pygame.init()
W= 400
screen = pygame.display.set_mode((W,W))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

snake = [(200, 200)]
direction = (20, 0)
food = (random.randrange(20,W-20,20), random.randrange(20,W-20,20))
score = 0

running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)
    
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)
    if head == food:
        score += 1
        food = (random.randrange(20,W-20,20), random.randrange(20,W-20,20))
    else:
        snake.pop()
    if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= W or head in snake[1:]:
        running = False
    screen.fill((0,0,0))
    for s in snake:
        pygame.draw.rect(screen, (0,255,0), (*s, 20, 20))
    pygame.draw.rect(screen, (255,0,0), (*food, 20, 20))
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()
