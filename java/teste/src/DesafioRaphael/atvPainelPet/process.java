package DesafioRaphael.atvPainelPet;

import java.io.IOException;

public class process {
	public static void clearTerminal() throws InterruptedException, IOException {
		if(System.getProperty("os.name").contains("Window")) {
			new ProcessBuilder("cmd","/c","cls").inheritIO().start().waitFor();
		}else {
			new ProcessBuilder("clear").inheritIO().start().waitFor();
		}
	}
	
	public static void killProcess() throws InterruptedException, IOException {
		clearTerminal();
		
		System.out.println("Execução encerrada com sucesso!!");
	}
}
