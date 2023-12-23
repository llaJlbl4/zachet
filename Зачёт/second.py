import pygame


pygame.init()

screen_wight = 1500
screen_high = 800

display = pygame.display.set_mode((screen_wight,screen_high))

font = pygame.font.SysFont("", 100)
font2 = pygame.font.SysFont("", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    text = font.render("[1,2,3,4,5]",True, (255,0,0))
    display.blit(text,(140, 400))
    text3 = font2.render("Список - это тип данных с", True, (255, 0, 0))
    display.blit(text3, (140, 500))
    text3 = font2.render("которыми можно взаимодействовать", True, (255, 0, 0))
    display.blit(text3, (140, 550))
    text2 = font.render("(1,2,3,4,5)",True, (255,0,0))
    display.blit(text2,(520, 400))
    text3 = font2.render("Кортеж - это тип данных с", True, (255, 0, 0))
    display.blit(text3, (520, 500))
    text3 = font2.render("|которыми нельзя взаимодействовать", True, (255, 0, 0))
    display.blit(text3, (520, 550))
    text3 = font.render("{1: 21, 2: 43, 3: 54}", True, (255, 0, 0))
    display.blit(text3, (900, 400))
    text3 = font2.render("Словарь - это тип данных ", True, (255, 0, 0))
    display.blit(text3, (900, 500))
    text3 = font2.render("|которые можно вызывать, но нельзя изменить", True, (255, 0, 0))
    display.blit(text3, (900, 550))
    pygame.display.update()