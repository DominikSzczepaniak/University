import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static java.lang.Integer.parseInt;

public class Czesc1 {
    public static void main(String[] args) {
        ArrayList<Integer> liczby;
        try {
            liczby = readFile();
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
            return;
        }
        List<Integer> sortedNumbers = liczby.stream()
                .sorted(Comparator.reverseOrder())
                .toList();
        System.out.println("1. Liczby uporządkowane od największej do najmniejszej wartości: " + sortedNumbers);

        List<Integer> primeNumbers = liczby.stream()
                .filter(Czesc1::isPrime)
                .toList();
        System.out.println("2. Liczby pierwsze: " + primeNumbers);

        int n = 1000;
        int sumBelowN = liczby.stream()
                .filter(number -> number < n)
                .mapToInt(Integer::intValue)
                .sum();
        System.out.println("3. Suma liczb mniejszych niż " + n + ": " + sumBelowN);

        int divisibleByN = 7;
        long divisibleCount = liczby.stream()
                .filter(number -> number % divisibleByN == 0)
                .count();
        System.out.println("4. Liczba liczb podzielnych przez " + divisibleByN + ": " + divisibleCount);
    }

    public static ArrayList<Integer> readFile() throws IllegalArgumentException{
        String path = "src/liczby.txt";
        ArrayList<Integer> liczby = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String regex = "^\\s*(\\d*)?:\\s*\\/\\/\\s*(.*)?$";
            Pattern pattern = Pattern.compile(regex);

            for (String ln = br.readLine(); ln != null; ln = br.readLine()) {
                Matcher matcher = pattern.matcher(ln);
                if (matcher.matches()) {
                    String liczbaString = matcher.group(1);
                    if(liczbaString.isEmpty()){
                        continue;
                    }
                    int liczba = parseInt(liczbaString);
                    liczby.add(liczba);
                }
                else{
                    throw new IllegalArgumentException("Niepoprawny plik");
                }
            }
        } catch (IllegalArgumentException e) {
            throw e;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return liczby;
    }

    private static boolean isPrime(int number) {
        if (number < 2) return false;
        for (long i = 2; i*i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}
