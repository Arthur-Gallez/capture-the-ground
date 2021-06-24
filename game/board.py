import pygame as pg
def init_board(x, y, screen):
    for i in range(60):
        for j in range(50):
            if (i + j) % 2:
                pg.draw.rect(screen, (250,250,250), [i * x/60, j * y/50, i * x/60 + x/60, j * y/50 + y/50])
            else:
                pg.draw.rect(screen, (230,230,230), [i * x/60, j * y/50, i * x/60 + x/60, j * y/50 + y/50])


def actu_board(x, y, screen,grille, grille_class):
    for x_index in range(60):
        for y_index in range(50):
            if grille[y_index][x_index]==1 or grille[y_index][x_index] in ["M", "MH", "MB", "MG", "MD", "MCHG", "MCHD", "MCBG", "MCBD"]:
                 pg.draw.rect(screen, (0,0,250), [x_index * x/60, y_index * y/50, x_index * x/60 + x/60, y_index * y/50 + y/50])
            else :
                if (x + y) % 2:
                    pg.draw.rect(screen, (250,250,250), [x_index * x/60, y_index * y/50, x_index * x/60 + x/60, y_index * y/50 + y/50])
                else:
                    pg.draw.rect(screen, (230,230,230), [x_index * x/60, y_index * y/50, x_index* x/60 + x/60, y_index * y/50 + y/50])
    for i in grille_class.log:
        fumee = pg.Rect(i[0]*10,i[1]*10, 10, 10)
        pg.draw.rect(screen, (100,100,100),fumee)
