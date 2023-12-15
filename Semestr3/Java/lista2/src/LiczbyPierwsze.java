import java.util.Arrays;

public final class LiczbyPierwsze {
    private static final int POTEGA2 = 21;
    private static final int[] SITO = new int[1<<POTEGA2];
    private static final int R = 1 << 21;
    static {
        for(int i = 2; i*i< R; i++){
            if(SITO[i] == 0){
                for(int j = i*i; j<R; j+=i){
                    SITO[j] = i;
                }
            }
        }
    }
    public static boolean czyPierwsza(long x){
        if(x <= 1) return false;
        if(x < R) return SITO[(int) x] == 0;
        if(x%2==0) return false;
        for(long i = 3; x/i/i>0; i+=2){
            if(x%i == 0) {
                return false;
            }
        }
        return true;
    }
    public static long[] naCzynnikiPierwsze(long x){
        long[] czynniki = new long[64];
        int index = 0;
        if(x==0 || x==-1 || x==1){
            czynniki[index++] = x;
            return Arrays.copyOf(czynniki, index+1);
        }
        if(x == Long.MIN_VALUE){
            czynniki[index++] = -1;
            for(int i = 0; i<63;i++){
                czynniki[index++] = 2;
            }
            return Arrays.copyOf(czynniki, 63);
        }
        if(x < 0){
            czynniki[index++] = -1;
            x = -x;
        }
        if(czyPierwsza(x)){
            czynniki[0] = 1;
            czynniki[1] = x;
            return Arrays.copyOf(czynniki, 2);
        }
        if(x < R){
            while(x > 1){
                czynniki[index++] = SITO[(int) x];
                x /= SITO[(int) x];
            }
        }
        else{
            while (x % 2 == 0) {
                czynniki[index++] = 2;
                x /= 2;
            }
            for(long i = 3; x>=1 && x/i/i>0; i += 2){
                while((i < R && SITO[(int) i] == i && x%i == 0)
                        ||
                        (i > R && x % i == 0)){
                    czynniki[index++] = i;
                    x /= i;
                }
            }
        }
        if(x > 1){
            czynniki[index++] = x;
        }
        return Arrays.copyOf(czynniki, index);
    }
}
