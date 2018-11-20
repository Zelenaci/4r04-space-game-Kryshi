#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:26:16 2018

@author: KrySt
"""
import math
from math import pi, sin, cos, radians
import pyglet
import random
from pyglet.window.key import UP, DOWN, LEFT, RIGHT


window = pyglet.window.Window(1000,800)
#obrazek = pyglet.image.load("bigship.png")
#obrazek.anchor_x = obrazek.width //2
#obrazek.anchor_y = obrazek.height //2
#sprite = pyglet.sprite.Sprite(obrazek)
batch = pyglet.graphics.Batch()
class Ship(object):
    def __init__(self, x = None, y = None, direction = None, speed = None):
        self.image = pyglet.image.load("bigship.png")
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch = batch)
        self.speed = 50
        self.uhel = self.sprite.rotation
        self.x = 0
        self.y = 0
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.xx = 0
        self.yy = 0
    def tick(self, dt):
        self.sprite.x = self.sprite.x + self.speed*dt*math.sin(pi*self.uhel/180)
        self.sprite.y = self.sprite.y + self.speed*dt*math.cos(pi*self.uhel/180)
        self.sprite.rotation = self.uhel
        self.bounce()
        
        if self.xx:
            self.x += dt * self.speed * cos(pi/2-radians(self.uhel))
        else: 
            self.x -= dt * self.speed * cos(pi/2-radians(self.uhel))
        self.sprite.x = self.x
        if self.yy:
            self.y += dt * self.speed * sin(pi/2-radians(self.uhel))
        else: 
            self.y -= dt * self.speed * sin(pi/2-radians(self.uhel))
        self.sprite.y = self.y
       
        for sym in klavesy:
            if sym == UP:
                if self.speed > 500:
                    self.speed = 500
                else:
                    self.speed += 300*dt
            if sym == DOWN:
                if self.speed < 10:
                    self.speed = 0
                else:
                    self.speed -= 300*dt
            if sym == LEFT:
                self.uhel -= 3
                self.sprite.rotation -= 3
            if sym == RIGHT:
                self.uhel += 3
                self.sprite.rotation += 3
    
    def bounce(self):
        if (self.x + self.image.width / 2) >= window.width:
            self.xx = 0
        elif (self.x - self.image.width / 2) <= 0:
            self.xx = 1
            
        if (self.y + self.image.width / 2) >= window.height:
            self.yy = 0
        elif (self.y - self.image.width / 2) <= 0:
            self.yy = 1
        
    def skatulata(self, x, y):
        self.x += x
        self.y += y

klavesy = set()

class Strelec(object):
    def __init__(self, x = None, y = None, direction = None, speed = None):
        if x:
            self.x = x 
        else:
            self.x = random.randint(0, window.width)
        if y:
            self.y = x
        else:
            self.y = random.randint(0, window.height)
        if direction:
            self.direction = direction
        else:
            self.direction = random.randint(0,90)
        if speed:
             self.speed = speed
        else:
            self.speed = random.randint(10,50)
        self.image = pyglet.image.load("1.png")
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch = batch)
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.xx = random.randint(0,2)
        self.yy = random.randint(0,2)

    def tick(self, dt):
        self.bounce()
        if self.xx:
            self.x += dt * self.speed * cos(pi/2-radians(self.direction))
        else: self.x -= dt * self.speed * cos(pi/2-radians(self.direction))
        self.sprite.x = self.x
        if self.yy:
            self.y += dt * self.speed * sin(pi/2-radians(self.direction))
        else: self.y -= dt * self.speed * sin(pi/2-radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation += 0.05 * self.speed

    def skatulata(self, x, y):
        self.x += x
        self.y += y
        
        
    def bounce(self):
        if (self.x + self.image.width / 2) >= window.width:
            self.xx = 0
        elif (self.x - self.image.width / 2) <= 0:
            self.xx = 1
            
        if (self.y + self.image.width / 2) >= window.height:
            self.yy = 0
        elif (self.y - self.image.width / 2) <= 0:
            self.yy = 1

#class Meet():
    #meteors = []
    
    #def __init__ (self, count):
        #for _ in range(count):
            #self.add_meteor()
            
    #def add_meteor(self, dt = None):
        #self.meteors.append(Strelec())
    
    #def tick(self, dt):
        #for meteor in self.meteors:
            #meteor.tick(dt)
           
            
    
    
kamen = Strelec(10)
ship = Ship()
#meet = Meet(10)

@window.event
def on_key_press(sym,mod):
    global klavesy
    klavesy.add(sym)

@window.event
def on_key_release(sym,mod):
    global klavesy
    klavesy.remove(sym)
        
@window.event
def on_draw():
    window.clear()
    batch.draw()
    
    
pyglet.clock.schedule_interval(meet.tick, 1/1000000)    
pyglet.clock.schedule_interval(kamen.tick, 1/1000000)    
pyglet.clock.schedule_interval(ship.tick, 1/1000000)    
pyglet.app.run()
print('Hotovo!')




















