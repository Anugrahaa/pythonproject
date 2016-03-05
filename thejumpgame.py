import sys, pygame
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

#load and position obstacles
obs = pygame.image.load("./images/obs.png")
obs = pygame.transform.scale(obs, (30,10))

obswidth = obs.convert().get_width()

obsrectl = obs.get_rect()
obsrectr = obs.get_rect()
obsrectl.x = 20 + wallwidth
obsrectr.x = wallrectr.x - obswidth

obsy = [10,50,100,200,250,320,390,450]


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	#color wall pixels on screen	
	screen.fill(black)
	screen.blit(wall, wallrectl)
	screen.blit(wall, wallrectr)
	i=0
	while i < len(obsy)-1:
		obsrectl.y=obsy[i]
		obsrectr.y=obsy[i+1]
		#color obs on screen
		screen.blit(obs, obsrectr)
		screen.blit(obs, obsrectl)
		i+=1
	
	#display drawn image
	pygame.display.flip()
