from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
x=0
f=True
z=0

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def draw():
    ###road###


    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global f
    global z
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    ##########################################
    glColor3f(0.6,0.6,0.6)
    glTranslate(0,0,0)
    glScale(50,1,2)
    glutSolidCube(5)


########################################################3
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(x,0,0)
    glScale(1,.25,.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(0,1.25,0)
    glScale(.5,.25,.5)
    glutWireCube(5)

    glColor(0,0,1)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.5,1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(-2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(-2,-.5,1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutWireTorus(.125,.5,12,8)

    glColor(0,0,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.3,.4)
    glutSolidSphere(.3,20,20)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.3,-.4)
    glutSolidSphere(.3,20,20)



    if x > 7:
      f = False

    if x < -14:
        f = True

    if f:
        x+=.001
        z-=1
    else:
        x-=.001
        z+=1




    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"3rabety")
myinit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
