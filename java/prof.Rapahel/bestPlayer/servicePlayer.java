package bestPlayer;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class servicePlayer {
    public static void clear(){
        try{
            String sistema = System.getProperty("os.name");
            if(sistema.contains("Windows")){
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            }else{
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch(Exception e){
            System.out.println("Erro: "+ e.getMessage());
        }
    }

    public static void addVotos(List<Map> players, Map<String, Integer> player, int opc){
        boolean f = false;
        for (int i =0; i < players.size(); i++){
            if (players.get(i).containsValue(opc)){
                if (opc == (int) players.get(i).get("camisa")){
                    int voto = (int) players.get(i).get("voto");
                    players.get(i).replace("voto", voto, voto+1);
                    f = true;
                }
            }
        }if (f == false){
            player.put("camisa", opc);
            player.put("voto", 1);
            players.add(player);
        }
    }

    public static List<Map> setPorcentagem(List<Map> players, int totalVotos){
        List<Map> newPlayers =  new ArrayList<Map>();
        for (int i =0; i < players.size(); i++){
            Map<String, Double> player =  new HashMap<>();

            int camisa  = (int) players.get(i).get("camisa");
            int voto  = (int) players.get(i).get("voto");

            player.put("camisa", (double) camisa);
            player.put("voto",  (double) voto);
            player.put("porcentagem", (double) (voto *100)/ totalVotos);
            newPlayers.add(player);
        }
        return newPlayers;
    }
}