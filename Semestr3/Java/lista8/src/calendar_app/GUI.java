package calendar_app;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;

public class GUI extends JFrame {
    private JTabbedPane calendarTabbedPane;
    private JPanel rootPanel;
    private JPanel monthsInYearTab;
    private JPanel daysInMonthTab;
    private JList nextMonth;
    private JList currentMonth;
    private JList previousMonth;
    private JSpinner yearSpinner;
    private JSlider monthSlider;
    private JToolBar toolbar;
    private JPanel currentYearPanel;

    private GregorianCalendar calendar;

    private MonthGUI months[];

    public GUI(String title) throws HeadlessException {
        super(title);
        setContentPane(rootPanel);

        calendar = (GregorianCalendar) GregorianCalendar.getInstance();
        yearSpinner.setValue(calendar.getTime().getYear() + 1900);
        monthSlider.setValue(calendar.getTime().getMonth() + 1);


        months = new MonthGUI[12];

        createYearPanel();
        createListeners();
        fireContentsChanged();
    }

    private void createUIComponents() {
        currentYearPanel = new JPanel(new GridLayout(3, 4, 5, 5));
        previousMonth = new JList(new MonthListModel());
        currentMonth = new JList(new MonthListModel());
        nextMonth = new JList(new MonthListModel());

        previousMonth.setCellRenderer(new MonthCellRenderer());
        currentMonth.setCellRenderer(new MonthCellRenderer());
        nextMonth.setCellRenderer(new MonthCellRenderer());

        previousMonth.setBackground(Color.pink);
        currentMonth.setBackground(Color.white);
        nextMonth.setBackground(Color.pink);

        previousMonth.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        currentMonth.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        nextMonth.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));

        yearSpinner = new JSpinner(new SpinnerNumberModel(1, 1, null, 1));
    }

    private void createListeners() {
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

        previousMonth.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (calendar.get(Calendar.YEAR) == 1 && calendar.get(Calendar.MONTH) == Calendar.JANUARY)
                    return;
                calendar.add(Calendar.MONTH, -1);
                fireContentsChanged();
            }
        });

        nextMonth.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseReleased(MouseEvent e) {
                calendar.add(Calendar.MONTH, 1);
                fireContentsChanged();
            }
        });
    }

    private void createYearPanel() {
        Date originalDate = calendar.getTime();
        calendar.set(calendar.get(Calendar.YEAR), Calendar.JANUARY, 1);
        for (int i = 0; i < 12; i++) {
            months[i] = new MonthGUI(calendar, this);
            currentYearPanel.add(months[i]);
            calendar.add(Calendar.MONTH, 1);
        }

        calendar.setTime(originalDate);
    }

    private void updateYearPanel() {
        Date originalDate = calendar.getTime();
        calendar.set(calendar.get(Calendar.YEAR), Calendar.JANUARY, 1);

        for (MonthGUI month : months) {
            month.updateMonthUI(calendar);
            calendar.add(Calendar.MONTH, 1);
        }

        calendar.setTime(originalDate);
    }

    private void updateMonthLists() {
        Date now = calendar.getTime();
        ((MonthListModel) currentMonth.getModel()).changeDate(now);

        if (now.getYear() + 1900 != 1 || now.getMonth() != 0) {
            now.setMonth(now.getMonth() - 1);
            ((MonthListModel) previousMonth.getModel()).changeDate(now);
        } else
            ((MonthListModel) previousMonth.getModel()).changeDate(null);
        if (now.getYear() != 1 || now.getMonth() != 1)
            now.setMonth(now.getMonth() + 1);
        now.setMonth(now.getMonth() + 1);
        ((MonthListModel) nextMonth.getModel()).changeDate(now);

    }

    public void fireContentsChanged() {
        updateYearPanel();
        updateMonthLists();

        calendarTabbedPane.setTitleAt(0, "" + yearSpinner.getValue());
        calendarTabbedPane.setTitleAt(1, DateHelper.yearFormat(calendar));
        yearSpinner.setValue(calendar.get(Calendar.YEAR));
        monthSlider.setValue(calendar.get(Calendar.MONTH) + 1);

    }

    public void switchTab(int i) {
        calendarTabbedPane.setSelectedIndex(i);
    }


}
