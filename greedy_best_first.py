# Greedy Best-first Search

import pygame
from queue import PriorityQueue

import utils

def greedy_best_first(draw, grid, start, end):
	f_score = {start: utils.h(start.get_pos(), end.get_pos())}

	count = 0
	frontier = PriorityQueue()
	frontier.put((f_score[start], count, start))
	frontier_hash = {start}
	explored = set()
	came_from = {}

	while not frontier.empty():
		
		for event in pygame.event.get():
			if(utils.is_quit(event)):
				pygame.quit()

		current = frontier.get()[2]
		frontier_hash.remove(current)
		explored.add(current)

		if current == end:
			utils.reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True

		for neighbor in current.neighbors:
			f_score[neighbor] = utils.h(neighbor.get_pos(), end.get_pos())
			if f_score[neighbor] < f_score[current] and neighbor not in frontier_hash and neighbor not in explored:
				count += 1
				came_from[neighbor] = current
				frontier.put((f_score[neighbor], count, neighbor))
				frontier_hash.add(neighbor)
				neighbor.make_visited()

		draw()

		if current != start:
			current.make_expanded()

	return False