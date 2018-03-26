from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    #glOrtho(-10,10,-10,10,-10,10) ##2d##
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def draw_chair(x,y,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(x, y, z)
    glScale(2, 2, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def draw_chair1(x,y,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(x, y, z)
    glScale(2.5, .5, 2)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()


def leg(x,y,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(x, y, z)
    glScale(.5, 2, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def draw_cube():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    draw_chair(4,1,1)
    draw_chair(-4.5,0,0)


    draw_chair1(2,-5,-.5)
    draw_chair1(-8,-5.5,-1)

    leg(2,-3.5,.5)
    leg(5.5,-3.5,.5)
    leg(5.5,-3.5,3)
    leg(2.5,-3.5,3)

    leg(-5,-4,0)
    leg(-5,-4,2.5)
    leg(-3,-4,2.5)
    leg(-3,-4,0.5)




    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)

glutCreateWindow(b"Sec6")
glutDisplayFunc(draw_cube)
glutIdleFunc(draw_cube)
myinit()
glutMainLoop()
