# A* Search

import pygame
from queue import PriorityQueue

import utils

def astar(draw, grid, start, end):
	count = 0
	frontier = PriorityQueue()
	frontier.put((0, count, start))
	frontier_hash = {start}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = utils.h(start.get_pos(), end.get_pos())
	came_from = {}

	while not frontier.empty():
		for event in pygame.event.get():
			if utils.is_quit(event):
				pygame.quit()
		
		current = frontier.get()[2]
		frontier_hash.remove(current)

		if current == end:
			utils.reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + utils.h(neighbor.get_pos(), end.get_pos())
				if neighbor not in frontier_hash:
					count += 1
					frontier.put((f_score[neighbor], count, neighbor))
					frontier_hash.add(neighbor)
					neighbor.make_visited()
		
		draw()

		if current != start:
			current.make_expanded()
	
	return False