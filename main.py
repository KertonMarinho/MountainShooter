import pygame

print('setup start')
pygame.init()
window = pygame.display.set_mode(size = (600, 480))
print('setup end ')

print('loop start')
while True:
	#check for all events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() #Close window
			quit() # end pygame