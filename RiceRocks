# program template for Spaceship 
#Modified by Natasha Medina
import simplegui
import math
import random

# Globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
SHIP_ANGLE_VEL_INC = 0.05
FRICTION_C= 0.1
score=0
lives=3
started = False
i=0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

#thrust ship
thrust_info = ImageInfo([135, 45], [90, 90], 35)

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
#soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def process_sprite_group(group_rocks,canvas):
    for r in list(group_rocks):
        r.draw(canvas)
        if r.update() == True:
            group_rocks.remove(r)    
            
      
        
def group_collide(group, other_object):
    #check for collisions between other_object and elements of the group
    rs = set([])
    for s in group:
        if s.collide(other_object):
            rs.add(s)         
            group.difference_update(rs)
            explosion_group.add(Sprite(s.get_position(),s.vel, 0, 0, explosion_image, explosion_info, explosion_sound))
            return True      
    return False

def group_group_collide(group1,group2):
    #check for collisions between two groups
    n = 0
    for r in list(group1): 
        if group_collide(group2,r):
            n += 1
            group1.remove(r)
    return n
    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            self.image_center = thrust_info.get_center()
            
        else: 
            self.image_center = ship_info.get_center()
            
        canvas.draw_image(self.image,self.image_center,self.image_size, [self.pos[0], self.pos[1]],self.image_size, self.angle)
        
    def update(self):
        #increment its angle by its angular velocity.
        self.angle += self.angle_vel
        #position update
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        #compute forward vector
        self.forward = angle_to_vector(self.angle)
        #friction update
        self.vel[0] *= (1-FRICTION_C)
        self.vel[1] *= (1-FRICTION_C)
        
        if self.thrust:
            self.vel[0] += self.forward[0]
            self.vel[1] += self.forward[1]
    
        if self.pos[0] <= self.radius or self.pos[0] >= WIDTH - self.radius:
            self.pos[0] %= WIDTH
        if self.pos[1] <= self.radius or self.pos[1] >= HEIGHT - self.radius:
            self.pos[1] %= HEIGHT
        
    def turn_thrust(self,sound, on):
        self.thrust = on
        if on:
            sound.play()
        else: 
            sound.rewind()
            
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
            
    def shoot_missile(self):
        global missile_group
        shoot_vel = (self.vel[0]+ 4*self.forward[0],self.vel[1]+ 4*self.forward[1]) 
        missile_pos = (self.pos[0] + self.forward[0]*self.radius,
                       self.pos[1] + self.forward[1]*self.radius)
        missile_group.add(Sprite(missile_pos, shoot_vel, self.angle, 0, missile_image, missile_info, missile_sound))
    
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            index_age = self.age % 24
            canvas.draw_image(self.image,[self.image_center[0]+self.image_size[0]*index_age,self.image_center[1]],self.image_size, [self.pos[0], self.pos[1]],self.image_size, self.angle)
            self.age+=1
            if self.age % 24 == 0:
                self.animated = False
        else:
            canvas.draw_image(self.image,self.image_center,self.image_size, [self.pos[0], self.pos[1]],self.image_size, self.angle)
        
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]       
               
        if self.pos[0] <= self.radius or self.pos[0] >= WIDTH - self.radius:
            self.pos[0] %= WIDTH
        if self.pos[1] <= self.radius or self.pos[1] >= HEIGHT - self.radius:
            self.pos[1] %= HEIGHT
        
        self.age += 1
        
        if self.age >= self.lifespan:
            return True
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def collide(self, other_object):
        return dist(self.pos,other_object.get_position()) <= self.radius + other_object.get_radius()

# define key handlers to control turning ship

def keydown(key):
    if simplegui.KEY_MAP["left"] == key:
        my_ship.angle_vel -= SHIP_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.angle_vel += SHIP_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.turn_thrust(ship_thrust_sound, True)
    elif simplegui.KEY_MAP["space"] == key:   
            my_ship.shoot_missile()
def keyup(key):
    if simplegui.KEY_MAP["left"] == key:
        my_ship.angle_vel += SHIP_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.angle_vel -= SHIP_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.turn_thrust(ship_thrust_sound,False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    splash_width = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    splash_height = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and splash_width and splash_height:
        lives = 3
        score = 0
        started = True     
           
def draw(canvas):
    global time, lives, score, started, soundtrack
    global rock_group, explosion_group
   
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    #draw UI
    canvas.draw_text("Lives", [30, 40], 25, 'White')
    canvas.draw_text(str(lives), [50, 70], 25, 'White')
    canvas.draw_text("Score", [730, 40], 25, 'White')
    canvas.draw_text(str(score), [750, 70], 25, 'White')
    # draw ship and missile
    my_ship.draw(canvas)   
    # update ship and missile
    my_ship.update()
    #draw and update sprites 
    if started:
        process_sprite_group(rock_group, canvas)
        process_sprite_group(explosion_group, canvas)
        soundtrack.play()
        soundtrack.set_volume(0.3)
        #to detect ship collisions.
        if group_collide(rock_group, my_ship):
            lives -= 1
            if lives == 0: 
                rock_group = set([])
                explosion_group = set ([])
                started = False
        #to detect missile/rock collisions.   
        score += group_group_collide(missile_group, rock_group)
        
    process_sprite_group(missile_group,canvas)

        
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        soundtrack.rewind()
   
   
        
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, pos, started
    global i
    vel= [random.randint(1,2),random.randint(1,2)]
    ang_vel=(random.randint(0,10)*0.01)- 0.05
    pos= [random.randint(0,WIDTH),random.randint(0,HEIGHT)]
        
    if started and dist(pos,my_ship.get_position()) > 5 * my_ship.get_radius():
        if len(rock_group) < 12:
            print "ID' rock",i
            rock_group.add(Sprite(pos,vel, 0, ang_vel, asteroid_image, asteroid_info))
            i+=1    
        else: 
            i = 0
    else:
        if not (dist(pos,my_ship.get_position()) > 5 * my_ship.get_radius()):
            print "IGNORE ROCK SPAWN!"
            rock_group.discard(Sprite(pos,vel, 0, ang_vel, asteroid_image, asteroid_info))
            

   
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH/2, HEIGHT/2], [0,0], 0, ship_image, ship_info)
rock_group = set([])
missile_group =  set([])
explosion_group = set ([])
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling

timer.start()
frame.start()
