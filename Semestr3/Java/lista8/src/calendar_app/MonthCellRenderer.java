package calendar_app;

import javax.swing.*;
import java.awt.*;

class MonthCellRenderer extends JLabel implements ListCellRenderer {
    public MonthCellRenderer() {
        setHorizontalAlignment(CENTER);
    }

    @Override
    public Component getListCellRendererComponent(JList list, Object value, int index, boolean isSelected, boolean cellHasFocus) {
        String string = (String) value;
        if (string.contains("Sun"))
            setForeground(Color.RED);
        else
            setForeground(Color.BLACK);
        setText(string);
        return this;
    }
}