import pygame


pygame.init()

screen_wight = 1500
screen_high = 800

display = pygame.display.set_mode((screen_wight,screen_high))

font = pygame.font.SysFont("", 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    text = font.render("Сысуев Дмитрий Алексеевич",True, (255,0,0))
    display.blit(text,(140, 400))
    pygame.display.update()

