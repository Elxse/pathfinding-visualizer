import pygame

import constants as cst
from spot import Spot

def make_grid(win_rows, spot_width, btn_height=0):
	grid = []
	for i in range(win_rows):
		grid.append([])
		for j in range(win_rows):
			spot = Spot(i, j, spot_width, btn_height, win_rows)
			grid[i].append(spot)
	return grid

def draw_grid(win, win_rows, win_width, line_height, btn_height=0):
	for i in range(win_rows):
		pygame.draw.line(win, cst.GREY, (0, i * line_height + btn_height), (win_width, i * line_height + btn_height))
	for j in range(win_rows):
		pygame.draw.line(win, cst.GREY, (j * line_height, btn_height), (j * line_height, win_width + btn_height))

def draw(win, grid, win_rows, sub_win_width, line_height, btn_height=0):
	win.fill(cst.WHITE)
	for row in grid:
		for spot in row:
			spot.draw(win)
	draw_grid(win, win_rows, sub_win_width, line_height, btn_height)
	pygame.display.update()

def get_clicked_pos(pos, win_rows, win_width, spot_width, btn_height=0):
	btn_lines = btn_height // spot_width
	left, top = pos
	row = top // spot_width - btn_lines
	col = left // spot_width
	return row, col

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def display_queue(Q):
	for spot in Q.queue:
		print("({0}, {1})".format(spot.row, spot.col))

def display_set(S):
	for spot in S:
		print("({0}, {1})".format(spot.row, spot.col))

def is_quit(event):
	if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
		return True
	return False