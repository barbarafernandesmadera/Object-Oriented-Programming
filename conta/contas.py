from conta import ContaEspecial, ContaPoupanca


class Contas:
	
	def __init__(self):
		self.contas_P = []
		self.contas_E = []
		
	
	
	def le_opcao(self):
		print('''1) Criar poupança\n2) Criar conta especial\n3) Realizar saque\n4) Realizar deposito\n\
5) Atualizar poupanças\n6) Mostrar saldos\n7) Sair''')
		while (True):
			k = int(input('Digite a opção desejada ===> '))
			if k >0 and k < 8:
				return k
		
		
	def add_E(self, conta):
		if not self.procura_E(conta.numero):
			self.contas_E.append(conta)
		
	def add_P(self, conta):
		if not self.procura_E(conta.numero):
			self.contas_P.append(conta)
		
		
	def procura_E(self, numero):
		for r in self.contas_E:
			if r.numero == numero:
				return r
		return None
		
	def procura_P(self, numero):
		for r in self.contas_P:
			if r.numero == numero:
				return r
		return None

	def printSaldos(self):
		for ctb in self.contas_P:
			print("Numero da conta poupança: {}".format(ctb.numero))
			print("Titular: {}".format(ctb.nome))
			print("Vencimento: {}".format(ctb.vencimento))
			print("Saldo: {}\n".format(ctb.saldo))

		for ctb in self.contas_E:
			print("Numero da conta especial: {}".format(ctb.numero))
			print("Titular: {}".format(ctb.nome))
			print("Limite: {}".format(ctb.limite))
			print("Saldo: {}\n".format(ctb.saldo))

	def atualiza_P(self, tx):
		for ctb in self.contas_P:
			ctb.atualiza(tx)


if __name__ == '__main__':
	op = 0
	ct = Contas()

	while True:
		op = ct.le_opcao()
		if op == 1: 
			conta = int(input("Numero da conta: "))
			s = input("Nome do correntista: ")
			dia = int(input("Dia de vencimento: "))
			cp = ContaPoupanca(s, conta, dia)
			ct.add_P(cp);
			print("************ Conta criada.**************")

		elif op == 2: 
			conta = int(input("Numero da conta: "))
			s = input("Nome do correntista: ")
			limite = float(input("Limite de saque: "))
			cp = ContaEspecial(s, conta, limite)
			ct.add_E(cp);
			print("************ Conta criada.**************")
		elif op == 3:
			conta = int(input("Numero da conta: "))
			valor = float(input("Valor a depositar: "))
			cp = ct.procura_P(conta);
			if cp != None:
				if 	cp.saca(valor):
					print("****************** Saque realizado ***********")
				else:
					print("****************** Saque não realizado ***********")
			else:
				ce = ct.procura_E(conta);
				if ce == None:
					print("************* Conta não existe **************")
				else:
					if 	ce.saca(valor):
						print("****************** Saque realizado ***********")
					else:
						print("****************** Saque não realizado ***********")
		elif op == 4:
			conta = int(input("Numero da conta: "))
			valor = float(input("Valor a sacar: "))
			cp = ct.procura_P(conta);
			if cp != None:
				cp.deposita(valor)
				print("****************** Depósito realizado ***********")
			else:
				ce = ct.procura_E(conta);
				if ce == None:
					print("************* Conta não existe **************")
				else:
					ce.deposita(valor)
					print("****************** Depósito realizado ***********")
		elif op == 6: 
			ct.printSaldos();
		elif op == 5:
			tx = float(input("Qual o valor da taxa? "))
			ct.atualiza_P(tx);
			print("Saldos atualizados");
		elif op == 7:
			print("Terminando o programa....")
			break;
		input("Digite ENTER para continuar")
		print("\n\n")




