package playlist.fernandaKipper.java.iniciante.Poo;

public class humano extends serVivo{
    public humano() {
        super(34);
    }

    @Override
    public void respirar() {
        this.idade = idade + 1;
        System.out.println("respirando");
    }
}
