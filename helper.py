import cmath

def rectToPolar(x):
	absx = abs(x)
	phasex = cmath.phase(x) * 180 / cmath.pi
	return (absx, phasex) #Nada como código ruim pela manhã
	
def prettyPrint(x):
	tmp = rectToPolar(x)
		
	print("Constante de atenuação (alfa): {:.3f}".format(x.real))
	print("Constante de fase (beta): {:.3f}".format(x.imag))
	
	print("Em coordenadas polares: " + "{:.3f}".format(tmp[0]) + " L" + "{:3f}".format(tmp[1]))

