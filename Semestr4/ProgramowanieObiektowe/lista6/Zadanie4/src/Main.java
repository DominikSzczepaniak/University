// Dominik Szczepaniak
// lista 6 zadanie 4
// javac 21.0.2

public class Main {
    public static void main(String[] args) {
        Integer[] array = {4, 1, 6, 2, 5, 3, 8, 7, 9};
        Integer[] temp = new Integer[array.length];

        MergeSortThread<Integer> sorter = new MergeSortThread<>(array, temp, 0, array.length - 1);
        sorter.start();
        try {
            sorter.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Sorted array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}