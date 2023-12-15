import java.util.List;
public class Main {
    public static void main(String[] args) {
        if(args.length == 0){
            System.err.println("Podaj jakas liczbe");
            return;
        }
        for(var arg : args){
            long x = Long.valueOf(arg);
            var dzielniki = LiczbyPierwsze.naCzynnikiPierwsze(x);
            System.out.print(x + " = ");
            for(int i = 0; i<dzielniki.length; i++){
                System.out.print(dzielniki[i]);
                if(i != dzielniki.length-1){
                    System.out.print(" * ");
                }
            }
            System.out.println();
        }
    }
}