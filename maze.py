
from pygame.locals import *
import pygame

cell_size = 48

class Player:
    x = 1
    y = 1
    speed = 1
 
    def moveRight(self):
        self.x = self.x + self.speed
        # print("x = ", self.player.x, " y = ", self.player.y)
        print("x = ", self.x, " y = ", self.y)
 
    def moveLeft(self):
        self.x = self.x - self.speed
        print("x = ", self.x, " y = ", self.y)
 
    def moveUp(self):
        self.y = self.y - self.speed
        print("x = ", self.x, " y = ", self.y)
 
    def moveDown(self):
        self.y = self.y + self.speed
        print("x = ", self.x, " y = ", self.y)
        
class Maze:
    def __init__(self):
    
       #self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                     # 1,0,0,0,0,0,0,0,0,1,
                     # 1,0,0,0,0,0,0,0,0,1,
                     # 1,0,1,1,1,1,1,1,0,1,
                     # 1,0,1,0,0,0,0,0,0,1,
                     # 1,0,1,0,1,1,1,1,0,1,
                     # 1,0,0,0,0,0,0,0,0,1,
                     # 1,1,1,1,1,1,1,1,1,1,]
        self.maze = []
        with open('data.txt', 'r') as f:
            l = [[int(num) for num in line.split()] for line in f]
        print(l)
        self.maze = l


    def draw(self,display_surf,block_surf):
       bx = 0
       by = 0
       red = (255,0,0)
       for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 1:
                    #pygame.draw.rect(display_surf,red,((i-1)*cell_size,(j-1)*cell_size,cell_size,cell_size))
                    display_surf.blit(block_surf,(j*cell_size , i*cell_size))
      
                

class App:
 
    windowWidth = 1000
    windowHeight = 900
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        self._running = True
        self._image_surf = pygame.image.load("ball.png").convert()
        self._block_surf = pygame.image.load("wall.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x*cell_size,self.player.y*cell_size))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            #self.on_loop()
            
            self.on_render()
           # print("Hello")
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()