package playlist.fernandaKipper.java.iniciante.Poo;

public abstract class serVivo {
    protected int idade;

    public serVivo(int idade) {this.idade = idade;}

    public abstract void respirar();
    public void dormir() {
        System.out.println("dormindo");
    }
}
