import pygame, random, os
pygame.init()

pygame.display.set_caption('ColorCellBoard')

a, CELL_WIDTH, COLOR_LIST, main_list, flag=False, 39, [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)], [], True
while not a:
    size=input('Введите длину экрана в квадратах (от 1 до 20)')
    try:
        x=int(size)
        b=True
        if int(size)>0 and int(size)<21:
            a=True
        else:
            a=False
    except:
        a=False
        b=False
    try:
        y=float(size)
        c=True
    except:
        c=False
    
    if not c:
        print('Вы ввели не число')
        continue
    
    elif not b:
        print('Ваше число не является целым')
        continue

    if not a:
        print('Ваше число не в пределах от 1 до 20')
size=int(size)

screen = pygame.display.set_mode((size*(CELL_WIDTH+1)-1, size*(CELL_WIDTH+1)-1))

clock = pygame.time.Clock()
done = False

class Cell():
    def __init__(self, x, y):
        self.rect=pygame.Rect(x, y, CELL_WIDTH, CELL_WIDTH)
        self.color=0
    def draw(self):
        pygame.draw.rect(screen, COLOR_LIST[self.color%6], self.rect)

for i in range(size):
    i*=CELL_WIDTH+1
    for j in range(size):
        j*=CELL_WIDTH+1
        main_list.append(Cell(i, j))


while not done:
    clock.tick(200)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if event.type==pygame.MOUSEBUTTONDOWN and flag:
        x, y=event.pos
        for i in main_list:
            if (i.rect).collidepoint((x, y)):
                i.color+=1
                flag=False
    if event.type==pygame.MOUSEBUTTONUP and (not flag):
        flag=True
    
    for i in main_list:
        i.draw()

    pygame.display.flip()
pygame.quit()