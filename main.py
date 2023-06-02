import pygame

# Initialisation de pygame
pygame.init()
screen = pygame.display.set_mode((673, 600))
pygame.display.set_caption("Puissance 4")
grille = pygame.image.load("grille.png")
clock = pygame.time.Clock()
running = True

# Coordonnées des cases de la grille
coordonnees = [
    [(50,529),(50,432),(50,336),(50,241),(50,146),(50,49)],        # Colonne 1
    [(145,529),(145,432),(145,336),(145,241),(145,146),(145,49)],  # Colonne 2
    [(242,529),(242,432),(242,336),(242,241),(242,146),(242,49)],  # Colonne 3
    [(338,529),(338,432),(338,336),(338,241),(338,146),(338,49)],  # Colonne 4
    [(433,529),(433,432),(433,336),(433,241),(433,146),(433,49)],  # Colonne 5
    [(530,529),(530,432),(530,336),(530,241),(530,146),(530,49)],  # Colonne 6
    [(625,529),(625,432),(625,336),(625,241),(625,146),(625,49)]   # Colonne 7
]

pions = []
ROUGE = (231, 76, 60)
JAUNE = (241, 196, 15)
play = ROUGE
game = True

# FONCTIONS

def afficher_pion(couleur, colonne, position):
    global play
    pygame.draw.circle(screen, couleur, position, 42)
    pions.append([couleur, colonne, position])

def change_couleur():
    global play
    if play == ROUGE:
        play = JAUNE
    elif play == JAUNE:
        play = ROUGE

def get_color(position):
    couleur = pygame.Surface.get_at(screen, position)
    if couleur[0] == 241 and couleur[1] == 196 and couleur[2] == 15:
        return 'JAUNE'
    elif couleur[0] == 231 and couleur[1] == 76 and couleur[2] == 60:
        return 'ROUGE'
    else:
        return 'VIDE'
    
def get_lower_position(colonne):
    for i in range(6):
        if get_color(coordonnees[colonne][i]) == 'VIDE':
            return coordonnees[colonne][i]
    return False
    
def draw_pions():
    for pion in pions:
        if(pion[2] == get_lower_position(pion[1])):
            afficher_pion(pion[0], pion[1], pion[2])

def check_win():
    # check horizontal
    for i in range(6):
        for j in range(4):
            if get_color(coordonnees[j][i]) == get_color(coordonnees[j+1][i]) == get_color(coordonnees[j+2][i]) == get_color(coordonnees[j+3][i]) != 'VIDE':
                return (True, get_color(coordonnees[j][i]))
    
    # check vertical
    for i in range(7):
        for j in range(3):
            if get_color(coordonnees[i][j]) == get_color(coordonnees[i][j+1]) == get_color(coordonnees[i][j+2]) == get_color(coordonnees[i][j+3]) != 'VIDE':
                return (True, get_color(coordonnees[i][j]))
    
    # check diagonal
    for i in range(4):
        for j in range(3):
            if get_color(coordonnees[i][j]) == get_color(coordonnees[i+1][j+1]) == get_color(coordonnees[i+2][j+2]) == get_color(coordonnees[i+3][j+3]) != 'VIDE':
                return (True, get_color(coordonnees[i][j]))
    
    #check diagonal inverse
    for i in range(4):
        for j in range(3):
            if get_color(coordonnees[i][j+3]) == get_color(coordonnees[i+1][j+2]) == get_color(coordonnees[i+2][j+1]) == get_color(coordonnees[i+3][j]) != 'VIDE':
                return (True, get_color(coordonnees[i][j +3]))
            
    draw = True
    # check match nul (tableau plein)
    for i in range(7):
        for j in range(6):
            if get_color(coordonnees[i][j]) == 'VIDE':
                draw = False
    if draw:
        return (True, 'NUL')

    return (False, 'VIDE')

# BOUCLE PRINCIPALE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game:
            if(event.key == pygame.K_1 or event.key == pygame.K_KP1):
                position = get_lower_position(0)
                if position:
                    afficher_pion(play, 0, position)
                    change_couleur()
            elif(event.key == pygame.K_2 or event.key == pygame.K_KP2):
                position = get_lower_position(1)
                if position:
                    afficher_pion(play, 1, position)
                    change_couleur()
            elif(event.key == pygame.K_3 or event.key == pygame.K_KP3):
                position = get_lower_position(2)
                if position:
                    afficher_pion(play, 2, position)
                    change_couleur()
            elif(event.key == pygame.K_4 or event.key == pygame.K_KP4):
                position = get_lower_position(3)
                if position:
                    afficher_pion(play, 3, position)
                    change_couleur()
            elif(event.key == pygame.K_5 or event.key == pygame.K_KP5):
                position = get_lower_position(4)
                if position:
                    afficher_pion(play, 4, position)
                    change_couleur() 
            elif(event.key == pygame.K_6 or event.key == pygame.K_KP6):
                position = get_lower_position(5)
                if position:
                    afficher_pion(play, 5, position)
                    change_couleur()
            elif(event.key == pygame.K_7 or event.key == pygame.K_KP7):
                position = get_lower_position(6)
                if position:
                    afficher_pion(play, 6, position)
                    change_couleur()

    screen.blit(grille, (0, 0))

    draw_pions()
    if check_win()[0]:
        if check_win()[1] == 'NUL':
            print("Match nul")
        else:
            print(f"L'équipe {check_win()[1]} a gagné")
        game = False

 

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()