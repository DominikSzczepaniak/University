import javax.swing.*;

class ProduktSpozywczyEditor extends PrzedmiotEditor {
    protected JTextField terminWaznosciField;
    protected JTextField iloscBialkaField;
    protected JTextField iloscWeglowodanowField;

    public ProduktSpozywczyEditor() {
        super();

        add(new JLabel("Termin ważności: "));
        terminWaznosciField = new JTextField();
        add(terminWaznosciField);

        add(new JLabel("Ilość białka: "));
        iloscBialkaField = new JTextField();
        add(iloscBialkaField);

        add(new JLabel("Ilość węglowodanów: "));
        iloscWeglowodanowField = new JTextField();
        add(iloscWeglowodanowField);

    }

    public String getTerminWaznosci() {
        return terminWaznosciField.getText();
    }

    public int getIloscBialka(){
        return Integer.parseInt(iloscBialkaField.getText());
    }

    public int getIloscWeglowodanow(){
        return Integer.parseInt(iloscWeglowodanowField.getText());
    }
}