import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 500
GRID_SIZE = 40
AGENT_SIZE = WIDTH // GRID_SIZE
FIRE_PROBABILITY = 0.02

# Colors
FOREST_GREEN = (34, 139, 34)
FIRE_RED = (255, 0, 0)
EMPTY_GRAY = (169, 169, 169)

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "empty"

    def set_state(self, state):
        self.state = state

    def draw(self, screen):
        color = EMPTY_GRAY
        if self.state == "tree":
            color = FOREST_GREEN
        elif self.state == "fire":
            color = FIRE_RED

        pygame.draw.rect(screen, color, (self.x * AGENT_SIZE, self.y * AGENT_SIZE, AGENT_SIZE, AGENT_SIZE))

class FireSimulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Wildfire Spread Simulation")
        self.clock = pygame.time.Clock()

        # Initialize grid
        self.grid = [[Cell(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
        self.initialize_grid()

    def initialize_grid(self):
        for row in self.grid:
            for cell in row:
                if random.random() < FIRE_PROBABILITY:
                    cell.set_state("fire")
                else:
                    cell.set_state("tree")

    def spread_fire(self):
        new_grid = [[Cell(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = self.grid[x][y]
                new_grid[x][y] = Cell(x, y)

                if cell.state == "tree":
                    neighbors = self.get_neighbors(x, y)
                    for neighbor in neighbors:
                        if self.grid[neighbor[0]][neighbor[1]].state == "fire" and random.random() < 0.3:
                            new_grid[x][y].set_state("fire")
                            break
                    else:
                        new_grid[x][y].set_state("tree")

                elif cell.state == "fire":
                    new_grid[x][y].set_state("empty")

        self.grid = new_grid

    def get_neighbors(self, x, y):
        neighbors = []

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (dx != 0 or dy != 0):
                    neighbors.append((nx, ny))

        return neighbors

    def run_simulation(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.spread_fire()

            self.screen.fill(EMPTY_GRAY)
            for row in self.grid:
                for cell in row:
                    cell.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(5)  # Adjust the speed of the simulation

        pygame.quit()

if __name__ == "__main__":
    simulation = FireSimulation()
    simulation.run_simulation()
