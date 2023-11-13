import pygame
import random

pygame.init()

class Rectangle():
    def __init__(self, distance_between, height_1):
        self._dist_between = distance_between
        self._height_1 = height_1
        self._height_2 = c_height-(self._height_1 + self._dist_between)
        self._curr_x_pos_top = 450
        self._curr_x_pos_bot = 450
        self._y_pos_top = 0
        self._rect_width = 50
        self._speed = 0.5
        self._top_y_pos = [num for num in range(self._height_1 + 1)]
        self._bot_y_pos = [num for num in range((self._height_1 + self._dist_between),c_height+1)]
        self._curr_x_range = [num for num in range((self._curr_x_pos_top - int((self._rect_width/2))), (self._curr_x_pos_top + int((self._rect_width/2) + 1)))]
        
    @property
    def curr_top_pos(self):
        return self._curr_x_pos_top
    @property
    def curr_bot_pos(self):
        return self._curr_x_pos_bot
    
    def display(self):
        pygame.draw.rect(canvas, obs_color,(self._curr_x_pos_top ,0 ,self._rect_width, self._height_1))
        pygame.draw.rect(canvas, obs_color,(self._curr_x_pos_bot ,(self._height_1 + self._dist_between),self._rect_width, self._height_2))
    
    def move(self):
        self._curr_x_pos_top -= self._speed
        self._curr_x_pos_bot -= self._speed
        self._curr_x_range = [num for num in range(int((self._curr_x_pos_top - int((self._rect_width/2)))), int((self._curr_x_pos_top + int((self._rect_width/2) + 1))))]

    


################################################################################################################## Falling funtion
def falling(fall_speed = 2):
    # Changes the y position
    global posy

    posy += fall_speed
    if posy > c_height - rect_height:
        pygame.QUIT()

# Clears screen to all white

    canvas.fill((255, 255, 255))

# Draws new rectangles with updated cordinates

    pygame.draw.rect(canvas, rect_color,(posx ,posy ,rect_width, rect_height))
#############################################################################################################################################

def jump():
     global posy
     if pygame.key.get_pressed()[pygame.K_SPACE]:
                if posy < 0:
                    posy += 0
                else:
                    posy -= 5
            
##################################################################

def check_collision():
    global posy
    global posx
    if ((posy + 8 in t1._top_y_pos) or (posy + 45 in t1._bot_y_pos)) and ((posx + 25  in t1._curr_x_range) or (posx - 25  in t1._curr_x_range)) :
        return True
    else:
        return False



##################################################################

def obsicle():
     global obs_x_top
     global obs_x_bot
     distance_between = random.randint(200,250)
     height_of_obs = random.randint(100,200)
     height_1 = height_of_obs
     inbetween = distance_between
     pygame.draw.rect(canvas, obs_color,(obs_x_top ,0 ,rect_width, height_1))
     pygame.draw.rect(canvas, obs_color,(obs_x_bot ,(height_1 + inbetween),rect_width, 500))
         
     


######################################## Variables

color = (255,255,255)
rect_color = (0,255,0)
obs_color = (0,0,0)
c_width = 500
c_height = 500
obs_x_top = 450
obs_x_bot = 450
rect_height = 50
rect_width = 50
posx = ((c_width/2) - (rect_width/2))
posy = ((c_height/2) - (rect_height))
fall_speed = 2
t1 = None

#########################################

create_obs = pygame.USEREVENT + 1

# CREATING CANVAS 
canvas = pygame.display.set_mode((c_width, c_height)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("My Flappy Game") 
exit = False
  
clock = pygame.time.Clock()

while not exit: 
    canvas.fill(color)
    for event in pygame.event.get():
        if event.type == create_obs:
            obsicle()
        if event.type == pygame.QUIT: 
            exit = True
            
        
            
################################################## Makes player constntly fall       
     
    falling()

###################################################

    jump()

####################################################

    #obsicle()
    if t1 == None:
        t1 = Rectangle(random.randint(200,250),random.randint(50,300))
        t1.display()
    else:
        t1.display()
        t1.move()
        
####################################################
     
    collision = check_collision()
    print(collision)
    if collision:
        pygame.QUIT()
    else:
        pass
    
        

# update the display   
    pygame.display.update() 

    clock.tick(90)









