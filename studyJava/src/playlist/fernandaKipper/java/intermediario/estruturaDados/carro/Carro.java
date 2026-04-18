package playlist.fernandaKipper.java.intermediario.estruturaDados.carro;

public class Carro {
    String modelo;
    String cor;
    int ano;
    String placa;

    void ligar(){
        System.out.println("Ligar Carro");
    }






    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }
}
