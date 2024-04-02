public class TimedSingleton {
    private static TimedSingleton instance;
    private static long lastAccessTime = 0;
    private static final long MAX_DURATION = 5000; // 5 sekund

    private TimedSingleton() {}

    public static synchronized TimedSingleton getInstance() {
        long currentTime = System.currentTimeMillis();
        if (instance == null || (currentTime - lastAccessTime > MAX_DURATION)) {
            instance = new TimedSingleton();
            lastAccessTime = currentTime;
        }
        return instance;
    }
}
