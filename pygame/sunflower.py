#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pygame

pygame.init()
MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

def load_image(file, width=None, number=None):
    file = os.path.join(MAIN_DIR, 'data/image', file)
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if width == None:
        return surface
    height = surface.get_height()

    return [surface.subsurface(
        Rect((i * width, 0), (width, height))
        ) for i in xrange(number)]

class SunFlower(pygame.sprite.Sprite):
    _rate = 100
    _width = 82
    _height = 77
    _number = 18
    images = []
    def __init__(self):
        self.order = 0
        pygame.sprite.Sprite.__init__(self)
        if len(self.images) == 0:
            self.images = load_image("sunflower.png", self._width, self._number)
        self.image = self.images[self.order]
        self.rect = Rect(0, 0, self._width, self._height)
        self.life = self._life
        self.passed_time = 0

    def update(self, passed_time):
        self.passed_time += passed_time
        self.order = ( self.passed_time / self._rate ) % self._number
        if self.order == 0 and self.passed_time > self._rate:
            self.passed_time = 0
        self.image = self.images[self.order]
