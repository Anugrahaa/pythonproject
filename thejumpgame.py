import sys, pygame
import random
import time

pygame.init()
 
size = width, height = 640, 480
black = 0, 0, 0
 
#draw screen 
screen = pygame.display.set_mode(size)
 
#load and position wall 
wall = pygame.image.load("./images/wall.jpg")
wall = pygame.transform.scale(wall, (50,480))

wallrectl = wall.get_rect()
wallrectl.x = 20
wallrectl.y = 0

wallwidth = wall.convert().get_width()

wallrectr = wall.get_rect()
wallrectr.x = 620 - wallwidth
wallrectr.y = 0

#load and position ninja
ninja = pygame.image.load("./images/Ninja.png")
ninja = pygame.transform.scale(ninja, (30,30))

ninrect = ninja.get_rect()
ninrect.x = 20 + wallwidth
ninrect.y = height - 60

#load and position obstacles
obs = pygame.image.load("./images/obs.png")
obs = pygame.transform.scale(obs, (30,10))

obswidth = obs.convert().get_width()

obsrectl = obs.get_rect()
obsrectr = obs.get_rect()
obsrectl.x = 20 + wallwidth
obsrectr.x = wallrectr.x - obswidth

obsyl = [5.0,0.0,0.0,0.0,0.0,0.0]
obsyr = [20.0,0.0,0.0,0.0,0.0,0.0]
trackl = [1,0,0,0,0,0]
trackr = [1,0,0,0,0,0]

obsrectl.y = 5
obsrectr.y = 20

speedl = 0.1
speedr = 0.2
prevl = 0
prevr = 0

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	#color wall pixels on screen	
	screen.fill(black)
	screen.blit(wall, wallrectl)
	screen.blit(wall, wallrectr)
	i=0
	countl = 0
	countr = 0
	while i < len(obsyl)-1:
		if trackl[i] == 0 and countl == 0 and obsyl[prevl] > random.randint(200,250) :
			obsyl[i] = 5
			obsrectl.y = obsyl[i]		
			trackl[i] = 1
			prevl = i
			screen.blit(obs, obsrectl)
			countl = 1
                if trackr[i] == 0 and countr == 0 and obsyr[prevr] > random.randint(150,200):
			obsyr[i] = 20
			obsrectr.y = obsyr[i]
			trackr[i] = 1
			prevr = i
			screen.blit(obs, obsrectr)
			countr = 1
		if trackl[i] == 1:
			obsrectl.y = obsyl[i] + speedl
			obsyl[i] = obsyl[i] + speedl
			screen.blit(obs, obsrectl)
			if obsrectl.y > height:
				obsyl[i] = 0
				trackl[i] = 0
		if trackr[i] == 1:
			obsrectr.y = obsyr[i] + speedr
			obsyr[i] = obsyr[i] + speedr
			screen.blit(obs, obsrectr)
			if obsrectr.y > height:
				obsyr[i] = 0
				trackr[i] = 0		
                i+=1
	if event.type == pygame.KEYDOWN:
		if pygame.key.name(event.key) == 'right':
			ninrect.x = 620 - wallwidth - 30
		if pygame.key.name(event.key) == 'left':
			ninrect.x = 20 + wallwidth
	screen.blit(ninja,ninrect)

	#display drawn image
	pygame.display.flip()
