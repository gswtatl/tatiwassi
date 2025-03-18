import pygame

pygame.init()
window = pygame.display.set_mode((320, 400))
pygame.display.set_caption('tapalka tati wassi')
clock = pygame.time.Clock()
tw = pygame.image.load(r'tatiwassi\tatiwassi.png').convert_alpha()
tw_rect = tw.get_rect()

counter = 0
font = pygame.font.Font(r'tatiwassi\font.ttf', 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if tw_rect.collidepoint(mouse_pos):
                counter += 1

    window.fill('white')
    window.blit(tw, tw_rect)
    counter_text = font.render(str(counter), True, 'black')
    window.blit(counter_text, counter_text.get_rect(center=(160, 340)))
    pygame.display.update()
    clock.tick(60)
