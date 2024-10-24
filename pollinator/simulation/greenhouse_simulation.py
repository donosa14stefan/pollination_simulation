import pygame
from pygame.math import Vector3
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# Inițializare Pygame și OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Setări OpenGL
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

# Setări cameră
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

class Plant:
    def __init__(self, position, height, leaf_count, flower_count, fruit_count=0, growth_stage='mature'):
        self.position = Vector3(position)
        self.height = height
        self.leaf_count = leaf_count
        self.flower_count = flower_count
        self.fruit_count = fruit_count
        self.growth_stage = growth_stage

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        
        # Desenează tulpina
        glColor3f(0.0, 0.5, 0.0)
        self.draw_cylinder(0.05, self.height, 10)
        
        # Desenează frunze
        glColor3f(0.0, 0.8, 0.0)
        for i in range(self.leaf_count):
            glPushMatrix()
            angle = (i / self.leaf_count) * 2 * math.pi
            glTranslatef(0.1 * math.cos(angle), 0.1 * math.sin(angle), (i / self.leaf_count) * self.height)
            glRotatef(random.uniform(0, 45), 1, 0, 0)
            glRotatef(angle * (180 / math.pi), 0, 0, 1)
            self.draw_leaf(0.2, 0.1)
            glPopMatrix()
        
        # Desenează flori
        glColor3f(1.0, 0.5, 0.5)
        for i in range(self.flower_count):
            glPushMatrix()
            angle = (i / self.flower_count) * 2 * math.pi
            glTranslatef(0.15 * math.cos(angle), 0.15 * math.sin(angle), self.height * 0.8 + 0.1)
            self.draw_sphere(0.1, 10, 10)
            glPopMatrix()
        
        # Desenează fructe
        glColor3f(1.0, 0.0, 0.0)
        for i in range(self.fruit_count):
            glPushMatrix()
            angle = (i / self.fruit_count) * 2 * math.pi
            glTranslatef(0.2 * math.cos(angle), 0.2 * math.sin(angle), self.height * 0.6 + 0.1)
            if self.name == "Tomato":
                self.draw_sphere(0.15, 10, 10)
            elif self.name == "Cucumber ":
                self.draw_cylinder(0.05, 0.3, 10)
            elif self.name == "Bell Pepper":
                self.draw_cone(0.1, 0.05, 0.2, 10, 10)
            elif self.name == "Strawberry":
                self.draw_cone(0.08, 0.05, 0.1, 10, 10)
            glPopMatrix()
        
        glPopMatrix()

    def draw_cylinder(self, radius, height, slices):
        glBegin(GL_QUAD_STRIP)
        for i in range(slices + 1):
            angle = 2 * math.pi * i / slices
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex3f(x, y, 0)
            glVertex3f(x, y, height)
        glEnd()

    def draw_leaf(self, length, width):
        glBegin(GL_TRIANGLES)
        glVertex3f(0, 0, 0)
        glVertex3f(length, width/2, 0)
        glVertex3f(length, -width/2, 0)
        glEnd()

    def draw_sphere(self, radius, slices, stacks):
        quad = gluNewQuadric()
        gluSphere(quad, radius, slices, stacks)

    def draw_cone(self, radius1, radius2, height, slices, stacks):
        quad = gluNewQuadric()
        gluCylinder(quad, radius1, radius2, height, slices, stacks)

# Creează plantele
plants = [
    Plant(Vector3(0, 0, 0), 1.5, 10, 5, 3, 'mature', "Tomato"),
    Plant(Vector3(2, 0, 0), 2.0, 15, 1, 2, 'young', "Cucumber"),
    Plant(Vector3(4, 0, 0), 1.2, 8, 3, 1, 'seedling', "Bell Pepper"),
    Plant(Vector3(6, 0, 0), 0.8, 6, 1, 0, 'mature', "Basil"),
    Plant(Vector3(8, 0, 0), 0.5, 4, 1, 2, 'young', "Strawberry")
]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Desenează plantele
    for plant in plants:
        plant.draw()

    pygame.display.flip()
    pygame.time.wait(10)
