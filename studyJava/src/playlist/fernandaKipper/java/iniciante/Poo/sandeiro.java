package playlist.fernandaKipper.java.iniciante.Poo;

public class sandeiro implements carro{
    private final int velocidadeMax = 150;
    private int velocidadeAtual = 0;

    @Override
    public void acelerar() {
        if(this.velocidadeAtual < velocidadeMax){
            this.velocidadeAtual += 10;
            System.out.println("acelerando");
            System.out.println("velocidadeAtual: " + this.velocidadeAtual);
        }else {
            System.out.println("acelerando....");
        }
    }
    @Override
    public void freiar() {
        System.out.println("freiando");
    }
    @Override
    public void parar() {
        System.out.println("parando");
    }


}
