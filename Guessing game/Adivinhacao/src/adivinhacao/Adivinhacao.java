/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package adivinhacao;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author Bárbara
 */
public class Adivinhacao {
    
    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       System.out.print("Digite um valor maximo de N: ");
       int n = scanner.nextInt();
       Random random = new Random();
       int numeroAleatorio = random.nextInt(n +1);
       int tentativas = 0;
       int chute;
       do{
           System.out.print("Adivinhe o número entre 0 e " + n + ": ");
           chute = scanner.nextInt();
           if(chute > numeroAleatorio){
               System.out.println("O número é menor.");
           } else if (chute < numeroAleatorio){
               System.out.println("O número é maior");
           }
           tentativas++;
       }while( chute != numeroAleatorio);
       System.out.println("Parabéns, você acertou em " + tentativas + " tentativas!");
    }
    
}
