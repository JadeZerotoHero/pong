import pygame
import sys

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window for the game
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Colors
bg_color = pygame.Color('black')
text_color = pygame.Color('white')
button_color = pygame.Color('gray')
button_hover_color = pygame.Color('lightgray')

# Game Variables
menu_font = pygame.font.Font("freesansbold.ttf", 128)
option_font = pygame.font.Font("freesansbold.ttf", 62)

# Button class for the menu options
class Button:
    def __init__(self, x, y, width, height, text, font, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, button_color, self.rect)
        pygame.draw.rect(screen, text_color, self.rect, 3)

        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

# Start the game function
def start_game():
    pygame.quit()
    execfile("pong.py")

# Exit the game function
def exit_game():
    pygame.quit()
    sys.exit()

# Main Menu
def main_menu():
    start_button = Button(screen_width/2 - 150, 400, 300, 80, "Start", option_font, start_game)
    exit_button = Button(screen_width/2 - 150, 500, 300, 80, "Exit", option_font, exit_game)

    while True:
        screen.fill(bg_color)

        title_text = menu_font.render("Pong", True, text_color)
        title_rect = title_text.get_rect(center=(screen_width/2, 200))
        screen.blit(title_text, title_rect)

        start_button.draw()
        exit_button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            start_button.handle_event(event)
            exit_button.handle_event(event)

# Start the main menu
main_menu()
