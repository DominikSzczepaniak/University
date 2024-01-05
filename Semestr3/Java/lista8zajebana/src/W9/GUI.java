package W9;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;

public class GUI extends JFrame {
    private JTabbedPane calendarTabbedPane;
    private JPanel rootPanel;
    private JPanel monthsInYearTab;
    private JPanel daysInMonthTab;
    private JList nextMonthList;
    private JList currentMonthList;
    private JList previousMonthList;
    private JSpinner yearSpinner;
    private JSlider monthSlider;
    private JToolBar toolbar;
    private JPanel currentYearPanel;

    private GregorianCalendar calendar;

    private MonthUI months[];

    public GUI(String title) throws HeadlessException {
        super(title);
        setContentPane(rootPanel);

        calendar = (GregorianCalendar) GregorianCalendar.getInstance();
        yearSpinner.setValue(calendar.getTime().getYear() + 1900);
        monthSlider.setValue(calendar.getTime().getMonth() + 1);


        months = new MonthUI[12];

        populateYearPanel();

        registerListeners();

        fireContentsChanged();
    }

    private void createUIComponents() {
        currentYearPanel = new JPanel(new GridLayout(3, 4, 5, 5));
        previousMonthList = new JList(new MonthListModel());
        currentMonthList = new JList(new MonthListModel());
        nextMonthList = new JList(new MonthListModel());

        previousMonthList.setCellRenderer(new MonthCellRenderer());
        currentMonthList.setCellRenderer(new MonthCellRenderer());
        nextMonthList.setCellRenderer(new MonthCellRenderer());

        previousMonthList.setBackground(Color.decode("#d2ddd9"));
        currentMonthList.setBackground(Color.decode("#efe7e1"));
        nextMonthList.setBackground(Color.decode("#d2ddd9"));

        previousMonthList.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        currentMonthList.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        nextMonthList.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));

        yearSpinner = new JSpinner(new SpinnerNumberModel(1, 1, null, 1));
    }



    private void registerListeners() {
        yearSpinner.addChangeListener(e -> {
            if ((int) yearSpinner.getValue() < 1)
                return;
            calendar.set(Calendar.YEAR, (int) yearSpinner.getValue());
            fireContentsChanged();
        });

        monthSlider.addChangeListener(e -> {
            calendar.set(Calendar.MONTH, monthSlider.getValue() - 1);
            fireContentsChanged();
        });

        previousMonthList.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (calendar.get(Calendar.YEAR) == 1 && calendar.get(Calendar.MONTH) == Calendar.JANUARY)
                    return;
                calendar.add(Calendar.MONTH, -1);
                fireContentsChanged();
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                previousMonthList.setBackground(Color.decode("#a0e8b8"));
            }

            @Override
            public void mouseExited(MouseEvent e) {
                previousMonthList.setBackground(Color.decode("#d2ddd9"));
            }
        });

        nextMonthList.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseReleased(MouseEvent e) {
                calendar.add(Calendar.MONTH, 1);
                fireContentsChanged();
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                nextMonthList.setBackground(Color.decode("#a0e8b8"));
            }

            @Override
            public void mouseExited(MouseEvent e) {
                nextMonthList.setBackground(Color.decode("#d2ddd9"));
            }
        });
    }

    private void populateYearPanel() {
        Date originalDate = calendar.getTime();
        calendar.set(calendar.get(Calendar.YEAR), Calendar.JANUARY, 1);
        for (int i = 0; i < 12; i++) {
            months[i] = new MonthUI(calendar, this);
            currentYearPanel.add(months[i]);
            calendar.add(Calendar.MONTH, 1);
        }

        calendar.setTime(originalDate);
    }

    private void updateYearPanel() {
        Date originalDate = calendar.getTime();
        calendar.set(calendar.get(Calendar.YEAR), Calendar.JANUARY, 1);

        for (MonthUI month : months) {
            month.updateMonthUI(calendar);
            calendar.add(Calendar.MONTH, 1);
        }

        calendar.setTime(originalDate);
    }

    private void updateMonthLists() {
        Date now = calendar.getTime();
        ((MonthListModel) currentMonthList.getModel()).changeDate(now);

        if (now.getYear() + 1900 != 1 || now.getMonth() != 0) {
            now.setMonth(now.getMonth() - 1);
            ((MonthListModel) previousMonthList.getModel()).changeDate(now);
        } else
            ((MonthListModel) previousMonthList.getModel()).changeDate(null);
        if (now.getYear() != 1 || now.getMonth() != 1)
            now.setMonth(now.getMonth() + 1);
        now.setMonth(now.getMonth() + 1);
        ((MonthListModel) nextMonthList.getModel()).changeDate(now);

    }

    public void fireContentsChanged() {
        updateYearPanel();
        updateMonthLists();

        calendarTabbedPane.setTitleAt(0, "" + yearSpinner.getValue());
        calendarTabbedPane.setTitleAt(1, new SimpleDateFormat("MMMM", Locale.ENGLISH).format(calendar.getTime()));
        yearSpinner.setValue(calendar.get(Calendar.YEAR));
        monthSlider.setValue(calendar.get(Calendar.MONTH) + 1);

    }

    public void switchTab(int i) {
        calendarTabbedPane.setSelectedIndex(i);
    }

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

}
