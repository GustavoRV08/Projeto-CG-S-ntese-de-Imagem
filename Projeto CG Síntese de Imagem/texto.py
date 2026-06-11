from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def afazeres():
  
  tarefas = ["Pegar Casaco",
        "Pegar Relogio",
        "Apagar a vela",
        "Pegar o machado",
        "Sair de Casa"
  ]
  
  y = 0.9

  for tarefa in tarefas:
        glColor3f(1, 1, 1)
        glRasterPos2f(-0.93, y)

        for char in tarefa:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

        y -= 0.08

