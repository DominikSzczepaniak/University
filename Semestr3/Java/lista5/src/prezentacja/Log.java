package prezentacja;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.time.LocalTime;
import java.util.Properties;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Log {
    private static final String logi = "rozgrywka.log";
    private static final Logger logger = Logger.getLogger(Log.class.getName());
    private FileHandler fileHandler;
    private int strzalLog = 1;
    {
        try{
            fileHandler = new FileHandler(logi);
            fileHandler.setFormatter(new SimpleFormatter());
            logger.addHandler(fileHandler);
        }catch(IOException e){
            e.printStackTrace();
        }
    }
    private String czas(){
        return LocalTime.now().toString();
    }
    private void log(String message){
        logger.info(message);
    }
    public void logStart(){
        log("StartGry: " + czas());
    }
    public void logEnd(){
        log("KoniecGry: " + czas());
    }
    public void logWin(){log("Wygrana");}
    public void logLose(){log("Przegrana");}
    public void logStrzal(){
        log("Strzal " + strzalLog + ": " + czas());
    }

}
