import constants as cst
import pygame

class Spot:
	def __init__(self, row, col, width, btn_height, total_rows):
		self.row = row
		self.col = col
		self.top = row * width + btn_height
		self.left = col * width
		self.width = width
		self.color = cst.WHITE
		self.neighbors = []
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_visited(self):
		return self.color == cst.CG_BLUE
	
	def is_expanded(self):
		return self.color == cst.VERDIGRIS

	def is_start(self):
		return self.color == cst.PEACH_PUFF

	def is_end(self):
		return self.color == cst.BITTERSWEET

	def is_barrier(self):
		return self.color == cst.BLACK

	def reset(self):
		self.color = cst.WHITE

	def make_visited(self):
		self.color = cst.CG_BLUE

	def make_expanded(self):
		self.color = cst.VERDIGRIS
	
	def make_start(self):
		self.color = cst.PEACH_PUFF

	def make_end(self):
		self.color = cst.BITTERSWEET

	def make_barrier(self):
		self.color = cst.BLACK

	def make_path(self):
		self.color = cst.LIGHT_YELLOW

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.left, self.top, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []

		# TOP
		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
			self.neighbors.append(grid[self.row - 1][self.col])

		# RIGHT
		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
			self.neighbors.append(grid[self.row][self.col + 1])

		# BOTTOM
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
			self.neighbors.append(grid[self.row + 1][self.col])

		# LEFT
		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
			self.neighbors.append(grid[self.row][self.col - 1])
	
