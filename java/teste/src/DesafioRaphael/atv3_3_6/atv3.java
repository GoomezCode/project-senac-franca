package DesafioRaphael.atv3_3_6;

import java.awt.List;
import java.util.ArrayList;
import java.util.Collections;

import javax.swing.JOptionPane;

public class atv3 {
	
public static void main(String[] args) {
	atv_1_3();
	
}

public static void atv_0_3() {
	float numConta = Float.parseFloat(JOptionPane.showInputDialog("Digite o número de sua conta!"));
	float saldo = Float.parseFloat(JOptionPane.showInputDialog("Digite o saldo atual: "));
	float debito = Float.parseFloat(JOptionPane.showInputDialog("Digite o valor do debito: "));
	float credito = Float.parseFloat(JOptionPane.showInputDialog("Digite o valor do credito: "));
	float saldoAtual = saldo - debito + credito;	
	
	JOptionPane.showMessageDialog(null, (saldoAtual >= 0)? "Saldo Positivo": "Saldo Negativo");
}

public static void atv_1_3() {
	float num1 = Float.parseFloat(JOptionPane.showInputDialog("Digite o primeiro número!"));
	float num2 = Float.parseFloat(JOptionPane.showInputDialog("Digite o segundo número!"));
	float num3 = Float.parseFloat(JOptionPane.showInputDialog("Digite o terceiro número!"));
	
	ArrayList<Float> nums = new ArrayList<Float>();
	nums.add(num1);
	nums.add(num2);
	nums.add(num3);
	
	Float max = Collections.max(nums);
	Float min = Collections.min(nums);
	JOptionPane.showMessageDialog(null, "O maior numero é: "+ max+"\n O menor numero é: "+ min);	
}

}
