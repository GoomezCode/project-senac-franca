package playlist.fernandaKipper.java.intermediario.records;

public class pintura<e extends pintavel> {
    private e coisaPintar;
    private String cor;
    private String textura;

    void pintar(){
        this.coisaPintar.aplicarTinta();
    }


    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getTextura() {
        return textura;
    }

    public void setTextura(String textura) {
        this.textura = textura;
    }

    public e getCoisaPintar() {
        return coisaPintar;
    }

    public void setCoisaPintar(e coisaPintar) {
        this.coisaPintar = coisaPintar;
    }
}
