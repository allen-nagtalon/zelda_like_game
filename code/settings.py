WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
MP_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
MP_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
  'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weaponds/sword/full.png'},
  'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weaponds/lance/full.png'},
  'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weaponds/axe/full.png'},
  'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weaponds/rapier/full.png'},
  'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../graphics/weaponds/sai/full.png'},
}

magic_data = {
  'flame': {'strength': 5, 'cost': 20, 'graphic': '../graphics/particles/flame/fire.png'},
  'heal': {'strength': 20, 'cost': 10, 'graphic': '../graphics/particles/heal/heal.png'}
}