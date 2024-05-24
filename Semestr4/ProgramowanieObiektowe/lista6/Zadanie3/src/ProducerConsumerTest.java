// Dominik Szczepaniak
// lista 6 zadanie 3
// javac 21.0.2

public class ProducerConsumerTest {
    public static void main(String[] args) {
        Buffer<String> buffer = new Buffer<>(10);
        Thread producerThread = new Thread(new Producer(buffer));
        Thread consumerThread = new Thread(new Consumer(buffer));

        producerThread.start();
        consumerThread.start();
    }
}
