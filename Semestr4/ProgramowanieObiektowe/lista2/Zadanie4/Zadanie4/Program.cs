using System;
using System.Collections.Generic;

public class LazyIntList
{
    private List<int> _elements;

    public LazyIntList()
    {
        _elements = new List<int>();
    }

    public int Element(int i)
    {
        while (_elements.Count <= i)
        {
            _elements.Add(_elements.Count);
        }

        return _elements[i];
    }

    public int Size()
    {
        return _elements.Count;
    }
}

public class LazyPrimeList : LazyIntList
{
    private List<int> _primes;

    public LazyPrimeList() : base()
    {
        _primes = new List<int>();
    }

    public new int Element(int i)
    {
        while (_primes.Count <= i)
        {
            int currentNumber = _primes.Count > 0 ? _primes[_primes.Count - 1] + 1 : 2;
            while (!IsPrime(currentNumber))
            {
                currentNumber++;
            }
            _primes.Add(currentNumber);
        }

        return _primes[i];
    }

    private bool IsPrime(int number)
    {
        if (number <= 1)
            return false;
        for (int i = 2; i * i <= number; i++)
        {
            if (number % i == 0)
            {
                return false;
            }
        }
        return true;
    }
}

class Program
{
    static void Main(string[] args)
    {
        LazyIntList list = new LazyIntList();
        Console.WriteLine(list.Size()); 
        Console.WriteLine(list.Element(40)); 
        Console.WriteLine(list.Size()); 
        Console.WriteLine(list.Element(38)); 
        Console.WriteLine(list.Size()); 
        
        LazyPrimeList primeList = new LazyPrimeList();
        Console.WriteLine(primeList.Element(0)); 
        Console.WriteLine(primeList.Element(1)); 
        Console.WriteLine(primeList.Element(2)); 
        Console.WriteLine(primeList.Element(3)); 
        Console.WriteLine(primeList.Element(4)); 
        Console.WriteLine(primeList.Element(5));  
        Console.WriteLine(primeList.Element(10)); 
        Console.WriteLine(primeList.Element(15)); 
    }
}