import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
  def __init__(self):

    # Get the Display Surface
    self.display_surface = pygame.display.get_surface()

    # Sprite Group Setup
    self.visible_sprites = pygame.sprite.Group()
    self.obstacle_sprites = pygame.sprite.Group()

    # Sprite Setup
    self.create_map()

  def create_map(self):
    for r_ind, row in enumerate(WORLD_MAP):
      for c_ind, tile in enumerate(row):
        x = c_ind * TILESIZE
        y = r_ind * TILESIZE

        if tile == 'x':
          Tile((x, y), [self.visible_sprites, self.obstacle_sprites])

        if tile == 'p':
          Player((x, y), [self.visible_sprites])

  def run(self):
    self.visible_sprites.draw(self.display_surface)