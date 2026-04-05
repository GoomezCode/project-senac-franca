package DesafioRaphael.atv3_3_6;

import javax.swing.JOptionPane;

public class atv6 {
public static void main(String[] args) {
	int opc = Integer.parseInt(JOptionPane.showInputDialog("Qual será o combusível?"+"\n Álcool (1) | Gasolina (2)"));
	Double qntLitro = Double.parseDouble(JOptionPane.showInputDialog("Digite a quantidade em litro"));
	Float pagar = (float) 0.0;
	
	if(opc == 1) {
		pagar = calCombustivel_atv6.A(qntLitro);
	}else if(opc == 2) {
		pagar = calCombustivel_atv6.G(qntLitro);
	}
	
	
	JOptionPane.showMessageDialog(null, "O valor a pagar é: "+pagar+"R$");
}
}
