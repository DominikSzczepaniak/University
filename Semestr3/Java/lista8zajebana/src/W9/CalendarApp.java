package W9;

import javax.swing.*;
import java.awt.*;

public class CalendarApp {
    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            GUI gui = new GUI("CalendarApp");
            gui.pack();
            gui.setSize(new Dimension(1200, 800));
            gui.setLocationRelativeTo(null);
            gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            gui.setVisible(true);
        });

    }
}
