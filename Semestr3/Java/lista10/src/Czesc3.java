import java.util.function.BinaryOperator;
import java.util.function.UnaryOperator;

public class Czesc3 {

    static UnaryOperator<Integer> collatzLength = n -> {
        if(n==1){
            return 1;
        }
        else if(n % 2 == 0){
            return 1 + Czesc3.collatzLength.apply(n / 2);
        }
        else{
            return 1 + Czesc3.collatzLength.apply(3 * n + 1);
        }
    };

    static BinaryOperator<Integer> Euklides = (a, b) -> {
        if(b == 0) return a;
        return Czesc3.Euklides.apply(b, a%b);
    };

    public static void main(String[] args) {
        liczCiag(11);
        liczCiag(15);
        liczCiag(27);
        liczNWD(48, 16);
        liczNWD(13, 12314255);
        liczNWD(100000001, 2);
        liczNWD(66, 12);
    }

    public static void liczCiag(int n){
        System.out.println("n = " + n + ": " + collatzLength.apply(n));
    }


    public static void liczNWD(int a, int b){
        System.out.println("NWD dla a = " + a + " i b = " + b + " jest rowne " + Euklides.apply(a, b));
    }

}
