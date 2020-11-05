import cmath
import inspect

def rectToPolar(x):
	absx = abs(x)
	phasex = cmath.phase(x) * 180 / cmath.pi
	return (absx, phasex) #Nada como código ruim pela manhã
	
def prettyPrint(x, computedValueName):
	tmp = rectToPolar(x)
	
	print(computedValueName[0] + ": {:.3f}".format(x.real), end="", flush=True)
	try:
		print(computedValueName[1] + ": {:.3f}".format(x.imag))
	except IndexError:
		print(": {:.3f}".format(x.imag))
		
	print("Em coordenadas polares: " + "{:.3f}".format(tmp[0]) + " L" + "{:3f}".format(tmp[1]))
