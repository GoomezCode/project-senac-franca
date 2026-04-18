package playlist.fernandaKipper.java.intermediario.records;

public class main {
    static void main() {
        Carro carro = new Carro("Sandeiro", 2080,"Daniel", "D3H4VK23");
        System.out.printf("Modelo: %1$s \nProprietario: %2$s \nAno: %3$d"
        , carro.modelo(),  carro.proprietario(), carro.ano());


    }
}
