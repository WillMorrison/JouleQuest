import pygame
import pygame_gui

pygame.init()

# Set window title and size, and get the graphics surface
pygame.display.set_caption('Smoke Test')
window_surface = pygame.display.set_mode((800, 600))

# Set up a UI manager
manager = pygame_gui.UIManager((800, 600))

clock = pygame.time.Clock()
is_running = True

# Main loop
while is_running:
  # Limit to 10 FPS and get the time delta for the UI manager
  time_delta_seconds = clock.tick(10)/1000

  for event in pygame.event.get():
     if event.type == pygame.QUIT:
       is_running = False
     elif event.type == pygame.USEREVENT:
       pass

     manager.process_events(event)

  manager.update(time_delta_seconds)

  # Redraw the window every frame
  window_surface.fill(pygame.Color('#FFFFFF'))
  manager.draw_ui(window_surface)
  pygame.display.update()
