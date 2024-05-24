import java.io.*;

public class Przedmiot implements Serializable {
    protected String nazwa;
    protected int waga;
    protected double cena;

    public Przedmiot(String nazwa, int waga, double cena) {
        this.nazwa = nazwa;
        this.waga = waga;
        this.cena = cena;
    }

    @Override
    public String toString() {
        return "Nazwa: " + nazwa + ", Waga: " + waga + ", Cena: " + cena;
    }

    public void zapiszDoPliku(String nazwaPliku) throws IOException {
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(nazwaPliku));
        out.writeObject(this);
        out.close();
    }

    public static Przedmiot odczytajZPliku(String nazwaPliku) throws IOException, ClassNotFoundException {
        ObjectInputStream in = new ObjectInputStream(new FileInputStream(nazwaPliku));
        Przedmiot obiekt = (Przedmiot) in.readObject();
        in.close();
        return obiekt;
    }
}
