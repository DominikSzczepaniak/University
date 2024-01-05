package prezentacja;
import gra.gra;
import gra.Para;

import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;


public class okno extends JFrame {

    private JMenuBar menuBar;
    private JMenu gameMenu, movesMenu, settingsMenu, helpMenu;
    private JMenuItem newGameItem, exitItem, upItem, downItem, leftItem, rightItem, selectItem, pieceColor, mapColor;
    private JRadioButtonMenuItem britishBoardItem, europeanBoardItem;
    private JCheckBoxMenuItem fillPiecesItem;
    private JMenuItem aboutGameItem, aboutAppItem;

    private MapPanel gamePanel;
    private JLabel statusLabel;
    private gra Gra;
    Para currentPosition = new Para(0, 2);

    Para selectedSquare = null;

    public okno() {
        setTitle("Samotnik");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 600);

        menuBar = new JMenuBar();

        gameMenu = new JMenu("Gra");
        gameMenu.setMnemonic(KeyEvent.VK_G);
        newGameItem = new JMenuItem("Nowa", KeyEvent.VK_N);
        exitItem = new JMenuItem("Koniec", KeyEvent.VK_K);
        gameMenu.add(newGameItem);
        gameMenu.addSeparator();
        gameMenu.add(exitItem);


        movesMenu = new JMenu("Ruchy");
        movesMenu.setMnemonic(KeyEvent.VK_R);
        upItem = new JMenuItem("W górę");
        upItem.setMnemonic(KeyEvent.VK_I);
        downItem = new JMenuItem("W dół");
        downItem.setMnemonic(KeyEvent.VK_K);
        leftItem = new JMenuItem("W lewo");
        leftItem.setMnemonic(KeyEvent.VK_J);
        rightItem = new JMenuItem("W prawo");
        rightItem.setMnemonic(KeyEvent.VK_L);
        selectItem = new JMenuItem("Zaznacz");
        selectItem.setMnemonic(KeyEvent.VK_ENTER);

        movesMenu.add(upItem);
        movesMenu.add(downItem);
        movesMenu.add(leftItem);
        movesMenu.add(rightItem);
        movesMenu.add(selectItem);


        settingsMenu = new JMenu("Ustawienia");
        ButtonGroup boardGroup = new ButtonGroup();
        britishBoardItem = new JRadioButtonMenuItem("Brytyjska");
        europeanBoardItem = new JRadioButtonMenuItem("Europejska");
        fillPiecesItem = new JCheckBoxMenuItem("Wypełnienie pionów");
        pieceColor = new JMenuItem("Kolor pionów");
        mapColor = new JMenuItem("Kolor mapy");
        boardGroup.add(britishBoardItem);
        boardGroup.add(europeanBoardItem);
        settingsMenu.add(britishBoardItem);
        settingsMenu.add(europeanBoardItem);
        settingsMenu.add(fillPiecesItem);
        settingsMenu.add(pieceColor);
        settingsMenu.add(mapColor);
        pieceColor.setVisible(false);
        mapColor.setVisible(false);


        helpMenu = new JMenu("Pomoc");
        aboutGameItem = new JMenuItem("O grze");
        aboutAppItem = new JMenuItem("O aplikacji");
        helpMenu.add(aboutGameItem);
        helpMenu.add(aboutAppItem);

        menuBar.add(gameMenu);
        menuBar.add(movesMenu);
        menuBar.add(settingsMenu);
        menuBar.add(Box.createHorizontalGlue());
        menuBar.add(helpMenu);

        setJMenuBar(menuBar);

        statusLabel = new JLabel("Stan gry");

        setLayout(new BorderLayout());
        add(statusLabel, BorderLayout.SOUTH);

        var zapisanaGra = gra.wczytajStanGry();
        if(zapisanaGra != null){
            int decyzja = JOptionPane.showConfirmDialog(okno.this,"Wczytać zapisaną grę?");
            if(decyzja == 0){
                Gra = zapisanaGra;
                gamePanel = new MapPanel();
                add(gamePanel, BorderLayout.CENTER);
                pieceColor.setVisible(true);
                mapColor.setVisible(true);
                britishBoardItem.setVisible(false);
                europeanBoardItem.setVisible(false);
                statusLabel.setText("Wczytano poprzednią gre");
            }
        }

        newGameItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(!britishBoardItem.isSelected() && !europeanBoardItem.isSelected()){
                    JOptionPane.showMessageDialog(okno.this, "NIE WYBRANO TYPU GRY!");
                    return;
                }

                Gra = new gra(europeanBoardItem.isSelected());
                gamePanel = new MapPanel();
                add(gamePanel, BorderLayout.CENTER);
                pieceColor.setVisible(true);
                mapColor.setVisible(true);
                britishBoardItem.setVisible(false);
                europeanBoardItem.setVisible(false);
                statusLabel.setText("Nowa gra rozpoczęta");

            }
        });

        exitItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(Gra != null){
                    Gra.zapiszStanGry();
                }
                System.exit(0);
            }
        });

        upItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(!Gra.dozwolonePrzesuniecie(new Para(currentPosition.getFirst()-1, currentPosition.getSecond()))){
                    return;
                }
                currentPosition.setFirst(currentPosition.getFirst()-1);
                gamePanel.repaint();
                statusLabel.setText("Ruch w górę");
            }
        });

        downItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(!Gra.dozwolonePrzesuniecie(new Para(currentPosition.getFirst()+1, currentPosition.getSecond()))){
                    return;
                }
                currentPosition.setFirst(currentPosition.getFirst()+1);
                gamePanel.repaint();
                statusLabel.setText("Ruch w dół");
            }
        });

        leftItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(!Gra.dozwolonePrzesuniecie(new Para(currentPosition.getFirst(), currentPosition.getSecond()-1))){
                    return;
                }
                currentPosition.setSecond(currentPosition.getSecond()-1);
                gamePanel.repaint();
                statusLabel.setText("Ruch w lewo");
            }
        });

        rightItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(!Gra.dozwolonePrzesuniecie(new Para(currentPosition.getFirst(), currentPosition.getSecond()+1))){
                    return;
                }
                currentPosition.setSecond(currentPosition.getSecond()+1);
                gamePanel.repaint();
                statusLabel.setText("Ruch w prawo");
            }
        });

        selectItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(selectedSquare == null){
                    if(Gra.plansza[currentPosition.getFirst()][currentPosition.getSecond()] == 0){
                        System.out.println("Musisz zaznaczyc pionka!");
                        return;
                    }
                    selectedSquare = new Para(currentPosition.getFirst(), currentPosition.getSecond());
                }
                else{
                    if(Gra.dozwolonyRuch(selectedSquare, currentPosition)){
                        Gra.wykonajRuch(selectedSquare.getFirst(), selectedSquare.getSecond(), currentPosition.getFirst(), currentPosition.getSecond());
                    }
                    else{
                        System.out.println("Niepoprawny ruch!");
                    }
                    selectedSquare = null;
                }
                gamePanel.repaint();
            }
        });

        britishBoardItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                statusLabel.setText("Wybrano planszę brytyjską");
            }
        });

        europeanBoardItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                statusLabel.setText("Wybrano planszę europejską");
            }
        });

        fillPiecesItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (fillPiecesItem.isSelected()) {
                    statusLabel.setText("Piony będą wypełnione");
                } else {
                    statusLabel.setText("Piony nie będą wypełnione");
                }
                gamePanel.repaint();
            }
        });

        pieceColor.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Color newColor = JColorChooser.showDialog(okno.this, "Wybierz kolor pionków", gamePanel.getPieceColor());
                if (newColor != null) {
                    gamePanel.setPieceColor(newColor);
                    gamePanel.repaint();
                }
                gamePanel.repaint();
            }
        });

        mapColor.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Color newColor = JColorChooser.showDialog(okno.this, "Wybierz kolor mapy", gamePanel.getMapColor());
                if(newColor != null){
                    gamePanel.setMapColor(newColor);
                    gamePanel.repaint();
                }
            }
        });

        aboutGameItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(okno.this, "Opis zasad gry\n" +
                        "Wybierz dowolny pionek. Możesz nim zbić sąsiedni pionek tylko gdy pole o dwa dalej w tym samym kierunku jest puste\n" +
                        "(Możesz przeskoczyć nad zbijanym pionkiem, jeśli pole na które przeskoczysz jest puste)");
            }
        });

        aboutAppItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(okno.this, "O aplikacji\n" +
                        "Autor: Dominik Szczepaniak\n" +
                        "Wersja: 1.0\n" +
                        "Data: 16.12.2023");
            }
        });


    }

    private class MapPanel extends JPanel{
        private Color MapColor = Color.WHITE;
        private Color PieceColor = Color.BLACK;

        public Color getMapColor() {
            return MapColor;
        }

        public Color getPieceColor() {
            return PieceColor;
        }

        public void setMapColor(Color mapColor) {
            MapColor = mapColor;
        }

        public void setPieceColor(Color pieceColor) {
            PieceColor = pieceColor;
        }

        public void paintComponent(Graphics g){
            if(Gra.koniecGry() == 1){
                britishBoardItem.setVisible(true);
                europeanBoardItem.setVisible(true);
                gamePanel.setVisible(false);
                JOptionPane.showMessageDialog(okno.this,"Wygrałeś!");
            }
            else if(Gra.koniecGry() == 2){
                britishBoardItem.setVisible(true);
                europeanBoardItem.setVisible(true);
                gamePanel.setVisible(false);
                JOptionPane.showMessageDialog(okno.this,"Przegrałeś!");
            }
            super.paintComponent(g);
            int cellSize = 50;
            for(int i = 0; i<7; i++){
                for(int j = 0; j<7; j++){
                    if(Gra.plansza[i][j] == -5){
                        continue;
                    }
                    int x = j * cellSize;
                    int y = i * cellSize;
                    g.setColor(MapColor);
                    g.drawRect(x, y, cellSize, cellSize);
                    if(i == currentPosition.getFirst() && j == currentPosition.getSecond()){
                        g.fillRect(x, y, cellSize,cellSize);
                    }
                    if (selectedSquare != null) {
                        if(i == selectedSquare.getFirst() && j == selectedSquare.getSecond()){
                            g.setColor(Color.RED);
                            g.fillRect(x, y, cellSize, cellSize);
                            g.setColor(MapColor);
                        }
                    }
                    if(Gra.plansza[i][j] == 1){
                        g.setColor(PieceColor);
                        if(fillPiecesItem.isSelected()){
                            g.fillOval(x, y, cellSize, cellSize);
                        }
                        else{
                            g.drawOval(x, y, cellSize, cellSize);
                        }

                    }
                }
            }
        }
    }


    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new okno().setVisible(true);
            }
        });
    }
}
