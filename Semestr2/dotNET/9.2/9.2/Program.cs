using System;
using System.Threading;

class Program
{
    static SemaphoreSlim barberSemaphore = new SemaphoreSlim(0);
    static SemaphoreSlim customerSemaphore = new SemaphoreSlim(0);
    static SemaphoreSlim seatSemaphore = new SemaphoreSlim(1);

    static int numCustomersWaiting = 0;

    static void Barber()
    {
        while (true)
        {
            barberSemaphore.Wait();

            seatSemaphore.Release();

            Console.WriteLine("Barber is cutting hair");

            Thread.Sleep(2000);

            Console.WriteLine("Barber finished cutting hair");

            customerSemaphore.Release();
        }
    }

    static void Customer(int customerNum)
    {
        seatSemaphore.Wait();

        if (numCustomersWaiting < 3)
        {
            numCustomersWaiting++;

            Console.WriteLine("Customer {0} is waiting", customerNum);

            seatSemaphore.Release();

            barberSemaphore.Release();
            customerSemaphore.Wait();

            Console.WriteLine("Customer {0} is getting a haircut", customerNum);

            Thread.Sleep(2000);

            Console.WriteLine("Customer {0} finished the haircut", customerNum);
        }
        else
        {
            seatSemaphore.Release();

            Console.WriteLine("Customer {0} is leaving, no seats available", customerNum);
        }
    }

    static void Main(string[] args)
    {
        Thread barberThread = new Thread(Barber);
        barberThread.Start();

        for (int i = 0; i < 10; i++)
        {
            Thread customerThread = new Thread(() => Customer(i));
            customerThread.Start();

            Thread.Sleep(1000);
        }

        Console.ReadLine();
    }
}
