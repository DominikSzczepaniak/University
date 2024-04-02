
class Program
{
    static void Main(string[] args)
    {
        Wektor v1 = new Wektor(3);
        v1[0] = 1;
        v1[1] = 2;
        v1[2] = 3;

        Wektor v2 = new Wektor(3);
        v2[0] = 4;
        v2[1] = 5;
        v2[2] = 6;

        Wektor suma = v1 + v2;
        Console.WriteLine("Suma: ({0}, {1}, {2})", suma[0], suma[1], suma[2]);

        float iloczynSkalarny = v1 * v2;
        Console.WriteLine("Iloczyn skalarny: {0}", iloczynSkalarny);

        float skalar = 2.5f;
        Wektor iloczyn = v1 * skalar;
        Console.WriteLine("Iloczyn przez skalar: ({0}, {1}, {2})", iloczyn[0], iloczyn[1], iloczyn[2]);

        float normaV1 = v1.Norma();
        Console.WriteLine("Norma v1: {0}", normaV1);

        Console.ReadLine();
    }
}
