from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

tarefas = [
      "Já está tudo pronto, agora é só não olhar para trás",
      "Essa será minha última conversa com aquela agiota",
      "Houve um incêndio no centro recentemente, foi uma tragédia",
      "Eu odeio pessoas que se atrasam, elas não se importam com o tempo de vida dos outros",
      "Tive um resfriado muito forte semana passada, não quero ter outro"
  ]

def afazeres():
  global tarefas

  y = 0.9

  glColor3f(1, 1, 1)
  glRasterPos2f(-0.93, y)

  if len(tarefas) > 0:
    for char in tarefas[-1]:
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
  else:
    for char in "SEJA NAPOLEÃO!":
          glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))



def proxima_tarefa():
  global tarefa_atual
  tarefa_atual += 1
  if tarefa_atual >= len(tarefas):
    tarefa_atual = 0

tarefas = [
      "Já está tudo pronto, agora é só não olhar para trás",
      "Essa será minha última conversa com aquela agiota",
      "Houve um incêndio no centro recentemente, foi uma tragédia",
      "Pessoas que se atrasam não se importam com o tempo de vida dos outros",
      "Tive um resfriado muito forte semana passada, não quero ter outro"
  ]
