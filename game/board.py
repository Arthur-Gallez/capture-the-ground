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



def render_zone(grille_class):
    if len(grille_class.log) != 0:
        print("victoire 1")
        direction_log = []
        for i in range(len(grille_class.log)-1):
            if grille_class.log[i][2] != grille_class.log[i+1][2]:
                direction_log.append(grille_class.log[i][2])
        direction_log.append(grille_class.log[-1][2])
        print(direction_log)
        co_log = []
        for j in grille_class.log:
            co_log.append([j[0],j[1]])
        if direction_log[0] != direction_log[-1]:
            print("victoire 2")
            for y in range(50):
                found = False
                for x in range(60):
                    if [x,y] in co_log:
                        found = True
                        break
                if not found:
                    for x in range(60):
                        if grille_class.get_square(x*10,y*10) == 0:
                            grille_class.modif_value(x*10,y*10,"M")
                            print(grille_class.get_square(x*10,y*10))
                else:
                    if direction_log[0] == "right":
                        if [2,y] in co_log:
                            for x in range(60):
                                if grille_class.get_square(x*10,y*10) == 0:
                                    grille_class.modif_value(x*10,y*10,"M")
                                    print(grille_class.get_square(x*10,y*10))
                        else:
                            ffound = False
                            x_aux = 1
                            while not ffound:
                                if [x_aux,y] in co_log:
                                    ffound = True
                                x_aux +=1
                            for p in range(x_aux, 60):
                                if grille_class.get_square(p*10,y*10) == 0:
                                    grille_class.modif_value(p*10,y*10,"M")
                                    print(grille_class.get_square(p*10,y*10))
    else:
        return