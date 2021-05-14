import pygame
import pygame_gui

from src import generator_model
from src import generator_ui

class Game:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Joule Quest')
        self.window_surface = pygame.display.set_mode((800, 600))

        self.ui_manager = pygame_gui.UIManager((800, 600))

        self.model_root = generator_model.Generator()
        self.ui_root = generator_ui.GeneratorWindow((0,0), self.ui_manager, self.model_root)


    def run(self):
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
          # Limit to 10 FPS and get the time delta for the UI manager
          time_delta_seconds = clock.tick(10)/1000

          for event in pygame.event.get():
             if event.type == pygame.QUIT:
               is_running = False
             elif event.type == pygame.USEREVENT:
               pass

             self.ui_manager.process_events(event)

          self.ui_manager.update(time_delta_seconds)

          # Redraw the window every frame
          self.window_surface.fill(pygame.Color('#FFFFFF'))
          self.ui_manager.draw_ui(self.window_surface)
          pygame.display.update()
