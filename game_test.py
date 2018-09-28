import pygame
import sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import random

pygame.init()
clock = pygame.time.Clock()

blob = pygame.image.load('images/mark-noble.png')

windowwidth = 500
windowheight = 400
rectX = 10.0
rectY = 10.0
rectendX = 275.0
rectendY = 10.0
rectXmv = 1
rectYmv = 1
rectcolor = [23,245,224]
start = 1
elX = 25
elY = 12.5
OX = 375
OY = 275
OendX = 125
OendY = 125
elendX  = 125
elendY = 125
movement = 0.25
gr = 150.0
#set up the window for the game to be played in, double brackets on the sizing
window = pygame.display.set_mode( (windowwidth, windowheight) )
window.fill((234,33,33))
Omovement = 0.5
Ospeed = 5
Odirection = -1

# Square Variables
playerSize = 20
playerX = (windowwidth / 2) - (playerSize / 2)
playerY = windowheight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 50.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False

def move():

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	# Move left 
	if leftDown:
		#If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowwidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowheight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowheight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1

#set a while loop to run forever - True is always True
while True:	
	#draw a rectangle pygame.draw.rect(Surface - already created, color - as a tuple (R,G,B), SIZING - as a tuple (fromleft, fromtop, width, height))
	pygame.draw.rect(window, rectcolor, (rectX, rectY, rectendX, rectendY))
	pygame.draw.ellipse(window, (34,233,33), [elX , elY, elendX, elendY], 5)
	#Draw an ellipse outline, using a rectangle as the outside boundaries
	if start == 1:
		pygame.draw.ellipse(window, (34,233,33), [elX , elY, elendX, elendY], 5)
		pygame.draw.lines(window, (234,33,33), False, [[50, 50], [50, 100], [50, 50], [75, 50],[75,75],[50,75],[75,100]], 5)
		pygame.draw.lines(window, (234,33,33), False, [[100, 100], [125, 100], [100, 100], [100, 50]], 5)
		pygame.draw.lines(window, (234,33,33), False, [[207.5, 87.5],[187.5, 87.5],[200, 87.5],[200, 100],[175, 100], [175, 62.5], [200, 62.5], [200, 75]], 5)
		pygame.draw.lines(window, (234,33,33), False, [[215, 100],[215,75],[230, 75], [230, 87.5], [215, 87.5],[230, 87.5], [230, 100]], 5)
		pygame.draw.lines(window, (234,33,33), False, [[242.5,100], [242.5,75],[250,75],[250,100],[250,75],[257.5,75],[257.5,100]], 5)
		pygame.draw.lines(window, (234,33,33), False, [[285,100], [270,100],[270,87.5],[285,87.5],[270,87.5],[270,75],[285,75]], 5)
	if rectY < 75:
		rectX += 0.01
		rectY += 0.02
		rectendX += 0.01
		rectendY += 0.02
	if (rectY >= 75) & (start == 1):
		rectX = 10.0
		rectY = 10.0
		rectendX = 275.0
		rectendY = 10.0
		rectcolor = [234,33,33]
		start += 1
	if (rectY >= 75) & (start > 1) & (gr <= (windowheight - elendY)):
		window.fill((234,33,33))
		pygame.draw.ellipse(window, (34,233,33), [elX , elY, elendX, elendY], 5)
		elY += movement
		if elY >= (windowheight - elendY):
			movement = (-1*movement)
			gr += 5.0
		if elY == gr:
			movement = 0.25
	if gr >= (windowheight - elendY):
		if elX+elendX <= windowwidth - 1:
			window.fill((234,33,33))
			pygame.draw.ellipse(window, (34,233,33), [elX , elY, elendX, elendY], 5)
			elX += 1
		if elX + elendX > (windowwidth -1):
			window.fill((234,33,33))
			pygame.draw.rect(window, (255,255,255), (playerX, playerY, playerSize, playerSize))
			pygame.draw.ellipse(window, (34,233,33), [OX , OY, OendX, OendY], 5)
			OX = OX+(Omovement*Odirection*Ospeed)
			if (OX+OendX >= windowwidth - 5) & (Odirection == 1):
				Odirection = -1
				Ospeed = Ospeed *1.25
			if (OX <= 5) & (Odirection == -1):
				Odirection = 1
				Ospeed = Ospeed *1.25
			if Ospeed >= 30:
				Ospeed = Ospeed - 15*(float(random.randint(0,10))/10)
			clock.tick(60)

	# Get a list of all events that happened since the last redraw
	for event in GAME_EVENTS.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed

		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	move()
	#if you want to make the game wait		
	#clock.tick(1)
	
	pygame.display.update()
