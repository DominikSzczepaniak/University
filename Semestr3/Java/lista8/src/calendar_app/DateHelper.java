package calendar_app;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Locale;

public class DateHelper {
    public static String yearFormat(GregorianCalendar calendar){
        return new SimpleDateFormat("MMMM", Locale.ENGLISH).format(calendar.getTime());
    }
    public static String yearFormat(Calendar calendar){
        return new SimpleDateFormat("MMMM", Locale.ENGLISH).format(calendar.getTime());
    }
    public static int dayOfMonth(Calendar calendar){
        return calendar.get(Calendar.DAY_OF_MONTH);
    }

    public static int dayOfMonth(GregorianCalendar calendar){
        return calendar.get(Calendar.DAY_OF_MONTH);
    }

    public static String dayOfWeek(GregorianCalendar calendar){
        return new SimpleDateFormat("EEE", Locale.ENGLISH).format(calendar.getTime());
    }

    public static String dayOfWeek(Calendar calendar){
        return new SimpleDateFormat("EEE", Locale.ENGLISH).format(calendar.getTime());
    }
}
