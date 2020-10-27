# Depth-first search

import pygame
from queue import LifoQueue

import utils

def depth_first(draw, grid, start, end):
	frontier = LifoQueue()
	frontier.put(start)
	frontier_hash = {start}
	explored = set()
	came_from = {}

	while not frontier.empty():
		for event in pygame.event.get():
			if utils.is_quit(event):
				pygame.quit()

		current = frontier.get()
		frontier_hash.remove(current)
		explored.add(current)

		if current == end:
			utils.reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True

		for neighbor in current.neighbors:
			if neighbor not in frontier_hash and neighbor not in explored:
				came_from[neighbor] = current
				frontier.put(neighbor)
				frontier_hash.add(neighbor)
				neighbor.make_visited()
		
		draw()

		if current != start:
			current.make_expanded()

	return False