import pygame
import random

pygame.init()




################################################################################################################## Falling funtion
def falling(fall_speed = 2):
    # Changes the y position
    global posy

    posy += fall_speed
    if posy == c_height + rect_height:
        posy = -rect_height

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

def obsicle():
     distance_between = random.randint(150,250)
     height_of_obs = random.randint(100,400)
     height_1 = height_of_obs
     inbetween = distance_between
     pygame.draw.rect(canvas, obs_color,(450 ,0 ,rect_width, 150))
     pygame.draw.rect(canvas, obs_color,(400 ,200 ,rect_width, 500))
     


######################################## Variables

color = (255,255,255)
rect_color = (0,255,0)
obs_color = (0,0,0)
c_width = 500
c_height = 500
rect_height = 50
rect_width = 50
posx = ((c_width/2) - (rect_width/2))
posy = ((c_height/2) - (rect_height))
fall_speed = 2

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
            distance_between = random.randint(150,250)
            height_of_obs = random.randint(100,400)
            height_1 = height_of_obs
            inbetween = distance_between
            pygame.draw.rect(canvas, obs_color,(450 ,0 ,rect_width, 200))
            pygame.draw.rect(canvas, obs_color,(450 ,350 ,rect_width, 200))
        if event.type == pygame.QUIT: 
            exit = True
            
        
            
################################################## Makes player constntly fall       
     
    falling()

###################################################

    jump()

####################################################

    obsicle()
    #pygame.time.set_timer(create_obs,1500)

# update the display   
    pygame.display.update() 

    clock.tick(90)









