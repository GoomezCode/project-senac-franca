package playlist.fernandaKipper.java.intermediario.generics;

import java.util.*;

public class introducao {
    static void main() {
        List<String> list  =  new ArrayList<>();
        list.add("Carro");
        list.add("Opala");
        list.add("Camaro");
        list.add("Audio");
        list.add("Golf");
        list.add("savero");

        Set<String> set  =  new HashSet<>();
        set.add("Carro");
        set.add("Opala");
        set.add("Camaro");
        set.add("Audio");
        set.add("Golf");
        set.add("savero");

        Map<String, String> dicionario = new  HashMap<>();
        dicionario.put("modelo","Opala");
        dicionario.put("valor","200");
        dicionario.put("placa","23K2J3H");
        dicionario.put("propriotario","Teste");

        Queue<String> queue = new  LinkedList<>();
        queue.add(dicionario.get("placa"));
        queue.add(dicionario.get("modelo"));
        queue.add(dicionario.get("valor"));
        queue.add(dicionario.get("propriotario"));

        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.add("Carro");
        linkedList.add("Opala");
        linkedList.add(1,"Diaa");




    }
}
