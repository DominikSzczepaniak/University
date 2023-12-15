package obliczenia;

public class Stala extends Wyrazenie{
    private double wartosc;
    public Stala(String arg) {
        switch(arg){
            case "π" -> wartosc = 3.13;
            case "e" -> wartosc = 2.72;
            //do dodania
            default -> Stala.throwException(new IllegalArgumentException("Nie ma takiej stalej: " + arg));
        }
    }
    @SuppressWarnings("unchecked")
    private static <T extends Throwable> void throwException(Throwable exception, Object dummy) throws T
    {
        throw (T) exception;
    }
    public static void throwException(Throwable exception)
    {
        Stala.<RuntimeException>throwException(exception, null);
    }
    @Override
    public double licz() {
        return wartosc;
    }

    @Override
    public String toString() {
        return Double.toString(wartosc);
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj) return true;
        if(obj == null || !(obj instanceof Stala)) return false;
        Stala c = (Stala) obj;
        double w1 = this.licz();
        double w2 = c.licz();
        return w1 == w2;
    }

}
