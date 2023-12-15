package prezentacja;

import obliczenia.Wymierna;
import rozgrywka.Gra;
import rozgrywka.Wyjatki;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Okno extends Frame {
    final private TextField licznikTextField, mianownikTextField;
    final private JButton submitButton, stopButton, newGameButton, exitButton;
    final private Scrollbar attemptsScrollbar, zakresScrollbar;
    final private Label WprowadzUlamek, liczbaProb, HashChar, zakresUlamkow, zakresWartosc, wynikStrzalu, graniceSzukania, startSzukania, koniecSzukania;
    final private Gra gra;
    private Wymierna start = new Wymierna(), koniec = new Wymierna(1);

    public Okno() {
        super("Gra z ułamkami");
        setSize(400, 300);
        setLayout(new FlowLayout());

        licznikTextField = new TextField(5);
        mianownikTextField = new TextField(5);
        WprowadzUlamek = new Label("Wprowadź ułamek: ");
        HashChar = new Label("/");
        add(WprowadzUlamek);
        add(licznikTextField);
        add(HashChar);
        add(mianownikTextField);
        licznikTextField.setVisible(false);
        mianownikTextField.setVisible(false);
        WprowadzUlamek.setVisible(false);
        HashChar.setVisible(false);

        submitButton = new JButton("Wyślij");
        add(submitButton);
        submitButton.setVisible(false);

        attemptsScrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 1, 1, 1, 11);
        liczbaProb = new Label("Liczba prób: ");
        add(liczbaProb);
        add(attemptsScrollbar);
        attemptsScrollbar.setVisible(false);

        zakresScrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 5, 1, 5, 20);
        zakresUlamkow = new Label("Zakres ułamków:");
        add(zakresScrollbar);
        zakresWartosc = new Label();
        zakresWartosc.setText("Wartość: " + zakresScrollbar.getValue());
        add(zakresWartosc);

        wynikStrzalu = new Label();
        add(wynikStrzalu);
        wynikStrzalu.setVisible(false);

        stopButton = new JButton("Zakończ grę");
        add(stopButton);
        stopButton.setVisible(false);

        newGameButton = new JButton("Nowa gra");
        add(newGameButton);

        exitButton = new JButton("Wyjście");
        add(exitButton);
        this.gra = new Gra();

        graniceSzukania = new Label("Granice szukania ułamków: ");
        startSzukania = new Label("0");
        koniecSzukania = new Label("1");
        add(graniceSzukania);
        add(startSzukania);
        add(koniecSzukania);
        graniceSzukania.setVisible(false);
        startSzukania.setVisible(false);
        koniecSzukania.setVisible(false);

        setupListeners();
    }

    private void setupListeners() {
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Wymierna in = null;
                try{
                    in = new Wymierna(Integer.parseInt(licznikTextField.getText()), Integer.parseInt(mianownikTextField.getText()));
                }catch(Exception ee){
                    if(ee.getMessage().equals("Gra nie jest aktywna")){
                        dispose();
                    }
                    System.out.println(ee.getMessage());
                }
                if(in.compareTo(koniec) == 1 || in.compareTo(start) == -1){
                    try{
                        throw new Wyjatki.PozaZasiegiem("Liczba jest poza zasiegiem - mniejsza niz " + start.toString() + " i wieksza niz " + koniec.toString());
                    }catch(Exception ee){
                        throw new RuntimeException(ee);
                    }
                }
                try{
                    String wynik = gra.strzal(in);
                    if(wynik.equals("Podana liczba jest za duża") && in.compareTo(koniec) == -1){
                        koniecSzukania.setText(in.toString());
                        koniec = in;
                    }
                    else if(wynik.equals("Podana liczba jest za mała") && in.compareTo(start) == 1){
                        startSzukania.setText(in.toString());
                        start = in;
                    }
                    if(gra.getStatusGry().equals("Zwyciestwo") || gra.getStatusGry().equals("Porazka")){
                        koniecGry();
                    }
                    wynikStrzalu.setText(wynik);
                    wynikStrzalu.setVisible(true);
                    revalidate();
                    repaint();

                }catch(Exception ee){
                    System.out.println(ee.getMessage());
                }
                updateGUI();
            }
        });
        licznikTextField.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                try{
                    if(e.getExtendedKeyCode() != 8){
                        int test = Integer.parseInt(String.valueOf(e.getKeyChar()));
                    }
                }catch(Exception ef){
                    e.consume();
                    System.out.println("licznik musi byc liczba");
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {

            }

            @Override
            public void keyReleased(KeyEvent e) {

            }
        });

        mianownikTextField.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                if(mianownikTextField.getText().length() == 0 && e.getKeyChar() == '0'){
                    e.consume();
                    try {
                        throw new Wyjatki.NieprawidlowaLiczbaWymiernaException("mianownik nie moze byc 0");
                    } catch (Wyjatki.NieprawidlowaLiczbaWymiernaException ex) {
                        throw new RuntimeException(ex);
                    }
                }
                try{
                    int test = Integer.parseInt(String.valueOf(e.getKeyChar()));
                }catch(Exception ef){
                    e.consume();
                    System.out.println("mianownik musi byc liczba");
                    try {
                        throw new Wyjatki.NieprawidlowyFormatException("mianownik musi byc liczba");
                    } catch (Wyjatki.NieprawidlowyFormatException ex) {
                        throw new RuntimeException(ex);
                    }
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {

            }

            @Override
            public void keyReleased(KeyEvent e) {

            }
        });

        submitButton.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                if(licznikTextField.getText().length() > 0 && mianownikTextField.getText().length() > 0){
                    int licznik = Integer.parseInt(licznikTextField.getText());
                    int mianownik = Integer.parseInt(mianownikTextField.getText());
                    submitButton.setToolTipText(licznik + "/"+ mianownik);
                    revalidate();
                    repaint();
                }
            }
        });

        stopButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                wynikStrzalu.setText("poddales sie");
                gra.surrender();
                koniecGry();
                wynikStrzalu.setVisible(true);
                revalidate();
                repaint();

            }
        });

        newGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int zakres = zakresScrollbar.getValue();
                try{
                    gra.start(zakres);
                } catch (Exception ex) {
                    System.out.println(ex.getMessage());
                }

                initializeGUI();
            }
        });

        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });
        zakresScrollbar.addMouseListener(new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent e) {
                zakresWartosc.setText("Wartość: " + zakresScrollbar.getValue());
                revalidate();
                repaint();
            }

            @Override
            public void mousePressed(MouseEvent e) {
                zakresWartosc.setText("Wartość: " + zakresScrollbar.getValue());
                revalidate();
                repaint();
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                zakresWartosc.setText("Wartość: " + zakresScrollbar.getValue());
                revalidate();
                repaint();
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                zakresWartosc.setText("Wartość: " + zakresScrollbar.getValue());
                revalidate();
                repaint();
            }

            @Override
            public void mouseExited(MouseEvent e) {
                zakresWartosc.setText("Wartość: " + zakresScrollbar.getValue());
                revalidate();
                repaint();
            }
        });
    }

    private void updateGUI(){
        attemptsScrollbar.setValue(gra.getLicznikProb());
    }
    private void initializeGUI(){
        attemptsScrollbar.setMaximumSize(new Dimension(0, gra.getMaksIloscProb()));
        attemptsScrollbar.setEnabled(false);
        zakresScrollbar.setVisible(false);
        newGameButton.setVisible(false);
        zakresUlamkow.setVisible(false);
        zakresWartosc.setVisible(false);
        licznikTextField.setVisible(true);
        submitButton.setVisible(true);
        mianownikTextField.setVisible(true);
        WprowadzUlamek.setVisible(true);
        HashChar.setVisible(true);
        stopButton.setVisible(true);
        attemptsScrollbar.setVisible(true);
        graniceSzukania.setVisible(true);
        startSzukania.setVisible(true);
        koniecSzukania.setVisible(true);
    }

    private void koniecGry(){
        licznikTextField.setVisible(false);
        submitButton.setVisible(false);
        mianownikTextField.setVisible(false);
        WprowadzUlamek.setVisible(false);
        HashChar.setVisible(false);
        stopButton.setVisible(false);
        attemptsScrollbar.setVisible(false);
        graniceSzukania.setVisible(false);
        startSzukania.setVisible(false);
        koniecSzukania.setVisible(false);
        liczbaProb.setVisible(false);
    }
}
