import pygame, random

pygame.init()
fps = pygame.time.Clock() #frame per second

screen_width = 1280
screen_height = 720

#make things
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 10, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(0, screen_height / 2 - 70, 10, 140)

#draw things
light_grey = (200, 200, 200)
line_color = pygame.Color(191, 191, 191)
bg_color = pygame.Color(71, 71, 71)
alice_blue = (196,221,254)
pink = (254,216,247)

ball_speed_x = 8
ball_speed_y = 8
opponent_speed_y = 8

player_speed = 0
opponent_speed = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PongGame")

def ball_restart():
    global ball_speed_y,ball_speed_x
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 5
            if event.key == pygame.K_w:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 5
            if event.key == pygame.K_w:
                player_speed += 5
    player.y += player_speed
    
    if player.top < 0:
        player.top = 0
    if player.bottom > screen_height:
        player.bottom = screen_height

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    opponent.y += opponent_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
        
    if opponent.top <= 0 or opponent.bottom >= screen_height:
        opponent_speed_y *= -1
    
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1
    
    screen.fill(bg_color)
    pygame.draw.rect(screen, alice_blue, player)
    pygame.draw.rect(screen, pink, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.line(screen, line_color, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip()
    fps.tick(60)