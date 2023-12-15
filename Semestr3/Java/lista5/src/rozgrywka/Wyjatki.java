package rozgrywka;

public class Wyjatki {
    public static class NieprawidlowaLiczbaWymiernaException extends Exception {
        public NieprawidlowaLiczbaWymiernaException(String message) {
            super(message);
        }
    }

    public static class NieprawidlowyFormatException extends Exception {
        public NieprawidlowyFormatException(String message) {
            super(message);
        }
    }
    public static class PozaZasiegiem extends Exception{
        public PozaZasiegiem(String message){
            super(message);
        }
    }

}
