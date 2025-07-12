import pygame
import time

# 버튼 클래스
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, size=(150, 50)):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.size = size
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = pygame.Surface(self.size)
            self.image.fill(self.base_color)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.hovering = False 

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.hovering = True
            return True
        else:
            self.hovering = False
            return False

    def changeColor(self):
        if self.hovering:
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

# Timer 클래스
class Timer:
    def __init__(self):
        self.start = time.perf_counter()
    def restart(self):
        self.start = time.perf_counter()
 
    def get_time(self):
        return time.perf_counter() - self.start
