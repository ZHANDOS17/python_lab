import pygame,datetime
pygame.init()
screen=pygame.display.set_mode((800,600))
bg=pygame.transform.scale(pygame.image.load('/Users/zandosmirbaj/Desktop/python/week1/python_lab-1/lab7/mickeybg.jpeg'),(800,600))
sec=pygame.transform.smoothscale(pygame.image.load('/Users/zandosmirbaj/Desktop/python/week1/python_lab-1/lab7/mickeym.png'),(800,600))
min=pygame.transform.smoothscale(pygame.image.load('/Users/zandosmirbaj/Desktop/python/week1/python_lab-1/lab7/mickeyh.png'),(800,600))
cl=pygame.time.Clock()
def r_center(s,image, angle, x, y): 
    r_image = pygame.transform.rotate(image, angle) 
    n_rect = r_image.get_rect(center=image.get_rect(center=(x, y)).center) 
    s.blit(r_image,n_rect)
run=True
while run:
    screen.blit(bg,(0,0))
    time=datetime.datetime.now()
    cl.tick(30)
    r_center(screen,sec,-time.second*6,400,300)
    r_center(screen,min,-time.minute*6-42,400,300)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update() 