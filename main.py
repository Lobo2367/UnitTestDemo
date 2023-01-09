#Declaraciones Obj y Func

class Caso:

  ID = int
  nombre = str
  fecha = str
  descripcion = str

  def __init__(self, n, f, d):
    self.ID = int
    self.nombre = n
    self.fecha = f
    self.descripcion = d


def main():
  insertID()
  insertnombre()
  insertdesc()
  insertfecha()


def insertID():
  ID = str
  ID = str(caso.nombre[0:2] + str(caso.fecha[0:2]))
  print(type(ID))
  return ID
def insertnombre(name):
  caso.nombre = name

def insertfecha(fecha):
  caso.fecha = fecha

def insertdesc(desc):
  caso.descripcion = desc





#Instancia de Prueba
caso = Caso("JGF", "200702", "Ok")

#Llamado Funcion
insertID()