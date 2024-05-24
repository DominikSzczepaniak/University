
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PrzedmiotEditor extends JPanel {
    protected JTextField nazwaField;
    protected JTextField wagaField;
    protected JTextField cenaField;

    public PrzedmiotEditor() {
        setLayout(new GridLayout(3, 2));

        add(new JLabel("Nazwa: "));
        nazwaField = new JTextField();
        add(nazwaField);

        add(new JLabel("Waga: "));
        wagaField = new JTextField();
        add(wagaField);

        add(new JLabel("Cena: "));
        cenaField = new JTextField();
        add(cenaField);
    }

    public String getNazwa() {
        return nazwaField.getText();
    }

    public int getWaga() {
        return Integer.parseInt(wagaField.getText());
    }

    public double getCena() {
        return Double.parseDouble(cenaField.getText());
    }

}

