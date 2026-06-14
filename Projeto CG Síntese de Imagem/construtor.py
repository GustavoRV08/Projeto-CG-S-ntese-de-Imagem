import random

class Face:
  def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, textura):
      self.coordX = []
      self.coordY = []
      self.coordX.append(x1)
      self.coordX.append(x2)
      self.coordX.append(x3)
      self.coordX.append(x4)
      self.coordY.append(y1)
      self.coordY.append(y2)
      self.coordY.append(y3)
      self.coordY.append(y4)
      self.textura = textura
      self.visivel = True

  def get_menorX(self):
      return min(self.coordX)

  def get_maiorX(self):
      return max(self.coordX)

  def get_menorY(self):
      return min(self.coordY)

  def get_maiorY(self):
      return max(self.coordY)

numFundo = random.randrange(0, 2)
if numFundo == 0:
    fundo = Face(-1, 1, 1, 1, 1, -1, -1, -1, r"fundo1.jpg")
else:
    fundo = Face(-1, 1, 1, 1, 1, -1, -1, -1, r"fundo2.jpg")

faces = []
#porta:
if numFundo == 0:
    faces.append(Face(0.49, 0.58,
                     0.97, 0.58,
                     0.97, -0.72,
                     0.49, -0.72,
                     r"porta_trancada(vela_mesa).jpg"))
else:
    faces.append(Face(0.49, 0.58,
         0.97, 0.58,
         0.97, -0.72,
         0.49, -0.72,
         r"porta_trancada(vela_cadeira).jpg"))
    

#machados:
match random.randrange(0, 3):
    case 0:
        faces.append(Face(-0.48, 0.74, 
            0.04, 0.74, 
            0.04, 0.41, 
            -0.48, 0.41, 
            r"machado.jpg"))
    case 1:
        faces.append(Face(-1, -0.37, 
            -0.61, -0.37, 
            -0.61, -0.87, 
            -1, -0.87, 
            r"machado2.jpg"))
    case 2:
        faces.append(Face(-0.01, -0.56, 
            0.5, -0.56, 
            0.5, -0.89, 
            -0.01, -0.89, 
            r"machado3.jpg"))
        

#velas
if numFundo == 0:
    faces.append(Face(0.2, 0.36, 
        0.42, 0.36, 
        0.42, 0, 
        0.2, 0, r"velas(mesa).jpg"))
else:
    faces.append(Face(0.71, -0.44, 
        0.93, -0.44, 
        0.93, -0.80, 
        0.71, -0.80, 
        r"velas(cadeira).jpg"))
    

#Relógios:
match random.randrange(0, 3):
    case 0:
        faces.append(Face(-0.52, -0.08,
            -0.32, -0.08, 
            -0.32, -0.34, 
            -0.52, -0.34, 
            r"relogio.jpg"))
    case 1:
        faces.append(Face(-0.27, -0.70,
            -0.07, -0.70, 
            -0.07, -0.95, 
            -0.27, -0.95, 
            r"relogio2.jpg"))  
    case 2:
        faces.append(Face(-0.14, 0.27,
            0.07, 0.27, 
            0.07, 0, 
            -0.14, 0, 
            r"relogio3.jpg"))
    
# Casaco
faces.append(Face(-0.82, 0.94, 
                -0.53, 0.94, 
                -0.53, -0.05, 
                -0.82, -0.05, 
                r"casaco.jpg"))






        









def pegar_lista():
    global faces
    return faces

def pegar_fundo():
    global fundo
    return fundo
