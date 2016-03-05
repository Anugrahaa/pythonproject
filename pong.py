import sys, pygame
pygame.init()
 
size = width, height = 320, 240
speedl = 1
speedt = -1
black = 0, 0, 0
 
screen = pygame.display.set_mode(size)
 
ball = pygame.image.load("./code/pythonstuff/images/ball.png")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	if event.type == pygame.KEYDOWN:
		if pygame.key.name(event.key) == 'up':
			ballrect = ballrect.move(0,speedt)
	if ballrect.left < 0 or ballrect.right > width:
		speedl = -speedl
	if ballrect.top < 0 or ballrect.bottom > height:
		speedt = -speedt

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
