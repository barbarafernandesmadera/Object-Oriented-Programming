import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.HashMap;
import java.util.Iterator;

public class Contas implements Serializable {

	private HashMap<Integer,ContaBancaria> contas = new HashMap<Integer,ContaBancaria>();
	
	public static void main(String[] args) throws Exception {
		int op = 0;
		Contas ct = null;
		try {
			FileInputStream fis = new FileInputStream("contas.dat");     
			ObjectInputStream ois = new ObjectInputStream(fis);
			ct = (Contas) ois.readObject();
			ois.close();
		}
		catch (Exception e)
		{
		   ct = new Contas();
		}
		
		while (op != 8) {
			op = leOpcao();
			switch (op)
			{
			case 1: 
				System.out.println("Nome do correntista: ");
				String s = EntradaTeclado.leString();
				System.out.println("Dia de vencimento: ");
				int dia = EntradaTeclado.leInt();
				ContaPoupanca cp = new PoupancaOuro(s, dia);
				ct.add(cp);
				System.out.println("************ Conta criada.**************");
				break;
				
			case 2: 
				System.out.println("Nome do correntista: ");
				s = EntradaTeclado.leString();
				System.out.println("Dia de vencimento: ");
				dia = EntradaTeclado.leInt();
				cp = new PoupancaSimples(s, dia);
				ct.add(cp);
				System.out.println("************ Conta criada.**************");
				break;

			case 3: 
				System.out.println("Nome do correntista: ");
				s = EntradaTeclado.leString();
				System.out.println("Limite de saque: ");
				double limite = EntradaTeclado.leDouble();
				ContaEspecial ce = new ContaEspecial(s, limite);
				ct.add(ce);
				System.out.println("************ Conta criada.**************");
				break;
			case 4:
				System.out.println("Numero da conta: ");
				int conta = EntradaTeclado.leInt();
				System.out.println("Valor a sacar: ");
				double valor = EntradaTeclado.leDouble();
				ContaBancaria cb = ct.procura(conta);
				if ( cb == null )
				{
					System.out.println("************* Conta não existe **************");
					break;
				}
				try {
					cb.saca(valor);
					System.out.println("****************** Saque realizado ***********");
				}
				catch (Exception e)
				{
					System.out.println("****************** Saque não realizado ***********");
					System.out.println(e.getMessage());
				}
				break;
			case 5:
				System.out.println("Numero da conta: ");
				conta = EntradaTeclado.leInt();
				System.out.println("Valor a depositar: ");
				valor = EntradaTeclado.leDouble();
				cb = ct.procura(conta);
				if ( cb == null )
				{
					System.out.println("************* Conta não existe **************");
					break;
				}
				cb.deposita(valor);
				System.out.println("****************** Depósito realizado ***********");
				break;
			case 7: 
				ct.printSaldos();
				break;
			case 6:
				System.out.println("Qual o valor da taxa? ");
				double tx = EntradaTeclado.leDouble();
				ct.atualizaPoupança(tx);
				System.out.println("Saldos atualizados");
				break;
			}
			System.out.println("Digite ENTER para continuar");
			EntradaTeclado.leString();
			System.out.println("\n\n");
		}
		FileOutputStream fos = new FileOutputStream("contas.dat");
		ObjectOutputStream oos = new ObjectOutputStream(fos);
		oos.writeObject(ct);
		oos.close();
	}

	private static int leOpcao() {
        System.out.println("1) Criar poupança especial\n2) Criar poupança simples\n3) Criar conta especial\n4) Realizar saque\n5) Realizar deposito\n"
        		+ "6) Atualizar poupanças\n7) Mostrar saldos\n8) Sair");
        int k = -1;
        while (true)
        {
        	System.out.println("Digite a opção desejada ===> ");
        	try {
        		k = EntradaTeclado.leInt();
        		if ( k > 0 && k <= 8 )
        			return k;
        	}
        	catch (Exception e) {
        		;
        	}
        }
	}

	private void add(ContaBancaria cb) {
		contas.put(cb.getNumConta(), cb);		
	}
	
	private void printSaldos() {
		for (ContaBancaria ctb : contas.values())
		{
			System.out.println("Numero da conta:" + ctb.getNumConta());
			System.out.println("Titular: " + ctb.getNomeCliente());
			System.out.println("Saldo: " + ctb.getSaldo());
			System.out.println();
		}

	}

	private void atualizaPoupança(double tx) {
		Iterator<ContaBancaria> it = contas.values().iterator();
		while  (it.hasNext())
		{
			ContaBancaria ctb = it.next();
			ctb.atualiza(tx);
		}
	}

	private ContaBancaria procura(int conta) {
		return contas.get(conta);
	}

}
