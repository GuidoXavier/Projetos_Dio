package com.mycompany.contabanco;

import java.util.Scanner;

public class ContaTerminal {

    public int numero;
    public String agencia;
    public String nome;
    public double saldo;

    public void dados() {
    Scanner leia = new Scanner(System.in);
    
    System.out.println("Qual a sua Agencia?");
    agencia = leia.nextLine();
    
    System.out.println("Qual o número de sua conta?");
    numero = leia.nextInt();
    leia.nextLine(); // As vezes o leia nextInt consome o próximo comando, então fiz isso para corrigir o erro//
    
    System.out.println("Qual seu nome?");
    nome = leia.nextLine();
    
    System.out.println("Qual seu saldo?");
    saldo = leia.nextDouble();
    welcome();
}


    public void welcome() {

        System.out.printf("Olá %s.\n"
                + "obrigado por criar uma conta em nosso banco, sua agência é %s, "
                + "conta %d e seu saldo %.2f já está disponível para saque", nome, agencia, numero, saldo);

    }

    public static void main(String[] args) {
        ContaTerminal iniciar = new ContaTerminal();
        iniciar.dados();
    }

}
