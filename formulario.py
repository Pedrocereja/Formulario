"""
Formulário 2 de ondas eletromagnéticas

Funções
-------
y(L, C, w, R=0, G=0) : Constante de propagação
Zo(L, C, w, R=0, G=0) : Impendância característica
Zin(Zl, Zo, B, l, a=0) : Impedância de entrada
Coef(Zl, Zo) : Coefs. de reflexão, transmissão e onda estacionária
"""

import cmath
		
def y(L, C, w, R = 0, G = 0):
	"""
	Constante de propagação
	
	Parâmetros
	----------
	L : Indutância
	C : Capacitância
	R : Resistência
	G : Condutância
	w : Frequência ângular(rad/s)
	
	Para um  meio sem perdas, R e G possuem valor padrão em 0
	
	Retorna a constante no formato cartesiano (alfa + jBeta)
	"""
	
	x = cmath.sqrt((R+w*L*1j)*(G+w*C*1j))
	
	print("Constante de atenuação (alfa): {:.3f}".format(x.real))
	print("Constante de fase (beta): {:.3f}".format(x.imag))
	absx = abs(x)
	phasex = cmath.phase(x) * 180 / cmath.pi
	print("Em coordenadas polares: " + "{:.3f}".format(absx) + " L" + "{:3f}".format(phasex))
	return x

def Zo(L, C, w, R = 0, G = 0):
	"""
	Impedância característica
	
	Parâmetros
	----------
	L : Indutância
	C : Capacitância
	w : Frequência ângular(rad/s)
	R : Resistência
	G : Condutância
	
	Para um  meio sem perdas, R e G possuem valor padrão em 0
	
	Retorna a impedância no formato cartesiano (alfa + jBeta)
	"""
	
	x = cmath.sqrt((R + w*L*1j)/(G + w*C*1j))

	print("Impedância característica :{:.3f}".format(x))
	absx = abs(x)
	phasex = cmath.phase(x) * 180 / cmath.pi
	print("Em coordenadas polares: " + "{:.3f}".format(absx) + " L" + "{:3f}".format(phasex))
	return x

def Zin(Zl, Zo, B, l, a=0):
	"""
	Impedância de entrada (Meios com ou sem perdas)
	
	Obs : Para meios sem perdas, o valor de a é definido em 0
	e pode ser deixado em branco
	
	Parâmetros
	----------
	Zl : Imp. característica do meio 2
	Zo : Imp. característica do meio 1
	B : Constante de fase da onda
	l : Distância do ponto de encontro entre os dois
	meios e o ponto de visão relativo da impedância
	a : Constante de atenuação da onda
	
	Retorna a impedância de entrada no formato cartesiano (alfa + jBeta)
	"""
	
	z = a +B*1j
	x = cmath.atanh(z*l)
	x = Zo*(Zl+Zo*x)/(Zo+Zl*x)
	
	print("Impedância de entrada : {:.3f}".format(x))
	absx = abs(x)
	phasex = cmath.phase(x) * 180 / cmath.pi()
	print("Em coordenadas polares: " + "{:.3f}".format(absx) + " L" + "{:3f}".format(phasex))
	return x

def Coef(Zl, Zo):
	"""
	Calcula os coeficientes do meio, imprimindo os coefs. de reflexão, transmissão e onda estacionária
	
	Parâmetros
	----------
	Zl : Imp. característica do meio 2
	Zo : Imp. característica do meio 1
	"""
	
	TAU = (Zl - Zo)/(Zl + Zo)
	tau = TAU + 1
	VSWR = (1+abs(TAU))/(1-abs(TAU))
	
	print("Coef. de reflexão (T): {:.3f}".format(TAU))
	print("Coef. de transmissão (tau): {:.3f}".format(tau))
	print("Coef. de onda estacionária (VSWR): {:.3f}".format(VSWR))

	
#testando
	
