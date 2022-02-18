from pygame import *
import os



init()

size = (800, 513)

screen = display.set_mode(size)

car_surf = image.load('5fd0c11d2cf79760dd4b97ea_lWTVIV2L0DYYKXRPDKciHB4tl5eSyQtA4kQzrbUIeWLZBCG_ArR0Pt1kMy02cib_GIo71_OVxqYBjj90WhBiZbeykO3YGh6-wuRydVVwcZl__N7WxSu5tIFBU0TsrzQaY0U-Tzm-.png')
screen.blit(car_surf, (0, 0))



ARIAL_50 = font.SysFont('arial', 40)
ARIAL_30 = font.SysFont('arial', 25)

def QUIT_Window():
    quit()
    os.system('python Napomenania.py')


class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True,  (0, 0, 9)))
        self._callbacks.append(callback)

    def append_option_2(self, option, callback):
        self._option_surfaces.append(ARIAL_30.render(option, True,  (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self,direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self,surf,x,y,option_y_padding):
        for i,option in enumerate(self._option_surfaces):
            option_rect=option.get_rect()
            option_rect.topleft=(x,y+i*option_y_padding)
            if i==self._current_option_index:
                draw.rect(surf,(123, 148, 255), option_rect)
            surf.blit(option,option_rect)


menu = Menu()
menu.append_option("PLAY",QUIT_Window)
menu.append_option('Quit',quit)


running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type==KEYDOWN:
            if e.key==K_w:
                menu.switch(-1)
            elif e.key==K_s:
                menu.switch(1)
            elif e.key==K_SPACE:
                menu.select()

    screen.blit(car_surf, (0, 0))

    menu.draw(screen,10,100,75)


    display.flip()
    display.update()
quit()