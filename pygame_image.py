import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

x = 0
y = 0


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        t = tmr%3200
        screen.blit(bg_img, [-t, 0])
        screen.blit(bg_img2,[-t+1600, 0])
        screen.blit(bg_img, [-t+3200, 0])
        screen.blit(bg_img2,[-t+4800, 0])
        
        clock.tick(200)
        
        
        x=0
        y=0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            y -= 1
        elif key_lst[pg.K_DOWN]:
            y += 1
        elif key_lst[pg.K_LEFT]:
            x -= 1
        elif key_lst[pg.K_RIGHT]:
            x +=2
        kk_rct.move_ip((-1+x,y))


        
        screen.blit(kk_img, kk_rct)
        pg.display.update()

        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

