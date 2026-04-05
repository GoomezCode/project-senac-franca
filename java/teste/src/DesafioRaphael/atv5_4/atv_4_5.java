package DesafioRaphael.atv5_4;

import javax.swing.JOptionPane;

public class atv_4_5 {
	public static void main(String[] args) {
//		 atv_04();
//		 atv_05();
	}
	
	public static void atv_05() {
		int cliente = Integer.parseInt(JOptionPane.showInputDialog("\n aluno(10) | professor(12) | direção(1) | não Aluno(15)"+"\n Digite o codigo de sua clasificação"));
		int qntCopia = Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade de folhas que queira imprimir"));
		Double val = 0.0;
		if(cliente == 10) {
			val = calcPagar_atv5.al(qntCopia);
		}else if(cliente == 12) {
			val = calcPagar_atv5.prof(qntCopia);
		}else if(cliente == 1) {
			val = calcPagar_atv5.dir(qntCopia);
		}else{
			val = calcPagar_atv5.nAl(qntCopia);
		}
		
		StringBuilder window = new StringBuilder();
		window.append("Clasificação: "+ calcPagar_atv5.identify(cliente));
		window.append("\n quantidade: "+qntCopia+" folhas");
		window.append("\n Terá que pagar no total: "+ val+"R$");
		
		JOptionPane.showMessageDialog(null, window);
	}
	
	
	public static void atv_04() {
		Double notaT = 0.0;
		for(int i = 1; i <= 3; i++) {
			String nota = JOptionPane.showInputDialog(i+"- Digite sua nota: ");
			notaT += Double.parseDouble(nota);
		}
		Double media = notaT /3;
		char nota = 'D';
		if(media <= 4.9) {
			nota = 'D';
		}else if(media <= 6.9 ) {
			nota = 'C';
		}else if (media <= 8.9) {
			nota = 'B';
		}else if (media <= 10) {
			nota = 'A';
		}
		StringBuilder win = new StringBuilder();
		win.append("\n média é: "+media.intValue());
		win.append("\n Conceito é: "+ nota);
		JOptionPane.showMessageDialog(null, win);
	}
	
}
