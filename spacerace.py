import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
score = 0
game_font = pygame.font.Font(None,40)

class SpaceShip(pygame.sprite.Sprite):
  def __init__(self,path,x_pos,y_pos):
    super().__init__()
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(center = (x_pos,y_pos))
    self.shield_surface = pygame.image.load('shield.png')
    self.health = 5
  def update(self):
    self.rect.center = pygame.mouse.get_pos()
    self.screen_constrain()
    self.display_health()
  def screen_constrain(self):
    if self.rect.right >= 1280:
      self.rect.right = 1280
    if self.rect.left <= 0:
      self.rect.left = 0
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= 720:
      self.rect.bottom = 720
  def display_health(self):
    for index,shield in enumerate(range(self.health)):
      screen.blit(self.shield_surface,(10 + index * 40 ,10))
  def get_damage(self,damage_amount):
    self.health -= damage_amount

spaceship = SpaceShip('spaceship.png',640,500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

class Meteor(pygame.sprite.Sprite):
  def __init__(self,path,x_pos,y_pos,x_v,y_v):
    super().__init__()
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(center = (x_pos,y_pos))
    self.x_v = x_v
    self.y_v = y_v
  def update(self):
    self.rect.centerx += self.x_v
    self.rect.centery += self.y_v
    if self.rect.centery >= 800:
      self.kill()

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,100)

class Laser(pygame.sprite.Sprite):
  def __init__(self,path,pos,speed):
    super().__init__()
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(center = pos)
    self.speed = speed
  def update(self):
    self.rect.centery -= self.speed
    if self.rect.centery <= -100:
      self.kill()

laser_group = pygame.sprite.Group()

def main_game():
  pygame.mouse.set_visible(False)
  laser_group.draw(screen)
  laser_group.update()

  spaceship_group.draw(screen)
  spaceship_group.update()

  meteor_group.draw(screen)
  meteor_group.update()

  if pygame.sprite.spritecollide(spaceship_group.sprite,meteor_group,True):
    spaceship_group.sprite.get_damage(1)

  for laser in laser_group:
    pygame.sprite.spritecollide(laser,meteor_group,True)

  return 1

def end_game():
  pygame.mouse.set_visible(True)
  text_surface = game_font.render('Game Over', True, (255,255,255))
  text_rect = text_surface.get_rect(center = (640,340))
  screen.blit(text_surface, text_rect)
  
  score_surface = game_font.render(f'Score: {score}', True, (255,255,255))
  score_rect = score_surface.get_rect(center = (640,380))
  screen.blit(score_surface, score_rect)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == METEOR_EVENT:
      meteor_path = random.choice(('Meteor1.png','Meteor2.png','Meteor3.png'))
      random_x_pos = random.randrange(0,1280)
      random_y_pos = random.randrange(-500,-50)
      random_x_v = random.randrange(-1,1)
      random_y_v = random.randrange(4,10)
      meteor = Meteor(meteor_path,random_x_pos,random_y_pos,random_x_v,random_y_v)
      meteor_group.add(meteor)
    if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
      spaceship_group.sprite.health = 5
      score = 0
      meteor_group.empty()
    if event.type == pygame.MOUSEBUTTONDOWN:
      new_laser = Laser('Laser.png',event.pos,15)
      laser_group.add(new_laser)

  screen.fill((42,45,51))
  
  if spaceship_group.sprite.health > 0:
   score += main_game()
  else:
    end_game()

  pygame.display.update()
  clock.tick(120)