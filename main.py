import pygame
import pygame_gui
import math

import utils
from dijkstra import dijkstra
from astar import astar
from greedy_best_first import greedy_best_first
from depth_first import depth_first
from breadth_first import breadth_first

def pathfinder(algorithm, name, win, win_rows, win_width, line_height):
	pygame.display.set_caption(name)
	grid = utils.make_grid(win_rows, line_height)

	start = None
	end = None

	run = True
	started = False
	while run:
		utils.draw(win, grid, win_rows, win_width, line_height=line_height)
		for event in pygame.event.get():
			if utils.is_quit(event):
				run = False

			if started:
				continue
			
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = utils.get_clicked_pos(pos, win_rows, win_width, line_height)
				if row >= 0 and col >= 0:
					spot = grid[row][col]
					if not start and spot != end:
						start = spot
						start.make_start()
					elif not end and spot != start:
						end = spot
						end.make_end()
					elif spot != end and spot != start:
						spot.make_barrier()
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = utils.get_clicked_pos(pos, win_rows, win_width, line_height)
				if row >= 0 and col >= 0:
					spot = grid[row][col]
					spot.reset()
					if spot == start:
						start = None
					elif spot == end:
						end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					algorithm(lambda: utils.draw(win, grid, win_rows, win_width, line_height), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = utils.make_grid(win_rows, line_height)


WIN_WIDTH = 1000
ROWS = 40
BTN_HEIGHT = 60
LINE_HEIGHT = WIN_WIDTH // ROWS

pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
pygame.display.set_caption("Path Finding Visualizer")

background = pygame.Surface((WIN_WIDTH, WIN_WIDTH))
background.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((WIN_WIDTH, WIN_WIDTH))

dijkstra_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 5), (200, 50)),
											text="Dijkstra's Algorithm",
											manager=manager)
astar_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((210, 5), (120, 50)),
											text="A* Search",
											manager=manager)
greedy_best_first_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((335, 5), (230, 50)),
											text="Greedy Best-first Search",
											manager=manager)
breadth_first_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((570, 5), (210, 50)),
											text="Breadth-first Search",
											manager=manager)
depth_first_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((785, 5), (205, 50)),
											text="Depth-first Search",
											manager=manager)
clock = pygame.time.Clock()
is_running = True

while is_running:
	time_delta = clock.tick(60)/1000.0
	for event in pygame.event.get():
		if utils.is_quit(event):
			is_running = False
		if event.type == pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				if event.ui_element == dijkstra_btn:
					pathfinder(dijkstra, "Dijkstra's Algorithm", WIN, ROWS, WIN_WIDTH, LINE_HEIGHT)
				if event.ui_element == astar_btn:
					pathfinder(astar, "A* Search", WIN, ROWS, WIN_WIDTH, LINE_HEIGHT)
				if event.ui_element == greedy_best_first_btn:
					pathfinder(greedy_best_first, "Greedy Best-first Search", WIN, ROWS, WIN_WIDTH, LINE_HEIGHT)
				if event.ui_element == breadth_first_btn:
					pathfinder(breadth_first, "Breadth-first Search", WIN, ROWS, WIN_WIDTH, LINE_HEIGHT)
				if event.ui_element == depth_first_btn:
					pathfinder(depth_first, "Depth-first Search", WIN, ROWS, WIN_WIDTH, LINE_HEIGHT)
		pygame.display.set_caption("Path Finding Visualizer")
		manager.process_events(event)

	manager.update(time_delta)

	WIN.blit(background, (0, 0))
	manager.draw_ui(WIN)
	utils.draw_grid(WIN, ROWS, WIN_WIDTH, line_height=LINE_HEIGHT, btn_height=BTN_HEIGHT)
	pygame.display.update()

pygame.quit()