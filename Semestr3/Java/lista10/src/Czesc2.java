import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static java.lang.Double.parseDouble;
import static java.lang.Integer.parseInt;

public class Czesc2 {
    public static void main(String[] args){
        LinkedList<Trojkat> trojkaty;
        try{
            trojkaty = readFile();
        } catch(IllegalArgumentException e){
            System.out.println(e.getMessage());
            return;
        }

        System.out.println("1. Trojkaty uporzadkowane od najmniejszego do najwiekszego obwodu:");
        trojkaty.stream()
                .sorted(Comparator.comparingDouble(t -> t.a + t.b + t.c))
                .forEach(System.out::println);


        System.out.println("\n2. Trojkaty, ktore sa trojkatami prostokatnymi:");
        trojkaty.stream()
                .filter(t -> {
                    double[] boki = {t.a, t.b, t.c};
                    Arrays.sort(boki);
                    return Math.pow(boki[0], 2) + Math.pow(boki[1], 2) == Math.pow(boki[2], 2);
                })
                .forEach(System.out::println);


        System.out.println("\n3. Ile trojkatow jest rownobocznych:");
        long ileRownobocznych = trojkaty.stream()
                .filter(t -> (t.a == t.b) && (t.b == t.c))
                .count();
        System.out.println("Liczba rownobocznych trojkatow: " + ileRownobocznych);


        System.out.println("\n4. Dwa trojkaty z najmniejszym i najwiekszym polem:");
        trojkaty.stream().min(Comparator.comparingDouble(t -> ((t.a + t.b + t.c) / 2 * ((t.a + t.b + t.c) / 2 - t.a) * ((t.a + t.b + t.c) / 2 - t.b) * ((t.a + t.b + t.c) / 2 - t.c)))).ifPresent(t -> System.out.println(t));
        trojkaty.stream().max(Comparator.comparingDouble(t -> ((t.a + t.b + t.c) / 2 * ((t.a + t.b + t.c) / 2 - t.a) * ((t.a + t.b + t.c) / 2 - t.b) * ((t.a + t.b + t.c) / 2 - t.c)))).ifPresent(t -> System.out.println(t));

    }

    public static LinkedList<Trojkat> readFile() throws IllegalArgumentException{
        String path = "src/trojkat.txt";
        LinkedList<Trojkat> trojkaty = new LinkedList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String regex = "^\\s*(\\d*\\.?\\d+)?\\s*(\\d*\\.?\\d+)?\\s*(\\d*\\.?\\d+)?(?:\\s*\\/\\/\\s*(.*))?$";
            Pattern pattern = Pattern.compile(regex);

            for (String ln = br.readLine(); ln != null; ln = br.readLine()) {
                Matcher matcher = pattern.matcher(ln);
                if (matcher.matches()) {
                    String liczbaString1 = matcher.group(1);
                    String liczbaString2 = matcher.group(2);
                    String liczbaString3 = matcher.group(3);
                    if(liczbaString1 == null || liczbaString2==null || liczbaString3 == null){
                        continue;
                    }
                    if(liczbaString1.isEmpty() || liczbaString2.isEmpty() || liczbaString3.isEmpty()){
                        continue;
                    }
                    double liczba1 = parseDouble(liczbaString1);
                    double liczba2 = parseDouble(liczbaString2);
                    double liczba3 = parseDouble(liczbaString3);
                    Trojkat abc;
                    try{
                        abc = new Trojkat(liczba1, liczba2, liczba3);
                    }catch(IllegalArgumentException ignore){continue;};
                    trojkaty.add(abc);
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
        return trojkaty;
    }
}
