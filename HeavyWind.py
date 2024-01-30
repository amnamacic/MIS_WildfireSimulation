import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 600, 500
GRID_SIZE = 40
AGENT_SIZE = WIDTH // GRID_SIZE
FIRE_PROBABILITY = 0.02
HEAVY_WIND_STRENGTH = 1.5  # Adjusted for heavy wind

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
    def __init__(self, wind_strength):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Wildfire Spread Simulation - Heavy Wind")
        self.clock = pygame.time.Clock()

        # Initialize grid
        self.grid = [[Cell(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
        self.initialize_grid()

        # Initialize heavy wind
        self.wind_direction = random.uniform(0, 2 * math.pi)
        self.wind_strength = wind_strength

        # Initialize data collection
        self.fire_spread_distances = []
        self.time_to_ignition = []
        self.fire_duration = []
        self.num_trees_burned = []

        # Additional variables for data collection
        self.fire_started = False
        self.fire_start_time = 0
        self.fire_start_x, self.fire_start_y = 0, 0

    def initialize_grid(self):
        for row in self.grid:
            for cell in row:
                if random.random() < FIRE_PROBABILITY:
                    cell.set_state("fire")
                else:
                    cell.set_state("tree")

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
            self.clock.tick(10)  # Adjust the speed of the simulation

            # Check if fire has started and record starting coordinates
            if not self.fire_started and any(cell.state == "fire" for row in self.grid for cell in row):
                self.fire_start_x, self.fire_start_y = self.find_last_fire_coordinates()
                self.fire_start_time = pygame.time.get_ticks()
                self.fire_started = True

        # Collect simulation results after the simulation ends
        self.collect_simulation_results()

        pygame.quit()

    def spread_fire(self):
        new_grid = [[Cell(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = self.grid[x][y]
                new_grid[x][y] = Cell(x, y)

                if cell.state == "tree":
                    neighbors = self.get_neighbors(x, y)
                    for neighbor in neighbors:
                        if (
                            self.grid[neighbor[0]][neighbor[1]].state == "fire"
                            and random.random() < self.get_wind_effect(neighbor[0] - x, neighbor[1] - y)
                        ):
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

    def get_wind_effect(self, dx, dy):
        wind_angle = math.atan2(dy, dx)
        angle_difference = abs(self.wind_direction - wind_angle) % (2 * math.pi)
        return max(0, 1 - angle_difference / math.pi) * self.wind_strength

    def find_last_fire_coordinates(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if self.grid[x][y].state == "fire":
                    return x, y

        # If no fire found, return default coordinates
        return 0, 0

    def collect_simulation_results(self):
        # Implement data collection based on your simulation logic
        # Calculate and store metrics like fire spread distance, time to ignition, etc.

        # 1. Fire Spread Distance (example)
        last_fire_x, last_fire_y = self.find_last_fire_coordinates()
        fire_spread_distance = math.sqrt((last_fire_x - self.fire_start_x)**2 + (last_fire_y - self.fire_start_y)**2)
        self.fire_spread_distances.append(fire_spread_distance)

        # 2. Time to Ignition (example)
        time_to_ignition = self.fire_start_time
        self.time_to_ignition.append(time_to_ignition)

        # 3. Fire Duration (example)
        fire_duration = pygame.time.get_ticks() - self.fire_start_time
        self.fire_duration.append(fire_duration)

        # 4. Number of Trees Burned (example)
        num_trees_burned = sum(1 for row in self.grid for cell in row if cell.state == "empty")
        self.num_trees_burned.append(num_trees_burned)

        # Print or store these values for further use
        print(f"Fire Spread Distance: {fire_spread_distance}")
        print(f"Time to Ignition: {time_to_ignition}")
        print(f"Fire Duration: {fire_duration}")
        print(f"Number of Trees Burned: {num_trees_burned}")

if __name__ == "__main__":
    num_simulations = 4  # Change this to the number of simulations you want to run

    for _ in range(num_simulations):
        simulation = FireSimulation(HEAVY_WIND_STRENGTH)
        simulation.run_simulation()
