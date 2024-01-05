import javax.swing.*;
import java.text.DateFormatSymbols;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.TimeZone;

public class DataModel extends AbstractListModel {
    private int year;
    private int month;
    public GregorianCalendar calendar = new GregorianCalendar(TimeZone.getDefault());

    public DataModel(){
        year = calendar.get(GregorianCalendar.YEAR);
        month = calendar.get(GregorianCalendar.MONTH)+1;
        calendar = new GregorianCalendar(year, month-1, 1);
    }

    public DataModel(int year, int month){
        this.year = year;
        this.month = month;
        calendar = new GregorianCalendar(year, month-1, 1);
    }

    @Override
    public int getSize() {
        return calendar.getActualMaximum(Calendar.DAY_OF_MONTH);
    }

    @Override
    public Object getElementAt(int index) {
        calendar.set(GregorianCalendar.DAY_OF_MONTH, index+1);
        String dayOfWeek = new DateFormatSymbols().getWeekdays()[calendar.get(GregorianCalendar.DAY_OF_WEEK)];
        int dayOfMonth = calendar.get(GregorianCalendar.DAY_OF_MONTH);
        String monthName = new DateFormatSymbols().getMonths()[month - 1];
        String dateInfo = dayOfWeek + ", " + dayOfMonth + " " + monthName;
        return dateInfo;
    }

    public void setMonth(int month) {
        this.month = month;
        calendar = new GregorianCalendar(year, month-1, 1);
    }

    public void setYear(int year) {
        this.year = year;
        calendar = new GregorianCalendar(year, month-1, 1);
    }

    public void decreaseMonth(){
        if(month == 1){
            year--;
            month = 12;
        }
        else{
            month--;
        }
        calendar = new GregorianCalendar(year, month-1, 1);
    }

    public void increaseMonth(){
        if(month == 12){
            year++;
            month = 1;
        }
        else{
            month++;
        }
        calendar = new GregorianCalendar(year, month-1, 1);
    }

    public int getMonth() {
        return month;
    }

    public int getYear() {
        return year;
    }
}
