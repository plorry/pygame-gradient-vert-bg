import pygame, sys, random
from pygame.locals import *

BLACK = (0,0,0)
BLUE = (0,0,0)
RED = (0,15,0)

FPS = 50

clock = pygame.time.Clock()

class Gradient_Vert():
	def __init__(self,screen,rect,top_color, bottom_color, steps):
		self.screen = screen
		self.rect = rect
		self.top_color = top_color
		self.bottom_color = bottom_color
		self.steps = steps
	
	def update(self):
		#pygame.draw.rect(self.screen,self.top_color,self.rect)
		color_step_size_1 = (self.top_color[0] - self.bottom_color[0]) / self.steps
		color_step_size_2 = (self.top_color[1] - self.bottom_color[1]) / self.steps
		color_step_size_3 = (self.top_color[2] - self.bottom_color[2]) / self.steps
		
		for i in range (self.steps):

			color_1 = (self.top_color[0] - (i * color_step_size_1))
			color_2 = (self.top_color[1] - (i * color_step_size_2))
			color_3 = (self.top_color[2] - (i * color_step_size_3))
			color_cur = (int(color_1),int(color_2),int(color_3))
			step_size = self.rect.height / self.steps
			rect_cur = pygame.Rect(self.rect.left,self.rect.top + (i * step_size), self.rect.width, step_size)
			#print color_cur
			if color_1 in range(0,255) and color_2 in range(0,255) and color_3 in range(0,255):
				pygame.draw.rect(self.screen, color_cur,rect_cur)
		
		color_step_size_last_1 = (self.top_color[0] - self.bottom_color[0]) / self.steps
		color_step_size_last_2 = (self.top_color[1] - self.bottom_color[1]) / self.steps
		color_step_size_last_3 = (self.top_color[2] - self.bottom_color[2]) / self.steps
		

def exit_game():
	sys.exit()
	
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((320,240),0,32)
	rect = pygame.Rect(0,0,320,240)
	gradient = Gradient_Vert(screen,rect,BLUE,RED,98)
	while 1:
		gradient.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_game()
		pygame.display.flip()
		clock.tick(FPS)