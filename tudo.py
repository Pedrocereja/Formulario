import formulario as f
import helper
import math #cmath.pow() não deu muito boa, por alguma razão.
from onda import Onda #lol


#valores quaisquer, esse é do exercício 1
L = 0.2 * math.pow(10, -6) #Indutância [H/m]
C = 100 * math.pow(10, -12) #Capacitância [F/m]
w = math.pow(10, 8) #Velocidade radial [rad/s]
R = 0.1 #Resistência [Ohm/m]
G = 10 * math.pow(10, -6) #Condutividade [S/m]
Zl = 1 #Impedância característica do meio 2
l = 0.02 #distância entre os meios
A = 2 #amplitude da onda

intrinsicImpedance = f.Zo(0.2 * math.pow(10, -6), 100 * math.pow(10, -12), math.pow(10, 8), 0.1, 10 * math.pow(10, -6))

waveConstants = f.y(0.2 * math.pow(10, -6), 100 * math.pow(10, -12), math.pow(10, 8), 0.1, 10 * math.pow(10, -6))

onda = Onda(A, w, waveConstants[0], waveConstants[1])

print("Amplitude: " + str(onda.amplitude))
print("Velocidade radial: " + str(onda.w))
print("Comprimento de onda: " + str(onda.lambd))
print("Velocidade de fase: " + str(onda.Vf))

inputImpedance = f.Zin(Zl, intrinsicImpedance, waveConstants[1], l, waveConstants[0])
mediumCoefficients = f.Coef(Zl, intrinsicImpedance)
