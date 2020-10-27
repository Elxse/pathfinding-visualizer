# Dijkstra's Algorithm

import pygame
from queue import PriorityQueue

import utils

def dijkstra(draw, grid, start, end):
	count = 0
	frontier = PriorityQueue()
	frontier.put((0, count, start))
	frontier_hash = {start}
	dist = {spot: float("inf") for row in grid for spot in row}
	dist[start] = 0
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
			temp_dist = dist[current] + 1
			if temp_dist < dist[neighbor]:
				dist[neighbor] = temp_dist
				came_from[neighbor] = current
			if neighbor not in explored and neighbor not in frontier_hash:
				count += 1
				frontier.put((dist[neighbor], count, neighbor))
				frontier_hash.add(neighbor)
				neighbor.make_visited()

		draw()

		if current != start:
			current.make_expanded()

	return False