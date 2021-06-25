import pygame
import random

pygame.init()

size = (600, 600)
display = pygame.display.set_mode(size)
pygame.display.set_caption("Snake ⚕")

clock = pygame.time.Clock()
done = False

snake = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [3, 2]]
food = [random.randint(1, 59), random.randint(1, 59)]

UP = [0, -1]
DOWN = [0, 1]
RIGHT = [1, 0]
LEFT = [-1, 0]
curDirection = list(RIGHT)

def snakeMovement():
	global snake

	for i in range(len(snake)-1):
		if snake[i] == snake[-1]:
			snake = snake[i+1:]
			break

	for i in range(len(snake)-1):
		snake[i] = list(snake[i+1])

	snake[-1][0] += curDirection[0]
	snake[-1][1] += curDirection[1]

	if (snake[-1][0]*10)+10 > 600:
		snake[-1][0] = -1
	elif (snake[-1][0]*10)+10 < 0:
		snake[-1][0] = (590-10)/10

	if (snake[-1][1]*10)+10 > 600:
		snake[-1][1] = -1
	elif (snake[-1][1]*10)+10 < 0:
		snake[-1][1] = (590-10)/10


def blitSnakeAndFood():
	for i in snake:
		square = pygame.Surface([10, 10])
		square.fill((255, 255, 255))
		display.blit(square, ((i[0]*10)+10, (i[1]*10)+10))

	square = pygame.Surface([10, 10])
	square.fill((255, 107, 33))
	display.blit(square, ((food[0]*10)+10, (food[1]*10)+10))

def eatFood():
	global food
	if snake[-1] == food:
		food = [random.randint(1, 59), random.randint(1, 59)]
		snake.insert(0, list(snake[0]))

def changeDirection(k):
	global curDirection

	if k == 'w' and curDirection!=DOWN:
		curDirection = list(UP)
	if k == 'a' and curDirection!=RIGHT:
		curDirection = list(LEFT)
	if k == 's' and curDirection!=UP:
		curDirection = list(DOWN)
	if k == 'd' and curDirection!=LEFT:
		curDirection = list(RIGHT)

while not done:
	display.fill(0)

	snakeMovement()
	blitSnakeAndFood()
	eatFood()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			changeDirection(event.unicode)

	pygame.display.flip()
	clock.tick(10)