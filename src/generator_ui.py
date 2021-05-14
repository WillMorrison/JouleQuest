import pygame
import pygame_gui

from rules_python.python.runfiles import runfiles


class GeneratorWindow(pygame_gui.elements.ui_window.UIWindow):
    def __init__(self, position, ui_manager, generator):
        super().__init__(pygame.Rect(position, (320, 120)), ui_manager,
                         window_display_title=generator.name,
                         object_id='#generator_window')

        self._generator = generator

        self.button = pygame_gui.elements.UIButton(pygame.Rect((64, 0), (150, 30)),
                                    'Unknown',
                                    ui_manager,
                                    container=self,
                                    object_id='#toggle_button')

        self.output_label = pygame_gui.elements.UILabel(pygame.Rect((64, 30), (160, 25)),
                                    f'Current Output: {self._generator.current_output}',
                                    ui_manager,
                                    container=self,
                                    object_id='#output_label')

        self._load_images()

        self._image = pygame_gui.elements.UIImage(pygame.Rect((0,0), (64, 64)),
                                    self._toggle_off_image,
                                    ui_manager,
                                    container=self,
                                    object_id='#toggle_image')
        

    def _load_images(self):
        r = runfiles.Create()
        with open(r.Rlocation('joule_quest/assets/images/light_switch_off_256x256.png'), 'r') as f:
            self._toggle_off_image = pygame.transform.scale(pygame.image.load(f), (64,64)).convert_alpha()
        with open(r.Rlocation('joule_quest/assets/images/light_switch_on_256x256.png'), 'r') as f:
            self._toggle_on_image = pygame.transform.scale(pygame.image.load(f), (64,64)).convert_alpha()


    def process_event(self, event):
        handled = super().process_event(event)

        if (event.type == pygame.USEREVENT and
                event.user_type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_object_id == "#generator_window.#toggle_button" and
                event.ui_element == self.button):
            handled = True
            self._generator.toggle_connection()
        return handled

    def update(self, time_delta):
        super().update(time_delta)

        self.output_label.set_text(f'Current Output: {self._generator.current_output}')
        self.output_label.update(time_delta)

        self.button.set_text('Connected' if self._generator.connected else 'Disconnected')
        self.button.update(time_delta)

        self._image.set_image(self._toggle_on_image if self._generator.connected else self._toggle_off_image)
        self._image.set_dimensions((64, 64))
        self._image.update(time_delta)
