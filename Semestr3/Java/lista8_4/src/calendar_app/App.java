package calendar_app;

import javax.swing.*;
import java.awt.*;

public class App {
    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            GUI gui = new GUI("CalendarApp");
            gui.pack();
            gui.setSize(new Dimension(1200, 900));
            gui.setLocationRelativeTo(null);
            gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            gui.setVisible(true);
        });

    }
}
