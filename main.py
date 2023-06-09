import pygame
import button

# Initialisation de pygame
pygame.init()
WIDTH = 673
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puissance 4 - Tour au Rouge")
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
pause = False

resume_button = button.Button(WIDTH // 2 - 60, 150, pygame.image.load("assets/button_resume.png").convert_alpha(), 1.5)
options_button = button.Button(WIDTH // 2 - 60, 230, pygame.image.load("assets/button_options.png").convert_alpha(), 1.5)
quit_button = button.Button(WIDTH // 2 - 60, 310, pygame.image.load("assets/button_quit.png").convert_alpha(), 1.5)
options_menu = "main"

# FONCTIONS

def afficher_pion(couleur, colonne, position):
    global play
    pygame.draw.circle(screen, couleur, position, 42)
    pions.append([couleur, colonne, position])

def change_couleur():
    global play
    if play == ROUGE:
        play = JAUNE
        pygame.display.set_caption('Puissance 4 - Tour au Jaune')
    elif play == JAUNE:
        play = ROUGE
        pygame.display.set_caption('Puissance 4 - Tour au Rouge')

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
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_ESCAPE) and game:
                game = False
                pause = True
                pygame.display.set_caption('Puissance 4 - Pause')

            elif(event.key == pygame.K_ESCAPE) and not game:
                game = True
                pause = False
                if play == ROUGE:
                    pygame.display.set_caption('Puissance 4 - Tour au Rouge')
                elif play == JAUNE:
                    pygame.display.set_caption('Puissance 4 - Tour au Jaune')
            elif(event.key == pygame.K_r):
                pions = []
                play = ROUGE
                game = True
                pygame.display.set_caption('Puissance 4 - Tour au Rouge')
        if event.type == pygame.KEYDOWN and game:
            colonne = -1
            position = False
            if(event.key == pygame.K_1 or event.key == pygame.K_KP1):
                colonne = 0
                position = get_lower_position(colonne)
            elif(event.key == pygame.K_2 or event.key == pygame.K_KP2):
                colonne = 1
                position = get_lower_position(colonne)
            elif(event.key == pygame.K_3 or event.key == pygame.K_KP3):
                colonne = 2
                position = get_lower_position(colonne)
            elif(event.key == pygame.K_4 or event.key == pygame.K_KP4):
                colonne = 3
                position = get_lower_position(colonne)
            elif(event.key == pygame.K_5 or event.key == pygame.K_KP5):
                colonne = 4
                position = get_lower_position(colonne)
            elif(event.key == pygame.K_6 or event.key == pygame.K_KP6):
                colonne = 5
                position = get_lower_position(colonne)
            elif(event.key == pygame.K_7 or event.key == pygame.K_KP7):
                colonne = 6
                position = get_lower_position(colonne)

            if position and colonne != -1:
                afficher_pion(play, colonne, position)
                change_couleur()
        if event.type == pygame.MOUSEBUTTONUP and game:
            posX = pygame.mouse.get_pos()[0]
            colonne = -1
            position = False
            if posX > 4 and posX <= 95:
                colonne = 0
                position = get_lower_position(colonne)
            elif posX > 95 and posX <= 192:
                colonne = 1
                position = get_lower_position(colonne)
            elif posX > 192 and posX <= 288:
                colonne = 2
                position = get_lower_position(colonne)
            elif posX > 288 and posX <= 384:
                colonne = 3
                position = get_lower_position(colonne)
            elif posX > 384 and posX <= 480:
                colonne = 4
                position = get_lower_position(colonne)
            elif posX > 480 and posX <= 576:
                colonne = 5
                position = get_lower_position(colonne)
            elif posX > 576 and posX <= 672:
                colonne = 6
                position = get_lower_position(colonne)
            if position and colonne != -1:
                afficher_pion(play, colonne, position)
                change_couleur()

    screen.blit(grille, (0, 0))

    if pause:
        borders_scale = 3
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 80 - 2 *borders_scale, 130 - borders_scale, 190 + 2*borders_scale, 260 + 2*borders_scale))
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 80 - borders_scale, 130, 190, 260))
        if quit_button.draw(screen):
            running = False
        if options_button.draw(screen):
            print("Options")

        if resume_button.draw(screen):
            pause = False
            game = True
            if play == ROUGE:
                pygame.display.set_caption('Puissance 4 - Tour au Rouge')
            elif play == JAUNE:
                pygame.display.set_caption('Puissance 4 - Tour au Jaune')

    draw_pions()
    if check_win()[0]:
        if check_win()[1] == 'NUL':
            print("Match nul")
            pygame.display.set_caption('Match nul')
        else:
            print(f"L'équipe {check_win()[1]} a gagné")
            pygame.display.set_caption(f"Victoire de l'équipe {check_win()[1]}")
        game = False

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()