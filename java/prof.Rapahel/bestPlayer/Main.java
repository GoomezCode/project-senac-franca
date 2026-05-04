package bestPlayer;


import javax.management.InvalidAttributeValueException;
import java.text.DecimalFormat;
import java.util.*;

public class Main {
	static DecimalFormat df = new DecimalFormat("0.00");
	static List<Map> players = new ArrayList<>();
	static int totalVotos = 0;
	public static void main(String[] args) {
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
					players = servicePlayer.setPorcentagem(players, totalVotos);
					windowStatus();
					System.out.println("");
					System.out.println("Sistema finalizado...");
					break;
				}
				if(opc >23 || opc < 0){throw new InvalidAttributeValueException("Camisa não encontrada!");}
				boolean f = false;
				servicePlayer.addVotos(players, player, opc);

				servicePlayer.clear();
				System.out.printf("Camisa %1$d votado!!\n\n", opc);
				totalVotos+=1;
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

	public static void windowStatus(){
		List<Double> porcentual = new ArrayList<>();
		for (int i = 0; i<players.size(); i++){
			double camisa = (double) players.get(i).get("camisa");
			double votos = (double) players.get(i).get("voto");
			double porcentagem = (double) players.get(i).get("porcentagem");
			porcentual.add(porcentagem);
//			System.out.printf("Camisa: %1$.2f | Votos: %2$.2f | Porcentual: %3$.2f\n");

			System.out.println("Camisa: "+(int)camisa+" | Votos: "+(int)votos+ " | Porcentagem: "+df.format(porcentagem)+"%");
		}
		System.out.println("");
		double maxPorcentual = Collections.max(porcentual);
		for(Map v: players){
			if(v.containsValue(maxPorcentual)){
				System.out.println("Melhor jogador --> Camisa: "+v.get("camisa")+", Votos: "+v.get("voto")+", Porcentual: "+df.format(v.get("porcentagem"))+"%");
			}
		}
		System.out.println("\nTotal votos: "+totalVotos);
	}
}