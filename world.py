import pygame

class World():
	def __init__(self, data, tile_size):
		self.tile_list = []

		#load images
		grass_tile = pygame.image.load('images/grass_tile.png') #1
		dirt_tile = pygame.image.load('images/dirt_tile.png') #2
		stone_tile = pygame.image.load('images/stone_tile.png') #3
		teleporation_box = pygame.image.load('images/teleportation_box.png') #3

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(grass_tile, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(dirt_tile, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					img = pygame.transform.scale(stone_tile, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 4:
					img = pygame.transform.scale(teleporation_box, (tile_size, tile_size*2))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)	
				col_count += 1
			row_count += 1

	def draw(self, screen):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
