#!/bin/python3.7

"""
Snak
A snake clone with bad spelling
Made with PyGame
"""
print("importing pygame")
import pygame
print("importing sys")
import sys
print("importing time")
import time
print("importing random")
import random
print("imports done")

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
speed = 10

# Window size
frame_size_x = 720
frame_size_y = 480

print("checking for errors")
# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print("oof")
    print("we errored")
    print("error code: " + check_errors[1])
    sys.exit(-1)
else:
    print("game is good")


# Initialise game window
print("init started")
pygame.display.set_caption("Snak")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
print("init done")

# Wait function used in game_over()
print("defining wait")
from pygame.locals import *
def wait():
    while True:
              if event.key == pygame.K_F5:
                print("f5 pressed")
                restart = True
                return
              elif event.key != pygame.K_F5:
                print("any key pressed")
                restart = False
                return
              if event.type == QUIT:
                print("closed from wait()")
                pygame.quit()
                sys.exit()
print("wait define done")

# Colors (R, G, B)
print("defining colors")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
print("color define done")

# FPS (frames per second) controller
print("defining fps controller")
fps_controller = pygame.time.Clock()
print("fps controller define done")

# Game variables
print("defining vars")
print("starting snake vars define")
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
print("snake vars done; now starting food vars")
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True
print("food vars done; now starting direction vars")
direction = "right"
change_to = direction
print("direction vars done; now defining score")
score = 0
screen_draw_num = 0
restart = True
print("defining vars done")

# Game Over
print("game over event define")
def game_over():
    print("death")
    my_font = pygame.font.SysFont("times new roman", 90)
    game_over_surface = my_font.render("u died", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, "times", 20, True)
    pygame.display.flip()
    print("score: " + str(score))
    print("snake head position: " + str(snake_pos))
    print("other snake parts: " + str(block))
    print("facing: " + str(direction))
    print("speed: "  + str(speed))
    print("screen refresh number: " + str(screen_draw_num))
    print("waiting")
    wait()
print("game over event define done")

# Score
print("score define")
def show_score(choice, color, font, size, on_end):
    if on_end == False:
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("score : " + str(score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x/10, 15)
        else:
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
        game_window.blit(score_surface, score_rect)
        # pygame.display.flip()
    elif on_end == True:
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("score : " + str(score) + "       press F5 to restart or press the any key to exit", True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (frame_size_x/10, 15)
        else:
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
        game_window.blit(score_surface, score_rect)
        # pygame.display.flip()
print("score define done")

print("starting game")

# Main logic
if restart == True:
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              print("quitting")
              pygame.quit()
              sys.exit()
          # Whenever a key is pressed down
          elif event.type == pygame.KEYDOWN:
              print("key pressed")
              # W -> up; S -> down; A -> left; D -> right
              if event.key == pygame.K_UP or event.key == ord("w"):
                  change_to = "up"
                  print("w")
              if event.key == pygame.K_DOWN or event.key == ord("s"):
                  change_to = "down"
                  print("s")
              if event.key == pygame.K_LEFT or event.key == ord("a"):
                  change_to = "left"
                  print("a")
              if event.key == pygame.K_RIGHT or event.key == ord("d"):
                  change_to = "right"
                  print("d")
              # F1 -> less hard; F2 -> more hard; limits are 5 and 200
              if event.key == pygame.K_F1 and not speed - 5 >= 5:
                  speed -= 5
                  print("F1")
              if event.key == pygame.K_F2 and not speed + 5 >= 200:
                  speed += 5
                  print("F2")
              # Esc -> Create event to quit the game
              if event.key == pygame.K_ESCAPE:
                  print("ESC")
                  print("closed from main logic")
                  pygame.event.post(pygame.event.Event(pygame.QUIT))
      # Making sure the snake cannot move in the opposite direction instantaneously
      if change_to == "up" and direction != "down":
          direction = "up"
      if change_to == "down" and direction != "up":
          direction = "down"
      if change_to == "left" and direction != "right":
          direction = "left"
      if change_to == "right" and direction != "left":
          direction = "right"
      # Moving the snake
      if direction == "up":
          snake_pos[1] -= 10
          print("moved up")
      if direction == "down":
          snake_pos[1] += 10
          print("moved down")
      if direction == "left":
          snake_pos[0] -= 10
          print("moved left")
      if direction == "right":
          snake_pos[0] += 10
          print("moved right")
      # Snake body growing mechanism
      snake_body.insert(0, list(snake_pos))
      if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
          score += 1
          speed_temp = speed
          speed += random.randrange(1, 5)
          print("added " + str(speed - speed_temp))
          print("new speed: " + str(speed))
          food_spawn = False
          print("yum food")
      else:
          snake_body.pop()
      # Spawning food on the screen
      if not food_spawn:
          food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
          print("spawning food")
      food_spawn = True
      # GFX
      game_window.fill(black)
      for pos in snake_body:
          # Snake body
          # .draw.rect(play_surface, color, xy-coordinate)
          # xy-coordinate -> .Rect(x, y, size_x, size_y)
          screen_draw_num += 1
          pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
      # Snake food
      pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
      # Game Over conditions
      # Getting out of bounds
      if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
          print("out of bounds on x")
          game_over()
      if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
          print("out of bounds on y")
          game_over()
      # Touching the snake body
      for block in snake_body[1:]:
          if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
              print("hit snake body")
              game_over()
      show_score(1, white, "consolas", 20, False)
      # Refresh game screen
      pygame.display.update()
      # Refresh rate
      fps_controller.tick(speed)
pygame.quit()
sys.exit()
