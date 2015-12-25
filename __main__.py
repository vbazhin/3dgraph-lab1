#import mpl_triangulation
#from sympy.geometry import *
import pprint
import math
#findCenter-> Intersect -> Division->  choosePlane-> BSPTree


class Vertex(object):
    __slots__ = ('x', 'y', 'z')
    def __init__ (self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
class HPlane(object):
    __slots__ = ('A', 'B', 'C', 'D')
    def __init__ (self, A=0.0, B=0.0, C=0.0, D=0.0):
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)
        self.D = float(D)
class Poligon(object):
    __slots__ = ('D1', 'D2', 'D3')
    def __init__(self, points):
        self.D1 = Vertex(points[0][0], points[0][1], points[0][2])
        self.D2 = Vertex(points[1][0], points[1][1], points[1][2])
        self.D2 = Vertex(points[2][0], points[2][1], points[2][2])
def sign(param):
    if param >= 0:
        return 1
    else:
        return 0

def findCenter(pList):
    center = {}
    for z in range(3):
        center[z] = 0
        for y in range(3):
            for x in range(len(pList)):
                '''суммируем все координаты сначала по x, потом по у, потом по z'''
                center[z] += pList[x][y][z]
        '''формируем усредненную координату всех вершин полигонов'''
        center[z] /= (3*len(pList))
    return center

'''сверху от плоскости - положительное расстояние, снизу - отрицательное '''
def findDistance(vertex, hPlane):
    t = 1/math.sqrt(pow(hPlane.A,2) + pow(hPlane.B,2) + pow(hPlane.C,2))
    distance = t * (hPlane.A*vertex.x + hPlane.B*vertex.y + hPlane.C*vertex.z + hPlane.D)
    return distance

def findIntersection(v1, v2, hPlane):
    num = -(hPlane.D + hPlane.A*v1.x + hPlane.B*v1.y + hPlane.C*v1.z)
    denom = hPlane.A*(v2.x-v1.x) + hPlane.B*(v2.y-v1.y) + hPlane.C*(v2.z-v1.z)
    t = num/denom
    if t<1 and t>0:
        x = v1.x + t*(v2.x-v1.x)
        y = v1.y + t*(v2.y-v1.y)
        z = v1.z + t*(v2.z-v1.z)
        return [x, y, z]
    else:
        return False
    #http://youclever.org/book/koordinaty-i-vektory-2
'''возвращает 2 или 3 полигона'''
def intersect(poligon, hPlane, pList):
    # проверяем случай разбиения на 2 полигона: если одна из точек принадлежит секущей
    if hPlane.D == -(hPlane.A*poligon.D1.x + hPlane.B*poligon.D1.y + hPlane.C*poligon.D1.z):
        pass
    elif hPlane.D == -(hPlane.A*poligon.D2.x + hPlane.B*poligon.D2.y + hPlane.C*poligon.D2.z):
        pass
    elif hPlane.D == -(hPlane.A*poligon.D3.x + hPlane.B*poligon.D3.y + hPlane.C*poligon.D3.z):
        pass


    # TODO Реализовать нахождение точки пересечения

    # иначе разбиваем на 3 полигона
    # находим тот единственный отрезок, не пересекаемый секущей, знак расстояний до секущей должны быть одинаковыми
    if sign(findDistance(poligon.D1, hPlane)) ==  sign(findDistance(poligon.D2, hPlane)):
        pass
    elif sign(findDistance(poligon.D2, hPlane)) ==  sign(findDistance(poligon.D3, hPlane)):
        pass
    else:
        pass

    pass

def division(pList, hPlane):
    pass

def choosePlane(pList):
    pass

def BSPTree(pList):
    pass


if __name__ == '__main__':
    # pList = mpl_triangulation.Polygons().create_triangles(plot=False)
    pList = [[[0.010703950112349703, 0.31750267022044021, 0.044739447260041976],
  [0.61545986162699373, 0.031921025441535633, 0.61046017478947368],
  [0.46970634241017262, 0.56238191601151766, 0.75962217347960725]],
 [[0.46970634241017262, 0.56238191601151766, 0.75962217347960725],
  [0.61545986162699373, 0.031921025441535633, 0.61046017478947368],
  [0.9050056709480313, 0.43199599017510792, 0.71627976004189076]],
 [[0.010703950112349703, 0.31750267022044021, 0.044739447260041976],
  [0.46970634241017262, 0.56238191601151766, 0.75962217347960725],
  [0.19327776718003142, 0.60127546357017791, 0.17020415394927624]],
 [[0.68137975038977416, 0.8078251531730366, 0.73276826612932977],
  [0.46970634241017262, 0.56238191601151766, 0.75962217347960725],
  [0.9050056709480313, 0.43199599017510792, 0.71627976004189076]],
 [[0.42223405563448124, 0.82102388311800656, 0.29936107695056402],
  [0.19327776718003142, 0.60127546357017791, 0.17020415394927624],
  [0.46970634241017262, 0.56238191601151766, 0.75962217347960725]],
 [[0.42223405563448124, 0.82102388311800656, 0.29936107695056402],
  [0.68137975038977416, 0.8078251531730366, 0.73276826612932977],
  [0.65386064305624791, 0.99638736192784427, 0.066331301696641032]],
 [[0.46970634241017262, 0.56238191601151766, 0.75962217347960725],
  [0.68137975038977416, 0.8078251531730366, 0.73276826612932977],
  [0.42223405563448124, 0.82102388311800656, 0.29936107695056402]],
 [[0.77586545375539373, 0.88561892784689311, 0.0038377191544501921],
  [0.68137975038977416, 0.8078251531730366, 0.73276826612932977],
  [0.9050056709480313, 0.43199599017510792, 0.71627976004189076]],
 [[0.65386064305624791, 0.99638736192784427, 0.066331301696641032],
  [0.68137975038977416, 0.8078251531730366, 0.73276826612932977],
  [0.70603836459742109, 0.93207750158170011, 0.6054971963174709]],
 [[0.70603836459742109, 0.93207750158170011, 0.6054971963174709],
  [0.77586545375539373, 0.88561892784689311, 0.0038377191544501921],
  [0.65386064305624791, 0.99638736192784427, 0.066331301696641032]],
 [[0.68137975038977416, 0.8078251531730366, 0.73276826612932977],
  [0.77586545375539373, 0.88561892784689311, 0.0038377191544501921],
  [0.70603836459742109, 0.93207750158170011, 0.6054971963174709]]]
    pprint.pprint(findCenter(pList))
    v = Vertex(4,3,1)
    hp = HPlane(-1,-2,1,5)
    v1 = Vertex(0.5,0.5,0)
    v2 = Vertex(7,0.5,0)
    pprint.pprint(findDistance(v1, hp))
    pprint.pprint(findDistance(v2, hp))
    print(findIntersection(v1,v2,hp))