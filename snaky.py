import pygame
import sys
import random

snake_speed = 4
cell_size = 40
grid_width = 32
grid_height = 28
screen_width = cell_size * grid_width
screen_height = cell_size * grid_height

snake_directions = {
    "up": (0, -1),
    "right": (1, 0),
    "left": (-1, 0),
    "down": (0, 1)
}

class Snake():
    def __init__(self) -> None:
        self.position = [(120, 120)]
        self.length = 1
        self.direction = snake_directions["right"]
        self.color = (17, 24, 47)
        self.score = 0

    def get_head_position(self):
        return self.position[0]
    
    def change_direction(self, new_direction):
        self.direction = snake_directions[new_direction]

    def turn(self):
        if self.length > 1 and True:
            pass

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x * cell_size))%screen_width), (cur[1]+(y * cell_size))%screen_height)
        if len(self.position) > 2 and new in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0,new)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = snake_directions["up"]
        self.score = 0


    def draw_snake(self, screen):
        for index in range(0, self.position.__len__()):
            pygame.draw.rect(screen, self.color, (self.position[index][0], self.position[index][1], cell_size, cell_size))

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*cell_size, random.randint(0, grid_height-1)*cell_size)

    def draw_food(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (cell_size, cell_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


class SnakyGame():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Snaky")
        self.font = pygame.font.SysFont("monospace",16)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def drawGrid(self):
        for y in range(0, int(grid_height)):
            for x in range(0, int(grid_width)):
                if (x+y)%2 == 0:
                    r = pygame.Rect((x * cell_size, y * cell_size), ( cell_size, cell_size))
                    pygame.draw.rect(self.screen,(93,216,228), r)
                else:
                    rr = pygame.Rect((x * cell_size, y * cell_size), ( cell_size, cell_size))
                    pygame.draw.rect(self.screen, (84,194,205), rr)
    def run(self):
        while True:
            self.drawGrid()
            self.snake.move()
            self.snake.draw_snake(self.screen)
            self.food.draw_food(self.screen)

            text = self.font.render("Score {0}".format(self.snake.score), 1, (0,0,0))
            self.screen.blit(text, (5,10))

            # Eat the food
            if self.snake.get_head_position() == self.food.position:
                self.snake.length += 1
                self.snake.score += 1
                self.food.randomize_position()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction("up")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("down")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("left")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction("right")
            # Update the display
            pygame.display.flip()
            self.clock.tick(10)


if __name__ == "__main__":
    game = SnakyGame()
    game.run()