# /usr/bin/env python3
#
# A basic test that the required game libraries are installed

import pygame
import pygame_gui


pygame.init()

# Set window title and size, and get the graphics surface
pygame.display.set_caption('Smoke Test')
window_surface = pygame.display.set_mode((800, 600))

# Set up a UI manager and a button
manager = pygame_gui.UIManager((800, 600))
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((225, 275), (350, 50)),
                                             text='Everything looks good. Click to close.',
                                             manager=manager)
clock = pygame.time.Clock()
is_running = True

# Main loop
while is_running:
  # Limit to 60 FPS and get the time delta for the UI manager
  time_delta_seconds = clock.tick(60)/1000

  for event in pygame.event.get():
     # Stop looping if user closes the window or clicks the button.
     if event.type == pygame.QUIT:
         is_running = False
     elif event.type == pygame.USEREVENT:
         if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
             if event.ui_element == hello_button:
                 is_running = False

     manager.process_events(event)

  manager.update(time_delta_seconds)

  # Redraw the window every frame
  window_surface.fill(pygame.Color('#000000'))
  manager.draw_ui(window_surface)
  pygame.display.update()
