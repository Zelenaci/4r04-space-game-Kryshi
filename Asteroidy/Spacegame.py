#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:43:38 2018
@author: KrySt
"""

#importing all modules
import random
import pyglet
from pyglet.window.key import DOWN, UP, LEFT, RIGHT
from math import sin, cos, radians, pi

#creating background and window
window = pyglet.window.Window(1920, 1080)
batch = pyglet.graphics.Batch()  
image = pyglet.image.load("space.png")

#defining meteors
class Shooter(object):

    def __init__(self, x=None, y=None, direction=None, speed=None, rspeed=None):
        num = random.choice(range(1, 8))
        self.image = pyglet.image.load('{}.png'.format(num))
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        self.x = random.randint(0, window.width )
        self.y = random.randint(800, window.height )
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.direction = random.randint(180, 359)
        self.speed = random.randint(50, 200)
        self.rspeed = random.randint(-2, 5)

    def tick(self, dt):
        self.bounce()
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation +=self.rspeed
        #collision check
        if abs(self.x-lod.x) < self.image.width /2 and abs(self.y-lod.y) < self.image.height /2:
            konec=pyglet.text.Label('YOU DIED',font_size=70, x=window.width//2, y=window.height//2,
                                      anchor_y="center",anchor_x='center')
            @window.event
            def on_draw():
                image.blit(0,0)
                konec.draw()
            
        
    def bounce(self):
        # vzdálenost okraje a středu
        rozmer = min(self.image.width, self.image.height)/2

        if self.x + rozmer >= window.width:
            self.direction = random.randint(190, 350)
            return
        if self.x - rozmer <= 0:
            self.direction = random.randint(10, 170)
            return
        if self.y + rozmer >= window.height:
            self.direction = random.randint(100, 260)
            return
        if self.y - rozmer <= 0:
            self.direction = random.randint(-80, 80)
            return
    


class Lodka(object):
    
    def __init__(self):
        self.obrazek = pyglet.image.load("bigship.png")
        self.obrazek.anchor_x = self.obrazek.width // 2
        self.obrazek.anchor_y = self.obrazek.height // 2
        self.sprite =pyglet.sprite.Sprite(self.obrazek,batch=batch)
        self.sprite.rotation=60
        self.speed= 0
        self.x=960
        self.y=540
        self.sprite.x = self.x
        self.sprite.y = self.y
    def tiktak(self,t):
        global klavesy
        self.x = self.sprite.x + self.speed*t*sin(pi*self.sprite.rotation/180)
        self.sprite.x=self.x
        self.y = self.sprite.y + self.speed*t*cos(pi*self.sprite.rotation/180)
        self.sprite.y=self.y
        self.okraj()
        
        for sym in klavesy:
            if sym == UP:
                if self.speed < 500:
                    self.speed += 25
                    
            if sym == DOWN:
                if self.speed > 10:
                    self.speed -= 10
                    
            if sym == LEFT:
                self.sprite.rotation -= 5
            if sym == RIGHT:
                self.sprite.rotation += 5
                
          
    def okraj(self):
        # vzdálenost okraje a středu
        rozmer = min(self.obrazek.width, self.obrazek.height)/2
        if self.x + rozmer >= window.width+60:
            self.sprite.x=-20
        if self.x - rozmer < -60:
            self.sprite.x=window.width+20
        if self.y + rozmer >= window.height + 60:
            self.sprite.y=-20
        if self.y - rozmer < -60:
            self.sprite.y=window.height+20  



klavesy=set()        
for o in range(1):
    lod=Lodka()
    pyglet.clock.schedule_interval(lod.tiktak, 1/ 30 )

for x in range(20):
    stone=Shooter()
    pyglet.clock.schedule_interval(stone.tick, 1/ 30 )


@window.event
def on_key_press(data, mod):
    global klavesy
    klavesy.add(data)
    

@window.event
def on_key_release(data, mod):
    global klavesy
    klavesy.remove(data)


@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    batch.draw()
    
    


pyglet.app.run()