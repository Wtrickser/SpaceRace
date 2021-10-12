import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

class SpaceShip(pygame.sprite.Sprite):
  def __init__(self,path,x_pos,y_pos,speed):
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

spaceship = SpaceShip('spaceship.png',640,500,10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

class Meteor(pygame.sprite.Sprite):
  def __init__(self,path,x_pos,y_pos,x_v,y_v):
    super().__init__()
    self.image = pygame.image.load("Meteor1.png")
    self.rect = self.image.get_rect(center = (x_pos,y_pos))
  
  def update(self):
    self.rect

meteor1 = Meteor('Meteor1.png',400,400,1,1)
meteor_group = pygame.sprite.Group()
meteor_group.add(meteor1)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.fill((42,45,51))
  
  spaceship_group.draw(screen)
  spaceship_group.update()

  meteor_group.draw(screen)

  pygame.display.update()
  clock.tick(120)