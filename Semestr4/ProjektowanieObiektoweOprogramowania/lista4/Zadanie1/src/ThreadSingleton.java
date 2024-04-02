public class ThreadSingleton {
    private static final ThreadLocal<ThreadSingleton> threadInstance = ThreadLocal.withInitial(ThreadSingleton::new);

    private ThreadSingleton() {}

    public static ThreadSingleton getInstance(){
        return threadInstance.get();
    }

}
