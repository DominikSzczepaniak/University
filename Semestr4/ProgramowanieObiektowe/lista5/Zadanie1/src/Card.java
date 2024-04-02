abstract class Card implements Comparable<Card> {
    protected int rank;
    @Override
    public int compareTo(Card o) {
        return Integer.compare(this.rank, o.rank);
    }

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + " (rank " + rank + ")";
    }
}

class Ace extends Card {
    public Ace() {
        this.rank = 14; // Najwyższa wartość
    }
}

class King extends Card {
    public King() {
        this.rank = 13;
    }
}

class Queen extends Card {
    public Queen() {
        this.rank = 12;
    }
}

class Jack extends Card {
    public Jack() {
        this.rank = 11;
    }
}
