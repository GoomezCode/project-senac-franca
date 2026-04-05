package DesafioRaphael.atv5_4;

public class calcPagar_atv5 {
	
	public static Double al(int qntCopia) {
		return qntCopia * 0.15;
	}
	public static Double prof(int qntCopia) {
		return qntCopia * 0.07;
	}
	public static Double dir(int qntCopia) {
		return 0.0;
	}
	public static Double nAl(int qntCopia) {
		return qntCopia * 0.20;
	}
	
	public static String identify(int cliente) {
		String tipo = "";
		if(cliente == 10) {
			tipo = "Aluno";
		}else if(cliente == 12) {
			tipo = "Professor";
		}else if(cliente == 1) {
			tipo = "Direção";
		}else if(cliente == 15) {
			tipo = "Não aluno";
		}
		return tipo;
	}
}
