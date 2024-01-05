package kalendarz;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;

public class MainWindow extends JFrame{
    private JPanel rootPanel;
    private JTable january;
    private JTable february;
    private JTable march;
    private JTable april;
    private JTable august;
    private JTable july;
    private JTable june;
    private JTable may;
    private JTable september;
    private JTable october;
    private JTable november;
    private JTable december;
    private JList PreviousMonth;
    private JList NextMonth;
    private JList CurrentMonth;
    private JSpinner yearSpinner;
    private JSlider monthSlider;
    private JTabbedPane tabbedPane1;

    private GregorianCalendar calendar;

    public MainWindow(String title) throws HeadlessException {
        super(title);
        monthSlider.setValue(calendar.getTime().getMonth()+1);


    }

    private void createUIComponents() {

        calendar = (GregorianCalendar) GregorianCalendar.getInstance();

        PreviousMonth = new JList(new MonthListModel());
        CurrentMonth = new JList(new MonthListModel());
        NextMonth = new JList(new MonthListModel());
        PreviousMonth.setCellRenderer(new MonthCellRenderer());
        CurrentMonth.setCellRenderer(new MonthCellRenderer());
        NextMonth.setCellRenderer(new MonthCellRenderer());

        PreviousMonth.setBackground(Color.decode("#d2ddd9"));
        CurrentMonth.setBackground(Color.decode("#efe7e1"));
        NextMonth.setBackground(Color.decode("#d2ddd9"));

        PreviousMonth.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        CurrentMonth.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));
        NextMonth.setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY, 2));

        yearSpinner = new JSpinner(new SpinnerNumberModel(1, 1, null, 1));
        yearSpinner.setValue(calendar.getTime().getYear() + 1900);


        PrepareYearPanel();

    }

    private void registerListeners(){
        yearSpinner.addChangeListener(e -> {
            if ((int) yearSpinner.getValue() < 1){
                return;
            }
            calendar.set(Calendar.YEAR, (int) yearSpinner.getValue());
            fireContestsChanged();
        });

        monthSlider.addChangeListener(e -> {
            calendar.set(Calendar.MONTH, monthSlider.getValue() - 1);
            fireContestsChanged();
        });

        PreviousMonth.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if(calendar.get(Calendar.YEAR) == 1 && calendar.get(Calendar.MONTH) == Calendar.JANUARY){
                    return;
                }
                calendar.add(Calendar.MONTH, -1);
                fireContestsChanged();
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                PreviousMonth.setBackground(Color.decode("#a0e8b8"));
            }

            @Override
            public void mouseExited(MouseEvent e) {
                PreviousMonth.setBackground(Color.decode("#d2ddd9"));
            }
        });

        NextMonth.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                calendar.add(Calendar.MONTH, 1);
                fireContestsChanged();
            }

            @Override
            public void mouseEntered(MouseEvent e) {
                PreviousMonth.setBackground(Color.decode("#a0e8b8"));
            }

            @Override
            public void mouseExited(MouseEvent e) {
                PreviousMonth.setBackground(Color.decode("#d2ddd9"));
            }
        });
    }
    private int getRowNumber(){
        return (int) Math.ceil((double) (calendar.get(Calendar.DAY_OF_WEEK) + calendar.get(Calendar.DAY_OF_MONTH)-1) / 7);
        //ktorym dniem w tygodniu jest pierwszy + reszta dni / 7
    }
    private void PrepareYearPanel(){
        Date data = calendar.getTime();
        calendar.set(calendar.get(Calendar.YEAR), Calendar.JANUARY, 1);
        january = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        february = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        march = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        april = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        may = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        june = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        july = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        august = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        september = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        november = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);
        december = new JTable(getRowNumber(), 7);
        calendar.add(Calendar.MONTH, 1);

    }

    private void updateMonthLists(){
        Date now = calendar.getTime();
        ((MonthListModel) CurrentMonth.getModel()).changeDate(now);

        if (now.getYear() + 1900 != 1 || now.getMonth() != 0) {
            now.setMonth(now.getMonth() - 1);
            ((MonthListModel) PreviousMonth.getModel()).changeDate(now);
        } else
            ((MonthListModel) PreviousMonth.getModel()).changeDate(null);
        if (now.getYear() != 1 || now.getMonth() != 1)
            now.setMonth(now.getMonth() + 1);
        now.setMonth(now.getMonth() + 1);
        ((MonthListModel) NextMonth.getModel()).changeDate(now);
    }

    public void fireContestsChanged(){
        PrepareYearPanel();
        updateMonthLists();



        tabbedPane1.setTitleAt(0, "" + yearSpinner.getValue());
        tabbedPane1.setTitleAt(1, new SimpleDateFormat("MMMM", Locale.ENGLISH).format(calendar.getTime()));
        yearSpinner.setValue(calendar.get(Calendar.YEAR));
        monthSlider.setValue(calendar.get(Calendar.MONTH) + 1);
    }

    public void switchTab(int i){
        tabbedPane1.setSelectedIndex(i);
    }

    class MonthCellRenderer extends JLabel implements ListCellRenderer{
        public MonthCellRenderer(){
            setHorizontalAlignment(CENTER);
        }
        @Override
        public Component getListCellRendererComponent(JList list, Object value, int index, boolean IsSelected, boolean cellHasFocus){
            String string = (String) value;
            if(string.contains("Sun")){
                setForeground(Color.RED);
            }
            else{
                setForeground(Color.BLACK);
            }
            setText(string);
            return this;
        }
    }
}
