package playlist.fernandaKipper.java.intermediario.streamApi;

import java.util.ArrayList;
import java.util.List;

public class main {
    static void main(String[] args) {
        List<String> list  =  new ArrayList<>();
        list.add("Carro");
        list.add("Opala");
        list.add("Camaro");
        list.add("Audio");
        list.add("Opala19");
        list.add("Golf");
        list.add("Opala67");
        list.add("savero");
        list.add("Opala62");
        list.add("Opala67");

        List<Integer> list2  =  new ArrayList<>();
        list2.add(1);
        list2.add(1);
        list2.add(1);
        list2.add(1);

        String t = list.stream()
                .filter(nome -> nome.startsWith("Opala") && nome.endsWith("67"))
                .map(String::toUpperCase)
                .reduce( "Opala",(a,b) -> a + ", "+ b) .toString();

        int i = list2.stream().reduce(0 ,(a, b) -> (a+b));

        System.out.println(i);
    }
}
