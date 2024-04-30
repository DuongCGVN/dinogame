import pygame,random

maxtreeindisplay=random.randint(1,5)
pygame.init
y_dino=150
score=0
icongame=pygame.image.load(r"C:\Users\sinhg\OneDrive\Desktop\dino\assets\dinosaur.png")

pygame.display.set_icon(icongame)
screen=pygame.display.set_mode((600,300))
pygame.display.set_caption("Khủng long")

gun=pygame.image.load(r'C:\Users\sinhg\OneDrive\Desktop\dino\assets\Remove-bg.ai_1714317709220.png')
kichthuocsung=gun.get_size()
gun=pygame.transform.scale(gun,(kichthuocsung[0]//20,kichthuocsung[0]//20))


cay=pygame.image.load(r'C:\Users\sinhg\OneDrive\Desktop\dino\assets\tree.png')
cay=pygame.transform.scale2x(cay)

khunglong=pygame.image.load(r"C:\Users\sinhg\OneDrive\Desktop\dino\assets\dinosaur.png")

bg=pygame.image.load(r'C:\Users\sinhg\OneDrive\Desktop\dino\assets\background.jpg')
#bg=pygame.transform.scale2x(bg)
x_bg=0
socay=[]
runing=True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing=False
        x_bg-=1    

        randomtree=random.randint(0,10)
        if randomtree==4:
            socay.append()
            
        screen.blit(bg,(x_bg,0))    
        screen.blit(khunglong,(150,y_dino))
        screen.blit(gun,(155,y_dino))
        pygame.display.update()