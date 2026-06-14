#tentando implementar clique de mouse
import posix
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import numpy as np
from PIL import Image
import texto as texto
import construtor

largura_janela = 0
altura_janela = 0

faces = construtor.pegar_lista()
fundo = construtor.pegar_fundo()

def imprimir_face(face):
  texId = ler_textura(face.textura)
  gl.glEnable(gl.GL_TEXTURE_2D)
  gl.glBindTexture(gl.GL_TEXTURE_2D, texId)
  gl.glBegin(gl.GL_QUADS)
  gl.glTexCoord2f(0, 1, 0)
  gl.glVertex3f(face.coordX[0], face.coordY[0], 0)
  gl.glTexCoord2f(1, 1, 0)
  gl.glVertex3f(face.coordX[1], face.coordY[1], 0)
  gl.glTexCoord2f(1, 0, 0)
  gl.glVertex3f(face.coordX[2], face.coordY[2], 0)
  gl.glTexCoord2f(0, 0, 0)
  gl.glVertex3f(face.coordX[3], face.coordY[3], 0)
  gl.glEnd()
  gl.glDisable(gl.GL_TEXTURE_2D)

def verificar_clique(face, xMouse, yMouse):
  if ((face.get_menorX()*largura_janela/2)+(largura_janela/2))<xMouse<((face.get_maiorX()*largura_janela/2)+(largura_janela/2)) and altura_janela-((face.get_maiorY()*altura_janela/2)+altura_janela/2) <yMouse< altura_janela-((face.get_menorY()*altura_janela/2)+altura_janela/2):
    return True
  else:
    return False

def ler_textura(nome):
  img = Image.open(nome)
  img = img.transpose(Image.FLIP_TOP_BOTTOM)
  image_data = np.array(list(img.getdata()), np.uint8)
  gl.glEnable(gl.GL_TEXTURE_2D)
  idTex = gl.glGenTextures(1)
  gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
  gl.glBindTexture(gl.GL_TEXTURE_2D, idTex)


  gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_BORDER)
  gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_BORDER)
  # texture filtering params
  gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
  gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)

  gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, img.size[0], img.size[1], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, image_data)
  gl.glTexEnvi(gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE , gl.GL_DECAL)
  return idTex

def mouse(botao, estado, x, y):
  if botao == glut.GLUT_LEFT_BUTTON and estado == glut.GLUT_DOWN:
    for i in range(len(faces)):
      if verificar_clique(faces[i], x, y) and i == len(texto.tarefas) and len(faces):
        faces.pop(i)
        if len(texto.tarefas) != 0:
            texto.tarefas.pop()
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    imprimir_face(fundo)
    for i in range(len(faces)):
      if faces[i].textura != None:
        imprimir_face(faces[i])
    texto.afazeres()
    print(f"len faces: {len(faces)}")
    if len(faces) == 0:
        glut.glutLeaveMainLoop()
    glut.glutSwapBuffers()


def resize(largura, altura):
  global altura_janela
  global largura_janela
  altura_janela = altura
  largura_janela = largura
  gl.glViewport(0, 0, largura, altura)
  gl.glLoadIdentity()

def display():
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glShadeModel(gl.GL_FLAT)
  imprimir_face(fundo)
  for i in range(len(faces)):
    if faces[i].textura != None:
        imprimir_face(faces[i])
  texto.afazeres()
  glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow('Crime e Castigo')
glut.glutReshapeWindow(1080, 810) #720, 540
glut.glutDisplayFunc(display)
glut.glutReshapeFunc(resize)
glut.glutMouseFunc(mouse)
glut.glutMainLoop()


#explicação do if que funcionou:
#(([menor valor de x do objeto]*largura_janela/2)+(largura_janela/2))<x<(([maior valor de x do objeto]*largura_janela/2)+(largura_janela/2)) and altura_janela-(([maior valor de y do objeto]*altura_janela/2)+altura_janela/2) <y< altura_janela-(([menor valor de y do objeto]*altura_janela/2)+altura_janela/2)
#OBS: essa conta provavelmente não funciona muito bem com formas que não sejam quadrados (vai ter como clicar em espaços vazios e ainda assim ativar a ação do objeto e coisas do gênero)
