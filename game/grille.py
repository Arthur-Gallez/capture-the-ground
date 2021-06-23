import pygame
class Grille :
    def __init__(self) :
        x_elem = 60
        y_elem = 50
        self.grille = []
        self.player=(0,0,"X")#X == Sur un block | x == Sur Vide |XM == Sur mur de base
        for _ in range(y_elem):
            sub_grille = []
            for i in range(x_elem):
                if _ == 0 or i == 0 or i==59 or _==49:
                    sub_grille.append("M")
                else :
                    sub_grille.append(0)
            self.grille.append(sub_grille)

    def get_square(self, x_pos,y_pos):
        #return ce quil y a à la position souhaité
        #return None si le position sort du cadre de jeu
        x_index=x_pos//10
        y_index=y_pos//10
        if x_index>60 or y_index>40:
            return None
        return self.grille[y_index][x_index]

    def get_grille(self):
        return self.grille

    def modif_value(self, x_pos,y_pos,value):
        x_index=x_pos//10
        y_index=y_pos//10
        if x_index>60 or y_index>40:
            return None
        self.grille[y_index][x_index]==value


    def move_player(self, x_pos,y_pos):
        x_index=x_pos//10
        y_index=y_pos//10
        if x_index>60 or y_index>40:
            return None
        previous = self.player

        #remet le block ou etait le player avant de bouger
        if previous[2] == "X":
            self.modif_value(previous[0],previous[1],1)
        elif previous[2] == "XM":
            self.modif_value(previous[0],previous[1],"M")
        elif previous[2]=="x":
            self.modif_value(previous[0],previous[1],0)

        #modifie le block ou il va
        go_on_square = self.get_square(x_pos,y_pos)

        if go_on_square == "M":
            self.player = (x_index,y_index,"XM")
            self.modif_value(previous[0],previous[1],"XM")

        elif go_on_square == "1":
            self.player = (x_index,y_index,"X")
            self.modif_value(previous[0],previous[1],"X")

        elif go_on_square == "0":
            self.player = (x_index,y_index,"x")
            self.modif_value(previous[0],previous[1],"x")

        else :
            return "Game_Over"


















grille_class = Grille()
print(grille_class.get_grille())


