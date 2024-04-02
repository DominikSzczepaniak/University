// Dominik Szczepaniak
// lista 5 zadanie 2
// javac 21.0.2
public class Main {
    public static void main(String[] args) {
        OrderedList<Card> deck = new OrderedList<>();
        deck.addElement(new King());
        deck.addElement(new Ace());
        deck.addElement(new Queen());
        deck.addElement(new Jack());

        System.out.println(deck);
    }
}
