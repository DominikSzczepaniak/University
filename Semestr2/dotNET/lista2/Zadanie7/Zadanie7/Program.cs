class Wektor
{
    int information1;
    int information2;
    public Wektor(int a, int b)
    {
        information1 = a;
        information2 = b;
    }
    public static Wektor operator +(Wektor a, Wektor b) => new Wektor(a.information1 + b.information1,
                                                                      a.information2 + b.information2);
    public static Wektor operator -(Wektor a, Wektor b) => new Wektor(a.information1 - b.information1,
                                                                      a.information2 - b.information2);
    public static Wektor operator *(Wektor a, int w) => new Wektor(a.information1 * w, a.information2 *w);
    public static Wektor operator *(int w, Wektor a) => new Wektor(a.information1 * w, a.information2 *w);
    public static int operator *(Wektor a, Wektor b)
    {
        return a.information1 * b.information1 + a.information2 * b.information2;
    }
    public static Wektor operator /(Wektor a, int w)
    {
        return new Wektor(a.information1 / w, a.information2 / w);
    }
    public static bool operator ==(Wektor a, Wektor b)
    {
        return (a.information1 == b.information1 && a.information2 == b.information2);
    }
    public static bool operator !=(Wektor a, Wektor b)
    {
        return !(a == b);
    }
    public string ToString()
    {
        return (information1 + " " + information2);
    }
}
class Program
{
    public static void Main()
    {
        Wektor w1 = new Wektor(3, 4);
        Wektor w2 = new Wektor(5, 7);
        Wektor suma = w1 + w2;
        Wektor roznica = w1 - w2;
        Wektor skalar = w1 * 3;
        Wektor dzielenie = w1 / 2;
        Console.WriteLine(suma.ToString());
        Console.WriteLine(roznica.ToString());
        Console.WriteLine(skalar.ToString());
        Console.WriteLine(dzielenie.ToString());
        Console.ReadLine();
    }
}