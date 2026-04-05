package DesafioRaphael.atvPainelPet;

import java.io.IOException;
import java.util.Scanner;

public class window {
	public static void main(String[] args) throws InterruptedException, IOException {
		windowIndex();
	}
// ------------------------------------------------------------------------------------------------------
	public static void windowIndex() throws InterruptedException, IOException {
		process.clearTerminal();
		Scanner in = new Scanner(System.in);
		while(true) {
			System.out.println("---------- Welcome PetShop ----------");
			System.out.println("(1) - Cadastrar pessoa");
			System.out.println("(2) - cadastrar pet");
			System.out.println("(3) - Encerrar programa");
			System.out.println("");
			System.out.print("Digite sua escolha: ");
			int escolha = in.nextInt();
			
			if(escolha == 1) {
				windowPerson();
			}else if(escolha == 2){
				windowPet();
			}else{
				process.killProcess();
				break;
			}
			
		}	
	}
// ------------------------------------------------------------------------------------------------------
	public static void windowPerson() throws InterruptedException, IOException {
		process.clearTerminal();
		
		Scanner in = new Scanner(System.in);
		while(true) {
			System.out.println("---------- Cadastro da pessoa ----------");
			System.out.print("Cadastrar nome: ");
			String nome = in.next();
			
			System.out.print("Cadastrar telefone: ");
			String tel = in.next();
			
			System.out.print("Cadastrar endereço: ");
			String address = in.next();
			
			System.out.println("(1) - cadastrar pet");
			System.out.println("(2) - voltar menu");
			System.out.println("(3) - Encerrar programa");
			System.out.println("");
			System.out.print("Digite sua escolha: ");
			int escolha = in.nextInt();
			
			if(escolha == 1) {
				windowPet();
			}else if(escolha == 2){
				windowIndex();
			}else{
				process.killProcess();
				break;
			}
			
		}
	}
// ------------------------------------------------------------------------------------------------------
	public static void windowPet() throws InterruptedException, IOException {
		process.clearTerminal();
		Scanner in = new Scanner(System.in);
		
		while(true) {
			System.out.println("---------- Cadastro do Pet ----------");
			System.out.print("Cadastrar nome pet: ");
			String nome = in.next();
			
			System.out.print("Cadastrar idade pet: ");
			String idade = in.next();
			
			System.out.print("Cadastrar raça pet: ");
			String raca = in.next();
			
			System.out.println("(1) - cadastrar pessoa");
			System.out.println("(2) - voltar menu");
			System.out.println("(3) - Encerrar programa");
			System.out.println("");
			System.out.print("Digite sua escolha: ");
			int escolha = in.nextInt();
			
			if(escolha == 1) {
				windowPerson();
			}else if(escolha == 2){
				windowIndex();
			}else{
				process.killProcess();
				break;
			}
			
		}
	}	
// ------------------------------------------------------------------------------------------------------
}
