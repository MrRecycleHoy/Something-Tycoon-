import pygame, random
from pygame.sprite import Group

pygame.init()
print("Pygame initialized")
screen = pygame.display.set_mode((600, 600))  # Width, Height
pygame.display.set_caption('MiniMonopoly')

#Clock object
clock = pygame.time.Clock()
FPS = 10

#Game vars
tile_size = 30
spawn_position = ()
wallss = []

#Create wall of the level
world_data = []

#Create wall group
wall_group = pygame.sprite.Group()

#Draw Grid
def draw_grid(tile):
    screen.fill((0, 0, 0))
    for x in range(tile, 800, tile):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 600))
    for y in range(tile, 600, tile):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (800, y))

#Create objective
def objective_position():
    pos = [random.randint(1, 18), random.randint(1, 18)]

    while pos[0] == players.rect.x or pos[1] == players.rect.y or pos in wallss:
        pos = [random.randint(1, 18), random.randint(1, 18)]
        
    return pos

#Class
class player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.moving = False
        self.velocity = 1
        self.dx = self.velocity
        self.dy = 0

    def update(self):
        self.image.fill(self.color)
        self.rect.x = self.x * tile_size
        self.rect.y = self.y * tile_size

        screen.blit(self.image, self.rect)
    
    def move(self):
        if self.moving and not self.collision_with_walls():
            self.x += self.dx
            self.y += self.dy
    
    def collision_with_walls(self):
        for wall in wall_group:
            if wall.x == self.x + self.dx and wall.y == self.y + self.dy:
                return True
        return False

class walls(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * tile_size
        self.rect.y = self.y * tile_size

class collectible():
    def __init__(self):
        self.pos = objective_position()
        self.x = self.pos[0] * tile_size
        self.y = self.pos[1] * tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self):
        screen.blit(self.image, self.rect)

#Open level file
with open('Something-Tycoon-/Map/world.txt', 'r') as f:
    for line in f:
        world_data.append(line)

#Create walls
for row, tiles in enumerate(world_data):
    for col, tile in enumerate(tiles):
        if tile == '1':
            wall = walls(row, col, (0, 0, 255))
            wallss.append([row, col])
            wall_group.add(wall)
        elif tile == 'P':
            spawn_position = (row, col)

#Create player
players = player(spawn_position[0], spawn_position[1], (0, 255, 0))

#Create collectibles
collectable = collectible()

#Main loop
running = True
while running:

    clock.tick(FPS)
    draw_grid(tile_size)

    players.update()
    players.move()

    if collectable.rect.colliderect(players.rect):
        collectable = collectible()
    collectable.draw()
    
    wall_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                players.moving = True
                players.dx = -players.velocity
                players.dy = 0

            elif event.key == pygame.K_RIGHT:
                players.moving = True
                players.dx = players.velocity
                players.dy = 0
                
            elif event.key == pygame.K_UP:
                players.moving = True
                players.dy = -players.velocity
                players.dx = 0

            elif event.key == pygame.K_DOWN:
                players.moving = True
                players.dy = players.velocity
                players.dx = 0

        elif event.type == pygame.KEYUP:
            players.moving = False

    pygame.display.update()

pygame.quit()