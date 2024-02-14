

class ContaBancaria:


	def __init__(self, nome, numero):
		self.nome = nome
		self.numero = numero
		self.saldo = 0.0
		
		
	def saca(self, qto):
		if self.saldo >= qto:
			self.saldo -= qto
			return True
		return False
	
	def deposita(self, qto):
		self.saldo += qto
		

class ContaEspecial(ContaBancaria):
	
	def __init__(self, nome, numero, limite):
		super().__init__(nome, numero)
		self.limite = limite
		
	def saca(self, qto):
		if self.saldo + self.limite >= qto:
			self.saldo -= qto
			return True
		return False
			

class ContaPoupanca(ContaBancaria):
	
	
	def __init__(self, nome, numero, dia):
		super().__init__(nome, numero)
		self.vencimento = dia
		
		
	def atualiza(self, taxa):
		self.saldo *= 1.0 + taxa
		

