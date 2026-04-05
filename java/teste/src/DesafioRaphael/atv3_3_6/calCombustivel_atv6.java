package DesafioRaphael.atv3_3_6;

public class calCombustivel_atv6 {
	public static Float A(Double litro) {
		// preço litro é 2,90R$
		Float preco = (float) (litro * 2.90);
		Float total = (float) 0.0;
		if(litro <= 20) {
			total = (float) (preco - (preco * 0.03));
		}else {
			total = (float) (preco - (preco * 0.05));
		}
		return total;
	}
	
	public static Float G(Double litro) {
		// preço litro é 3,30R$
		Float preco = (float) (litro * 3.30);
		Float total = (float) 0.0;
		if(litro <= 20) {
			total = (float) (preco - (preco * 0.04));
		}else {
			total = (float) (preco - (preco * 0.06));
		}
		return total;
	}
}
