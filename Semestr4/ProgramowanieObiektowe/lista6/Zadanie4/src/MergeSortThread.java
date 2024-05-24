public class MergeSortThread<T extends Comparable<T>> extends Thread {
    private T[] array;
    private int low, high;
    private T[] temp;

    public MergeSortThread(T[] array, T[] temp, int low, int high) {
        this.array = array;
        this.temp = temp;
        this.low = low;
        this.high = high;
    }

    @Override
    public void run() {
        mergeSort(array, temp, low, high);
    }

    private void mergeSort(T[] array, T[] temp, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            MergeSortThread<T> leftSorter = new MergeSortThread<>(array, temp, low, mid);
            MergeSortThread<T> rightSorter = new MergeSortThread<>(array, temp, mid + 1, high);
            leftSorter.start();
            rightSorter.start();

            try {
                leftSorter.join();
                rightSorter.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            merge(array, temp, low, mid, high);
        }
    }

    private void merge(T[] array, T[] temp, int low, int mid, int high) {
        System.arraycopy(array, low, temp, low, high - low + 1);

        int i = low, j = mid + 1, k = low;
        while (i <= mid && j <= high) {
            if (temp[i].compareTo(temp[j]) <= 0) {
                array[k++] = temp[i++];
            } else {
                array[k++] = temp[j++];
            }
        }

        while (i <= mid) {
            array[k++] = temp[i++];
        }

        while (j <= high) {
            array[k++] = temp[j++];
        }
    }
}
