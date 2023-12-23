import pygame


pygame.init()

screen_wight = 1500
screen_high = 800

display = pygame.display.set_mode((screen_wight, screen_high))

img = pygame.image.load("cat.jpg")
new_size = (1500, 800)
img = pygame.transform.scale(img, new_size)
img2 = pygame.image.load("dog.jpg")
img2 = pygame.transform.scale(img2, new_size)

font = pygame.font.SysFont("", 100)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    x = input("Выберите: <кот> или <собака>: ")
    display = pygame.display.set_mode((screen_wight, screen_high))



    if x == "кот":
        display.blit(img,(0,0))
        # img3=img2
    elif x == "собака":
        display.blit(img2, (0, 0))
        # img3 = img
    else:
        text = font.render("я же сказал кота или собаку", True,(255,0,0))
        display.blit(text,(0, 0))
    # display.blit(img, (0, 0))
    pygame.display.update()

