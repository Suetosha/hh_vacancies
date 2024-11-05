import pygame


class Music:
    def __init__(self, path):
        self.path = path

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()

    @staticmethod
    def stop():
        pygame.mixer.music.stop()
