import java.io.IOException;

public class teste {
    public static void limparTerminal() {
        try {
            String sistema = System.getProperty("os.name");

            if (sistema.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }

        } catch (Exception e) {
            System.out.println("Erro ao limpar o terminal.");
        }
    }

    public static void main(String[] args){
        String sistema = System.getProperty("os.name").toLowerCase();

        System.out.println(sistema);
    }
}
