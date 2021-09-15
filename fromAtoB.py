import pygame
import random

pygame.init()

display_object = pygame.display.Info()
width, height = display_object.current_w * .75, display_object.current_h * .75
surface = pygame.display.set_mode((int(width), int(height)))
surface_x, surface_y = surface.get_width(), surface.get_height()

clock = pygame.time.Clock()
fps = 60


class Point:
    def __init__(self):
        self.origin = [random.randint(10, surface_x - 10), random.randint(10, surface_y - 10)]
        self.current = self.origin
        self.destination = [random.randint(10, surface_x - 10), random.randint(10, surface_y - 10)]
        self.x_speed = None
        self.y_speed = None
        self.trail = []
        self.speed = 10

    def draw_point(self):
        pygame.draw.circle(surface, (255, 255, 255), self.current, 3)

    def move_point(self):
        distance = ((self.current[0] - self.destination[0]) ** 2 + (self.current[-1] - self.destination[-1]) ** 2) ** .5

        self.x_speed = (abs(self.current[0] - self.destination[0]) / distance) * [1, -1][
            self.current[0] - self.destination[0] > 0]
        self.y_speed = (abs(self.current[-1] - self.destination[-1]) / distance) * [1, -1][
            self.current[-1] - self.destination[-1] > 0]

        self.trail.append(self.current)

        self.current[0] += self.x_speed * self.speed
        self.current[-1] += self.y_speed * self.speed

        if distance < 25:
            self.destination = [random.randint(10, surface_x - 10), random.randint(10, surface_y - 10)]
            self.current = [200, 200]
            self.trail = []

    def draw_trail(self):
        pygame.draw.line(surface, (255, 255, 255), (200, 200), self.current)

points = [Point() for point in range(50)]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    clock.tick(fps)
    surface.fill((0, 0, 0))

    for point in points:
        point.move_point()
        # point.draw_point()
        point.draw_trail()

    pygame.display.update()
