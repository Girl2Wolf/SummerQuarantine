
import pygame
import sys
import random


pygame.init()



#my varibles
Width = (800)
Hight = (600)
EnemyColor = (0,0,255)
PlayerColor = (255,0,0)
#CHTC is Community health text color
CHTC = (255,255,0)
MTC = (255,0,255)
FriendColor = (255,255,255)
Player_Size = 50
Speed = 20
Player_Position = [(Width/2), (Hight-2*Player_Size)]
Enemy_Size = 50
Enemy_pos = [random.randint(0,Width-Enemy_Size),0]
Enemylist = [Enemy_pos]
Friend_Size = 50
Friend_pos = [random.randint(0,Width-Friend_Size),0]
Friendlist = [Friend_pos]
CHscore = 0
Mscore = 0

myFont = pygame.font.SysFont("freemono", 20)

background= (0,0,0)
screen = pygame.display.set_mode((Width, Hight))

gameover = False

clock = pygame.time.Clock()

# DO NOT TOUCH THESE SQUARES

def drop_enemies(Enemylist):
  delay = random.random()
  if len(Enemylist) < 10 and delay < 0.2:
    x_pos = random.randint(0, Width-Enemy_Size)
    y_pos = 0
    Enemylist.append([x_pos, y_pos])

def draw_enemies(Enemylist):
  for  Enemy_pos in Enemylist:
    pygame.draw.rect(screen, EnemyColor, (Enemy_pos[0], Enemy_pos[1], Enemy_Size, Enemy_Size)) 

def update_enemy_pos(Enemylist, CHscore):
    #Update of Enemy position 
  for idx, Enemy_pos in enumerate(Enemylist):
    if Enemy_pos[1]>= 0 and Enemy_pos[1]<Hight:
      Enemy_pos[1] += Speed
    else: 
      Enemylist.pop(idx)
      CHscore += 1
  return CHscore

def collision_check (Enemylist, Player_Position):
  for Enemy_pos in Enemylist:
    if detect_collision(Player_Position, Enemy_pos):
      return True
  return False


def detect_collision(Player_Position, Enemy_pos):
  p_x = Player_Position[0]
  p_y = Player_Position[1]

  e_x = Enemy_pos[0]
  e_y = Enemy_pos[1]
  if (e_x >= p_x and e_x < (p_x+ Player_Size)) or (p_x >= e_x and p_x < (e_x+Enemy_Size)):
    if (e_y >= p_y and e_y < (p_y+ Player_Size)) or (p_y >= e_y and p_y < (e_y+Enemy_Size)):
      return True
  return False

#THESE WILL BE FRIENDS

def drop_friends(Friendlist):
  delay = random.random()
  if len(Friendlist) < 2 and delay < 0.2:
    x_pos = random.randint(0, Width-Friend_Size)
    y_pos = 0
    Friendlist.append([x_pos, y_pos])

def draw_friends(Friendlist):
  for  Friend_pos in Friendlist:
    pygame.draw.rect(screen, FriendColor, (Friend_pos[0], Friend_pos[1], Friend_Size, Friend_Size)) 

def update_friend_pos(Friendlist, Mscore):
    #Update of Friend position 
  for idx, Friend_pos in enumerate(Friendlist):
    if Friend_pos[1]>= 0 and Friend_pos[1]<Hight:
      Friend_pos[1] += Speed
    else: 
      Friendlist.pop(idx)
      Mscore -= 1
  return Mscore

def Fcollision_check (Friendlist, Player_Position, Mscore):
  for Friend_pos in Friendlist:
    if Fdetect_collision(Player_Position, Friend_pos):
      Mscore += 5
      return Mscore
      return True
  return False


def Fdetect_collision(Player_Position, Friend_pos):
  p_x = Player_Position[0]
  p_y = Player_Position[1]

  f_x = Friend_pos[0]
  f_y = Friend_pos[1]
  if (f_x >= p_x and f_x < (p_x+ Player_Size)) or (p_x >= f_x and p_x < (f_x+Friend_Size)):
    if (f_y >= p_y and f_y < (p_y+ Player_Size)) or (p_y >= f_y and p_y < (f_y+Friend_Size)):
      return True
  return False

while not gameover:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.KEYDOWN:
      print(f"key down was {event.key}")

      x = Player_Position[0]
      y = Player_Position[1]
      if event.key == pygame.K_LEFT:
        x -= Player_Size
      elif event.key == pygame.K_RIGHT:
        x+= Player_Size
      Player_Position= [x,y]

  screen.fill(background) 

  if detect_collision(Player_Position, Enemy_pos):
    gameover = True
    break

  if collision_check (Enemylist, Player_Position):
    gameover = True
    break

  if Fdetect_collision(Player_Position, Friend_pos):
      Mscore += 1
    

    

  CHscore = update_enemy_pos(Enemylist, CHscore)
 

  text = "Community Health Score:" + str(CHscore)
  label = myFont.render(text, 1, CHTC)
  screen.blit(label, (Width - 600, Hight - 40))

  Mscore = update_friend_pos(Friendlist, Mscore)
  Mtext = "Mental Health Score:" + str(Mscore)
  Mlabel = myFont.render(Mtext, 1, MTC)
  screen.blit(Mlabel, (Width - 300, Hight - 40))

  drop_friends(Friendlist)
  draw_friends(Friendlist)
  update_friend_pos(Friendlist, Mscore)
  

  drop_enemies(Enemylist)
  draw_enemies(Enemylist)
  pygame.draw.rect(screen, PlayerColor, (Player_Position[0], Player_Position[1], Player_Size, Player_Size))

  clock.tick(30)
  pygame.display.update()
