import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Main {
    @Nested
    class AllTests{
        @Test
        public void GlobalSingletonTest() {
            GlobalSingleton firstInstance = GlobalSingleton.getInstance();
            GlobalSingleton secondInstance = GlobalSingleton.getInstance();
            assertSame(firstInstance, secondInstance);
        }

        @Test
        public void ThreadSingletonTest() throws InterruptedException{

            final ThreadSingleton[] instances = new ThreadSingleton[2];

            Thread thread1 = new Thread(() -> instances[0] = ThreadSingleton.getInstance());
            Thread thread2 = new Thread(() -> instances[1] = ThreadSingleton.getInstance());

            thread1.start();
            thread2.start();

            thread1.join();
            thread2.join();

            assertNotNull(instances[0]);
            assertNotNull(instances[1]);
            assertNotSame(instances[0], instances[1]);
        }

        @Test
        public void TimedSingletonTest() throws InterruptedException{
            TimedSingleton firstInstance = TimedSingleton.getInstance();
            Thread.sleep(6000);
            TimedSingleton secondInstance = TimedSingleton.getInstance();
            assertNotSame(firstInstance, secondInstance);
        }
    }

    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}