import javax.swing.*;
import java.awt.*;
import java.text.DateFormatSymbols;
import java.util.GregorianCalendar;

public class DataView extends JLabel implements ListCellRenderer<String> {
    private DataModel dataModel;
    public DataView(DataModel dataModel) {
        this.dataModel = dataModel;
        setOpaque(true);
    }
    @Override
    public Component getListCellRendererComponent(JList<? extends String> list, String value, int index,
                                                  boolean isSelected, boolean cellHasFocus) {
        setText(value);
        try {
            int dayOfWeek = dataModel.calendar.get(GregorianCalendar.DAY_OF_WEEK);
            if (dayOfWeek == GregorianCalendar.SUNDAY) {
                setBackground(Color.RED);
                setForeground(Color.WHITE);
            } else {
                setBackground(list.getBackground());
                setForeground(list.getForeground());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        if (isSelected) {
            setBackground(list.getSelectionBackground());
            setForeground(list.getSelectionForeground());
        }

        return this;
    }

    public JPanel getMonthTable(){
        JPanel panel = new JPanel();
        panel.add(new JLabel(new DateFormatSymbols().getMonths()[dataModel.calendar.get(GregorianCalendar.MONTH)]), BorderLayout.NORTH);
        int start_day = dataModel.calendar.get(GregorianCalendar.DAY_OF_WEEK);

        int dayInMonth = dataModel.getSize();
        int rows = 6;
        if(dataModel.getMonth() == 2){
            if(start_day==2){
                rows = 4;
            }
            else{
                rows = 5;
            }
        }
        else{
            if(start_day + 4*7 >= dayInMonth){
                rows = 5;
            }
        }
        GridLayout daysGrid = new GridLayout(rows+1, 7); //7 kolumn? spoko dostaniesz 6, 7 albo 8. ruletka decyduje?

        panel.setLayout(daysGrid);
//        panel.add(new JLabel("Poniedziałek"));
//        panel.add(new JLabel("Wtorek"));
//        panel.add(new JLabel("Środa"));
//        panel.add(new JLabel("Czwartek"));
//        panel.add(new JLabel("Piątek"));
//        panel.add(new JLabel("Sobota"));
//        panel.add(new JLabel("Niedziela"));
        start_day = start_day == 1 ? 7 : start_day-1;
        int next_sunday_in_days = 7-start_day;
//        System.out.println(next_sunday_in_days);
        int sum = 0;
        for(int i = 1; i<start_day-1; i++){
            panel.add(new JLabel(""));
            sum++;
        }
        for(int i = 1; i<=dayInMonth; i++){
            JLabel label = new JLabel(""+i, SwingConstants.CENTER);
            if(next_sunday_in_days==0){
                label.setForeground(Color.RED);
                next_sunday_in_days = 7;
            }
            panel.add(label);
            next_sunday_in_days--;
            sum++;
        }
        for(int i = 0; i<sum - rows*7; i++){
            panel.add(new JLabel(""));
        }
        System.out.println(rows*7 + " " + sum);
        System.out.println(daysGrid.getColumns());
        return panel;
    }
}
