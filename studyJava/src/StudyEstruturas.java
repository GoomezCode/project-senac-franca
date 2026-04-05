import java.util.*;

public class StudyEstruturas {
static void main(String[] args) {
     // Map --> estrutura de chave e valor ("nome: joãozinho")
    //  Set --> Não permite valores duplicadas em uma lista ("joão, joaozinho, alice")
    //  List --> permite valores duplicadas em uma lista ("joão, joaozinho, alice, joão")
    //  Queue --> Filas, usada normalmente para processamento em ordem (1,2,3) - (3,2,1) etc..

    Map<String, String> map = new HashMap<>();
    map.put("name","fernanda");
    map.put("sobrenome","morais");
    map.put("nascimento","10-02-1992");

    Set<Integer> tst = new HashSet<>();
    tst.add(1);
    tst.add(190);
    tst.add(1);
    tst.add(80);

    List<String> list = new ArrayList<>();
    list.add("Fernanda");
    list.add("joãozinho");
    list.add("Mark grecy");
    list.add("Conner");
    list.add("Krypton");

    Queue<String> queue = new LinkedList<>();
    queue.add("fernanda");
    queue.add("Joãozinho");
    queue.add("Mark Grecy");

    // Stream --> realizar operaçãoes funcionais nas nossas collections (estruturas de dados)
    // filter, map, reduce, agregações
    // filter - filtrar elementos de uma coleção
    // map - transformar os elementos de uma coleção
    // reduce - reduz os elementos de uma coleção a um único elemento
    // agregações - soma, média, contagem, etc..

    list.stream()
        .map(String::toLowerCase)
        .filter(nome -> nome.startsWith("m"))
        .forEach(System.out::println);
    }
}
