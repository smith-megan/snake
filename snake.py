import pygame
import time
import random

snake_speed=15

window_x =720
window_y=480

black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)

pygame.init()

pygame.display.set_caption('Snek')
game_window=pygame.display.set_mode((window_x,window_y))

fps= pygame.time.Clock()

snake_position=[100,50]
snake_body=[random.randrange(1, (window_x//10))*10,
            random.randrange(1, (window_y//10))*10]

fruit_spawn=True

direction='RIGHT'
change_to=direction

score=0

def show_score(choice, color, font, size):
  score_font=pygame.font.SysFont(font, size)

  score_surface=score_font.render('Score: '+str(score), True, color)

  score_rect = score_surface.get_rect()

  game_window.blit(score_surface,score_rect)

def game_over(): 
  my_font=pygame.font.SysFont('times new roman', 50)
  game_over_surface=my_font.render('Your Score: '+str(score), True, red)

  game_over_rect=game_over_surface.get_rect()

  game_over_rect.midtop=(window_x/2, window_y/4)

  game_window.blit(game_over_surface, game_over_rect)
  pygame.display.flip()

  time.sleep(2)

  pygame.quit()

  quit()

while True:

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        change_to='UP'
      if event.key== pygame.K_DOWN:
        change_to='DOWN'
      if event.key==pygame.K_LEFT:
        change_to='LEFT'
      if event.key==pygame.K_RIGHT:
        change_to='RIGHT'
  
  if direction=='UP':
    snake_position[1]-=10
  if direction =='DOWN':
    snake_position[1]+=10
  if direction =='LEFT':
    snake_position[0]-=10
  if direction=='RIGHT':
    snake_position[0]+=10
  

  for pos in snake_body:
    pygame.draw.rect(game_window, green, 
                    pygame.Rect(pos[0],pos[1],10,10))
  # pygame.draw.rect(game_window, white, pygame.Rect())


  show_score(1, white, 'times new roman', 20)

  pygame.display.update()
  fps.tick(snake_speed)