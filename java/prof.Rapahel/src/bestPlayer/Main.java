package bestPlayer;


import javax.management.InvalidAttributeValueException;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		List<Map> players = new ArrayList<>();




		Scanner input = new Scanner(System.in);

		servicePlayer.clear();
		while(true){
			try{
				Map<String,Integer> player = new HashMap<>();
				System.out.println("Digite 0 para sair!");
				System.out.println("");
				System.out.print("Digite o num do jogador (1 - 23): ");
				int opc = input.nextInt();
				if (opc == 0){
					servicePlayer.clear();
					System.out.println("");
					System.out.println("Sistema finalizado...");
					break;
				}
				if(opc >23 || opc < 0){throw new InvalidAttributeValueException("Camisa não encontrada!");}
				servicePlayer.clear();
				System.out.printf("Camisa %1$d votado!!\n\n", opc);

			} catch(InvalidAttributeValueException e){
				servicePlayer.clear();
				System.out.println("Erro: "+e.getMessage());
				System.out.println("");
			} catch(InputMismatchException e){
				servicePlayer.clear();
				System.out.println("Erro: Digite um numero!");
				System.out.println("");
				input.nextLine();
			}
		}




	}
}
