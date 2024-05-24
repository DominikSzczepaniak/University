import javax.swing.*;

class ElektronikaEditor extends PrzedmiotEditor {
    protected JTextField producentField;
    protected JTextField kategoriaField;
    protected JTextField zastosowanieField;


    public ElektronikaEditor() {
        super();

        add(new JLabel("Producent: "));
        producentField = new JTextField();
        add(producentField);

        add(new JLabel("Kategoria: "));
        kategoriaField = new JTextField();
        add(kategoriaField);

        add(new JLabel("Zastosowanie: "));
        zastosowanieField = new JTextField();
        add(zastosowanieField);
    }

    public String getProducent() {
        return producentField.getText();
    }

    public String getKategoria() {
        return kategoriaField.getText();
    }

    public String getZastosowanie() {
        return zastosowanieField.getText();
    }


}