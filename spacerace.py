import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

class SpaceShip(pygame.sprite.Sprite):
  def __init__(self,path,x_pos,y_pos):
    super().__init__()
    self.image = pygame.image.load(path)
    self.rect = self.image.get_rect(center = (x_pos,y_pos))
  def update(self):
    self.rect.center = pygame.mouse.get_pos()
    self.screen_constrain()
  
  def screen_constrain(self):
    if self.rect.right >= 1280:
      self.rect.right = 1280
    if self.rect.left <= 0:
      self.rect.left = 0
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= 720:
      self.rect.bottom = 720

spaceship = SpaceShip('spaceship.png',640,500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

class Meteor(pygame.sprite.Sprite):
  def __init__(self,path,x_pos,y_pos,x_v,y_v):
    super().__init__()
    self.image = pygame.image.load("Meteor1.png")
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
    if event.type == pygame.MOUSEBUTTONDOWN:
      new_laser = Laser('Laser.png', event.pos,15)
      laser_group.add(new_laser)

  screen.fill((42,45,51))
  
  laser_group.draw(screen)
  laser_group.update()

  spaceship_group.draw(screen)
  spaceship_group.update()

  meteor_group.draw(screen)
  meteor_group.update()

  pygame.display.update()
  clock.tick(120)