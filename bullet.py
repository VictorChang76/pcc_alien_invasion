import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""

	def __init__(self, ai_game):
		super().__init()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.bullet_color = self.settings.bullet_color

		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# update the decimal position of the bullet
		self.y -= self.settings.bullet_speed
		# set the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.bullet_color, self.rect)