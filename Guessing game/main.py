import random

class Advinha:
    def __init__(self,n):
      self.n = n;
      self.min = 0;
      self.max = n;
      self.ultimo_palpite = None;

    def palpite(self):
      if self.ultimo_palpite is None:
        #Primeira tentativa: chute um número aleatório entre 0 e N;  
        self.ultimo_palpite= random.randint(self.min, self.max);
      else:
        #Tentativas subsequentes: chute o número no meio do intervalo restante
        self.ultimo_palpite = (self.min + self.max) // 2
      
      return self.ultimo_palpite

      def update(self, result):
        if result == "menor":
          self.max = self.ultimo_palpite - 1
        elif result == "maior":
          self.min = self.ultimo_palpite + 1

      def play(self):
        result = None
        while result != "acertou":
          palpite = self.palpite()
          result = input(f"O número é {palpite}? (responda 'maior', 'menor', ou 'acertou'): ")
          self.update(result)
        print("Eu acertei")  

jogo = Advinha(10)
jogo.play()