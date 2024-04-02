using System.Text;

public class IntStream
{
    internal int _licznik = -1;

    public int next()
    {
        _licznik += 1;
        return _licznik;
    }

    public bool eos()
    {
        return _licznik + 1 < _licznik;
    }

    public void reset()
    {
        _licznik = -1;
    }
}

public class FibStream : IntStream
{
    private int _licznik2 = 1;

    public FibStream()
    {
        _licznik = 0;
    }

    public int next()
    {
        int save = _licznik2;
        _licznik2 = _licznik + _licznik2;
        _licznik = save;
        return _licznik2;
    }

    public bool eos()
    {
        return _licznik + _licznik2 < _licznik2;
    }

    public void reset()
    {
        _licznik = 0;
        _licznik2 = 1;
    }
}

public class RandomStream
{
    private Random rand = new Random();
    public int next()
    {
        return rand.Next();
    }

    public bool eos()
    {
        return false;
    }

    public void reset()
    {
    }
}

public class RandomWordStream
{
    private RandomStream rand;
    private FibStream fib; //zakładam, że w zadaniu chodziło o długości kolejnych liczb fibbonaciego, a nie liczb pierwszych?

    public RandomWordStream()
    {
        rand = new RandomStream();
        fib = new FibStream();
    }
    public string next()
    {
        int dl = fib.next();
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < dl; i++)
        {
            int liczba = rand.next() % 26 + 65;
            ans.Append((char)liczba);
        }
        return ans.ToString();
    }

    public void reset()
    {
        fib.reset();
    }

    public bool eos()
    {
        return fib.eos();
    }
}

public class Program
{
    public static void Main()
    {
        IntStream ist = new IntStream();
        FibStream fst = new FibStream();
        RandomStream rst = new RandomStream();
        for (int i = 0; i < 5; i++)
        {
            Console.Write(ist.next() + " ");
        }
        Console.WriteLine();
        ist.reset();
        for (int i = 0; i < 5; i++)
        {
            Console.Write(ist.next() + " ");
        }

        Console.WriteLine();
        
        for (int i = 0; i < 5; i++)
        {
            Console.Write(fst.next() + " ");
        }
        Console.WriteLine();
        fst.reset();
        for (int i = 0; i < 44; i++)
        {
            fst.next();
        }
        Console.WriteLine(fst.next());
        Console.WriteLine(fst.eos());
        
        Console.WriteLine(rst.next());
        Console.WriteLine(rst.next());

        RandomWordStream rws = new RandomWordStream();
        Console.WriteLine(rws.next());
        Console.WriteLine(rws.next());
        Console.WriteLine(rws.next());
        Console.WriteLine(rws.next());
        Console.WriteLine(rws.next());
    }
}