package playlist.fernandaKipper.java.iniciante.Poo;

// public --> acessivel de todo lugar
// default --> quando eu não defino, ele segue esse daqui
// private --> acessivel somente dentro da classe que foi definido
// protected --> acessivel por todo mundo que está no mesmo pacote

public class modificadorAcesso {
    static void main() {
        sandeiro myCar = null;
    try{
        myCar.acelerar();
    } catch(NullPointerException e){
        System.out.println("Vende carro furado");
    }

    }
}
