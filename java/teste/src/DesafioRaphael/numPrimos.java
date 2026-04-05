package DesafioRaphael;

public class numPrimos {
public static void main(String[] args) {
	int num = 630;	
	boolean verifi = true;
	
	if(num <= 1) {
		verifi = false;
	}else {
		for(int i =2;i<= Math.sqrt(num); i++) {
			if(num % i == 0) {
				verifi = false;
				break;
			}
		}
	}
	
	System.out.println( (verifi == true)?"O numero: "+num+" é Primo!!":"O numero: "+num+" Não é primo!!");
}
}
