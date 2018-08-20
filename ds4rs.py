import math
import random

RandomRadius = 2

def pythag(x,y):
	x = x * x
	y = y * y
	return(math.sqrt(x+y))

def rr(x):
	return x + random.uniform(RandomRadius * -1, RandomRadius)

try:
	import pyautogui
	import pygame

	screenWidth, screenHeight = pyautogui.size()
	currentMouseX, currentMouseY = pyautogui.position()
	pyautogui.moveTo(100, 100, .5, pyautogui.easeOutQuad)
	pyautogui.click()
	pygame.init()
	joystick = pygame.joystick.Joystick(0)
	joystick.init()

	posX = 500
	posY = 500;
	radius = 10;
	moving = False

	oldLocX = 0
	oldLocY = 0

	calibrating = True
	mappings = [None,None,None,None,None,None]

	while True:
		for event in pygame.event.get():
					if event.type == pygame.JOYBUTTONDOWN:
						#buttons 0-5, 10, 11 custon
						#buttons 6 and 7 are L and R click
						#button 8 is remap
						#button 9 is calibrate



						#for x in range(joystick.get_numbuttons()):
						if(joystick.get_button(6)):
							pyautogui.click(button='right')
						if(joystick.get_button(7)):
							pyautogui.click()


						if(joystick.get_button(9)):
							if calibrating:
								posX, posY = pyautogui.position()
								print("center set to" + str(pyautogui.position()))
								calibrating = False
							else:
								tx, ty= pyautogui.position()
								radius = pythag(tx - posX, ty - posY)
								print("radius set to" + str(radius))
								calibrating = True

						if(joystick.get_button(8)):
							print("Started looking for button remap")
							looping = True
							while looping:
								for event in pygame.event.get():
									if event.type == pygame.JOYBUTTONDOWN:
										for x in range(6):
											if(joystick.get_button(x)):
												mappings[x] = pyautogui.position()
												looping = False
						for x in range(5):
							if(joystick.get_button(x)):
								if mappings[x] is not None:
									print("button " + str(x) + " set to " + str(mappings[x]))
									px, py = mappings[x]
									ox, oy = pyautogui.position()
									pyautogui.moveTo(rr(px), rr(py), 0.1 + random.uniform(0,0.1), pyautogui.easeOutQuad)
									pyautogui.click()
									pyautogui.moveTo(rr(ox), rr(oy), 0.1 + random.uniform(0,0.1), pyautogui.easeOutQuad)

					if event.type == pygame.JOYAXISMOTION:
						#print(joystick.get_name() + " " + str(joystick.get_numaxes()) + "\n")
						if(pythag(joystick.get_axis(0), joystick.get_axis(1)) > 0.4):
							if not moving:
								oldLocX, oldLocY = pyautogui.position();
							moving = True
							tempX = joystick.get_axis(0) * radius
							tempY = joystick.get_axis(1) * radius
							pyautogui.moveTo(posX + tempX, posY + tempY, .1, pyautogui.easeOutQuad)
							pyautogui.click()
						elif moving:
							#pyautogui.moveTo(posX, posY, .1, pyautogui.easeOutQuad)
							#pyautogui.click()
							moving = False
							pyautogui.moveTo(oldLocX, oldLocY, .1, pyautogui.easeOutQuad)



		#time.sleep(0.05)
except KeyboardInterrupt:
	pass


