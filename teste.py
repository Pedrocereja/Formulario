class Onda:
	"""
	Uma onda plana uniforme se propagando no sentido positivo de z
	
	Parâmetros
	----------
	Vo : Valor máximo
	w : Frequência(rad/s)
	a : Constante de atenuação(Np/m)
	B : Constante de fase(rad/m)
	
	Atributos
	---------
	Vo : Valor máximo
	w : Frequência(rad/s)
	a : Constante de atenuação(Np/m)
	B : Constante de fase(rad/m)
	lambd : Comprimento de onda(m)
	Vf = Velocidade da frente de onda(m/s)
	"""
	
	def __init__(self, Vo, w, a, B):
		self.Vo = Vo
		self.w = w
		self.a = a
		self.B = B
		self.lambd = 2*cmath.pi*B
		self.Vf = w/B
		
	def Valor(self, z, t):
		"""
		Valor da onda em um dado instante no tempo e espaço
	
		Parâmetros
		----------
		z : Posição no eixo z
		t : Tempo
		"""
		
		x = self.Vo*cmath.exp(-self.a*z)*cmath.cos(self.w*t-self.B*z)
		return x