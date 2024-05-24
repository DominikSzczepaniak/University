public class Producer implements Runnable {
    private final Buffer<String> buffer;

    public Producer(Buffer<String> buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        String[] messages = {"Message 1", "Message 2", "Message 3", "END"};
        try {
            for (String message : messages) {
                buffer.put(message);
                System.out.println("Produced: " + message);
                Thread.sleep(1000); // symulacja czasu produkcji
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
