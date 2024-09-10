#Adición de vectores complejos
import numpy as np

v1 = np.array([1+2j, 3+4j, 5+6j])
v2 = np.array([6+5j, 4+3j, 2+1j])
sumaVectores = v1 + v2
print(sumaVectores)

#Inverso (aditivo) de un vector complejo
inversoAditivo = -v1
print(inversoAditivo)

#Multiplicación de un escalar por un vector complejo
escalar = 2 + 3j
multiplicacionEscalarVector = escalar * v1
print(multiplicacionEscalarVector)

#Adición de matrices complejas
m1 = np.array([[1+2j, 3+4j], [5+6j, 7+8j]])
m2 = np.array([[8+7j, 6+5j], [4+3j, 2+1j]])
sumaMatrices = m1 + m2
print(sumaMatrices)

#Inversa (aditiva) de una matriz compleja
inversaAditivaMatriz = -m1
print(inversaAditivaMatriz)

#Multiplicación de un escalar por una matriz compleja
multiplicacionEscalarMatriz = escalar * m1
print(multiplicacionEscalarMatriz)

#Transpuesta de una matriz/vector
transpuestaVector = v1.T
transpuestaMatriz = m1.T
print(transpuestaVector)
print(transpuestaMatriz)

#Conjugada de una matriz/vector
conjugadaVector = np.conj(v1)
conjugadaMatriz = np.conj(m1)
print(conjugadaVector)
print(conjugadaMatriz)

#Adjunta (daga) de una matriz/vector
adjuntaVector = np.conj(v1).T
adjuntaMatriz = np.conj(m1).T
print(adjuntaVector)
print(adjuntaMatriz)

#Producto de dos matrices (de tamaños compatibles)
m3 = np.array([[1+1j, 2+2j], [3+3j, 4+4j]])
m4 = np.array([[5+5j, 6+6j], [7+7j, 8+8j]])
productoMatrices = np.dot(m3, m4)
print(productoMatrices)

#Función para calcular la “acción” de una matriz sobre un vector
accionMatrizVector = np.dot(m1, v1[:2])
print(accionMatrizVector)

#Producto interno de dos vectores
productoInterno = np.vdot(v1, v2)
print(productoInterno)

#Norma de un vector
normaVector = np.linalg.norm(v1)
print(normaVector)

#Distancia entre dos vectores
distanciaVectores = np.linalg.norm(v1 - v2)
print(distanciaVectores)

#Valores y vectores propios de una matriz
valoresPropios, vectoresPropios = np.linalg.eig(m1)
print(valoresPropios)
print(vectoresPropios)

#Revisar si una matriz es unitaria
def esUnitaria(matriz):
    identidad = np.eye(matriz.shape[0])
    return np.allclose(np.dot(matriz, np.conj(matriz).T), identidad)

print(esUnitaria(m1))

#Revisar si una matriz es Hermitiana
def esHermitiana(matriz):
    return np.allclose(matriz, np.conj(matriz).T)

print(esHermitiana(m1))

#Producto tensor de dos matrices/vectores
productoTensor = np.kron(m1, m2)
print(productoTensor)












