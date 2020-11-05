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
		if(x.imag > 0):
			print(computedValueName[1] + ": +j{:.3f}".format(x.imag))
		else:
			print(computedValueName[1] + ": -j{:.3f}".format(x.imag))
	except IndexError:
		if(x.imag > 0):
			print(" +j{:.3f}".format(x.imag))
		else:
			print(" -j{:.3f}".format(x.imag))
		
	print("Em coordenadas polares: " + "{:.3f}".format(tmp[0]) + " L" + "{:3f}".format(tmp[1]))
