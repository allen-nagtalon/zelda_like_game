import enum
import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon

class Level:
  def __init__(self):

    # Get the Display Surface
    self.display_surface = pygame.display.get_surface()

    # Sprite Group Setup
    self.visible_sprites = YSortCameraGroup()
    self.obstacle_sprites = pygame.sprite.Group()

    # Sprite Setup
    self.create_map()

  def create_attack(self):
    Weapon(self.player, [self.visible_sprites])

  def create_map(self):
    layouts = {
      'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
      'grass': import_csv_layout('../map/map_Grass.csv'),
      'large_object': import_csv_layout('../map/map_LargeObjects.csv'),
    }
    graphics = {
      'grass': import_folder('../graphics/grass'),
      'large_objects': import_folder('../graphics/objects')
    }

    for style, layout in layouts.items():
      for r_ind, row in enumerate(layout):
        for c_ind, tile in enumerate(row):
          if tile != '-1':
            x = c_ind * TILESIZE
            y = r_ind * TILESIZE
            if style == 'boundary':
              Tile((x, y), [self.obstacle_sprites], 'invisible')
            if style == 'grass':
              random_grass_image = choice(graphics['grass'])
              Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
            if style == 'large_object':
              surf = graphics['large_objects'][int(tile)]
              Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'large_object', surf)

    self.player = Player((2000, 1500), [self.visible_sprites], self.obstacle_sprites, self.create_attack)

  def run(self):
    self.visible_sprites.custom_draw(self.player)
    self.visible_sprites.update()
    debug(self.player.status)

class YSortCameraGroup(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_width = self.display_surface.get_size()[0] // 2
    self.half_height = self.display_surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()

    self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
    self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))

  def custom_draw(self, player):
    self.offset.x = player.rect.centerx - self.half_width
    self.offset.y = player.rect.centery - self.half_height

    floor_offset_pos = self.floor_rect.topleft - self.offset
    self.display_surface.blit(self.floor_surf, floor_offset_pos)

    for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
      offset_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image, offset_pos)
