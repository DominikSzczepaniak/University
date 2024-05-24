// Dominik Szczepaniak
// lista7
// javac 21.0.2

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.io.*;
import java.util.Objects;

public class Main {
    private static Przedmiot createNewObject(String className, String fileName) {
        Przedmiot przedmiot;
        if(!Objects.equals(className, "ProduktSpozywczy") && !Objects.equals(className, "Elektronika")){
            throw new IllegalArgumentException("Nieznana klasa: " + className);
        }
        if (className.equals("ProduktSpozywczy")) {
            przedmiot = new ProduktSpozywczy("Chleb", 500, 2.5, "2024-04-20", 5, 24);
        }
        else{
            przedmiot = new Elektronika("Laptop", 2000, 2500, "Dell", "Komputery i laptopy", "Praca");
        }
        try {
            przedmiot.zapiszDoPliku(fileName);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return przedmiot;
    }


    public static void main(String[] args) {
        int dl = args.length;
        if(dl > 1){
            String fileName = args[0];
            String className = args[1];

            try {
                boolean fileExists = new File(fileName).exists();
                if (fileExists) {
                    Przedmiot przedmiot = Przedmiot.odczytajZPliku(fileName);
                    System.out.println("Wczytano przedmiot z pliku:");
                    System.out.println(przedmiot);
                } else {
                    Przedmiot przedmiot = createNewObject(className, fileName);
                    System.out.println("Utworzono nowy obiekt klasy " + className);
                    System.out.println(przedmiot);
                }
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }

        JFrame frame = new JFrame("Edytor Obiektów");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTabbedPane tabbedPane = new JTabbedPane();

        ProduktSpozywczyEditor produktEditor = new ProduktSpozywczyEditor();
        ElektronikaEditor elektronikaEditor = new ElektronikaEditor();

        tabbedPane.addTab("Produkt Spożywczy", produktEditor);
        tabbedPane.addTab("Elektronika", elektronikaEditor);

        JButton submitButton = new JButton("Submit");
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(submitButton);

        frame.getContentPane().add(tabbedPane, BorderLayout.CENTER);
        frame.getContentPane().add(buttonPanel, BorderLayout.SOUTH);
        frame.pack();
        frame.setVisible(true);

        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Component selectedComponent = tabbedPane.getSelectedComponent();
                if (selectedComponent instanceof ProduktSpozywczyEditor produktEditor) {
                    ProduktSpozywczy produktSpozywczy = new ProduktSpozywczy(produktEditor.getNazwa(), produktEditor.getWaga(), produktEditor.getCena(), produktEditor.getTerminWaznosci(), produktEditor.getIloscBialka(), produktEditor.getIloscWeglowodanow());
                    System.out.println(produktSpozywczy);
                } else if (selectedComponent instanceof ElektronikaEditor elektronikaEditor) {
                    Elektronika elektronika = new Elektronika(elektronikaEditor.getNazwa(), elektronikaEditor.getWaga(), elektronikaEditor.getCena(), elektronikaEditor.getProducent(), elektronikaEditor.getKategoria(), elektronikaEditor.getZastosowanie());
                    System.out.println(elektronika);
                }
            }
        });
    }
}
