package playlist.fernandaKipper.java.iniciante;

public class condicionais {
    static void main() {
        byte b = 100;
        short s = 10000;
        int i = 100000;
        long l = 100000L;
        float f = 10.5f;
        double d = 20.5;
        char c = 'A';
        String str = "Teste";
        boolean bool = true;

        if (str.isBlank()) {
            System.out.println("Verdadeiro");
        }else if(str.equalsIgnoreCase("teste")){
            System.out.println(str);
        } else{
            System.out.println("Falso");
        }

    }
}
