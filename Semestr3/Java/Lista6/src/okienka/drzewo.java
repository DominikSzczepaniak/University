package okienka;
import algorithms.BST;

import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class drzewo extends JFrame{
    BSTPanel mainPanel;
    BST<String> bst;
    public drzewo(){
        bst = new BST<String>();
        mainPanel = new BSTPanel();

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1200, 800);

        initComponents();
    }
    private void initComponents(){
        JPanel controlPanel = new JPanel();
        JLabel inputLabel = new JLabel("Wstaw wartość:");
        JTextField inputValueField = new JTextField(10);
        JButton insertButton = new JButton("Wstaw");
        JButton removeButton = new JButton("Usun");
        JButton minButton = new JButton("Minimalna wartośc");
        JButton maxButton = new JButton("Maksymalna wartośc");
        JLabel outputValueLabel = new JLabel();

        insertButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String value = inputValueField.getText();
                bst.insert(value);
                mainPanel.repaint();
            }
        });

        removeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String value = inputValueField.getText();
                bst.remove(value);
                mainPanel.repaint();
            }
        });
        minButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String value = bst.min();
                outputValueLabel.setText(value);
                mainPanel.repaint();
            }
        });
        maxButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String value = bst.max();
                outputValueLabel.setText(value);
                mainPanel.repaint();
            }
        });

        controlPanel.add(inputLabel);
        controlPanel.add(inputValueField);
        controlPanel.add(insertButton);
        controlPanel.add(removeButton);
        controlPanel.add(minButton);
        controlPanel.add(maxButton);
        controlPanel.add(outputValueLabel);

        add(controlPanel, BorderLayout.NORTH);
        add(mainPanel, BorderLayout.CENTER);
    }

    private class BSTPanel extends JPanel{
        private static final int NODE_SIZE = 30;
        private static final int HORIZONTAL_GAP = 300;

        private void drawTree(Graphics g, int x, int y, BST<String>.Node<String> node, int horizontalGap, int level) {
            if (node != null) {
                g.setColor(Color.BLACK);
                g.fillOval(x - NODE_SIZE / 2, y - NODE_SIZE / 2, NODE_SIZE, NODE_SIZE);
                g.setColor(Color.YELLOW);
                g.drawString((String) node.value, x - 5, y + 5);

                if (node.left != null) {
                    int newX = x - horizontalGap / 2;
                    int newY = y + 50;
                    g.drawLine(x, y, newX, newY);
                    drawTree(g, newX, newY, node.left, horizontalGap / 2, level + 1);
                }

                if (node.right != null) {
                    int newX = x + horizontalGap / 2;
                    int newY = y + 50;
                    g.drawLine(x, y, newX, newY);
                    drawTree(g, newX, newY, node.right, horizontalGap / 2, level + 1);
                }
            }
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            drawTree(g, getWidth() / 2, 30, bst.root, HORIZONTAL_GAP, 0);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new drzewo().setVisible(true);
            }
        });
    }

}
