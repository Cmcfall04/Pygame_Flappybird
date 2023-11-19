import pygame
import random

pygame.init()

class Rectangle():
    def __init__(self, distance_between, height_1, speed):
        self._dist_between = distance_between
        self._height_1 = height_1
        self._height_2 = c_height-(self._height_1 + self._dist_between)
        self._curr_x_pos_top = 450
        self._curr_x_pos_bot = 450
        self._y_pos_top = 0
        self._rect_width = 50
        self._speed = speed 
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
        
    def curr_pos(self):
        pass

    


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
     x = 7
     if pygame.key.get_pressed()[pygame.K_SPACE]:
                if posy < 0:
                    posy += 0
                else:
                    posy -= x
                    
            
##################################################################

def check_collision(top_y_pos , bot_y_pos, curr_x_range):
    global posy
    global posx
    if ((posy + 8 in top_y_pos) or (posy + 45 in bot_y_pos)) and ((posx + 20  in curr_x_range) or (posx - 20  in curr_x_range)) :
        return True
    else:
        return False



##################################################################

def score_check(curr_pos):
    global score
    global obs_speed
    key = [0,1]
    diff = curr_pos - posx
    if 0 <= diff <= 2 :
        score += 1
        print(score)
        prev_score = score
        
####################################################################
        
def next_level():
    global score
    global max_distance_between_obsticle
    global min_distance_between_obsticle
    global obs_speed
    if (score % 10 == 0) and (score > 1):
        if max_distance_between_obsticle > 150:
            max_distance_between_obsticle -= 25
            min_distance_between_obsticle -= 20 
            print(max_distance_between_obsticle)
            print(min_distance_between_obsticle)
            print("level up")
        else:
            pass
    if (score % 5 == 0) and (score > 1):
        if obs_speed < 4:
            obs_speed += 0.5
            print("speed up")
        else:
            pass
        
        


######################################## Variables

color = (255,255,255)
rect_color  = (0,255,0)
obs_color = (0,153,153)
c_width = 500
c_height = 500
obs_x_top = 450
obs_x_bot = 450
rect_height = 50
rect_width = 50
max_distance_between_obsticle = 300
min_distance_between_obsticle = 220
posx = ((c_width/2) - (rect_width/2))
posy = ((c_height/2) - (rect_height))
fall_speed = 3
score = 0
temp_score = None
obs_speed = 2      
obs_1 = None
obs_2 = False

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
     
    falling(fall_speed)

################################################### Pushes player up when space bar is pressed

    jump()

####################################################
    
    
####################################################

    #obsicle()
    if obs_1 == None:
        obs_1 = Rectangle(random.randint(min_distance_between_obsticle,max_distance_between_obsticle),random.randint(0,249), obs_speed)
        obs_1.display()
    else:
        collision = check_collision(obs_1._top_y_pos,obs_1._bot_y_pos, obs_1._curr_x_range)
        if collision:
            pygame.QUIT()
        else:
            pass
        obs_1.display()
        curr_score = score
        score_check(obs_1.curr_top_pos)
        obs_1.move()
        #print(obs_1.curr_top_pos)
        #print(f"curr pos: {posx}")
        
#################################################### Creates second obs
        
    if((obs_1.curr_top_pos) < (c_width / 2)) and (obs_2 == False):
        obs_2 = Rectangle(random.randint(100,250),random.randint(50,250), obs_speed)
        obs_2.display()
    if obs_2 != False:
        obs_2.display()
        obs_2.move()
        score_check(obs_2.curr_top_pos)
        collision2 = check_collision(obs_2._top_y_pos,obs_2._bot_y_pos, obs_2._curr_x_range)
        if collision2:
            pygame.QUIT()
        if obs_2.curr_top_pos < obs_2._rect_width:
            obs_2 = False
     
    
    if obs_1.curr_top_pos < obs_1._rect_width:
        obs_1 = None
#############################################################################################
        
    if temp_score != score:
        next_level()
    else:
        pass
    temp_score = score

        

# update the display   
    pygame.display.update() 

    clock.tick(90)









