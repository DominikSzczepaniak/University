using System.Runtime.CompilerServices;
using System.Timers;

namespace Test
{
    public static class TaskExtensions
    {
        public static TaskAwaiter GetAwaiter(this int miliseconds)
        {
            //Thread.Sleep(2000);
            return Task.Delay(miliseconds).GetAwaiter();
        }

        public static Task Delay(int miliseconds)
        {
            TaskCompletionSource<object> tcs = new TaskCompletionSource<object>();
            System.Timers.Timer t = new System.Timers.Timer();
            t.Interval = miliseconds;
            t.Elapsed += (source, e) =>
            {
                t.Stop();
                t.Dispose();
                tcs.SetResult(null);
            };
            t.Start();
            return tcs.Task;
        }
    }

    class Program 
    {
        public static async Task Main()
        {
            
            Console.WriteLine(1);
            await 2000;
            Console.WriteLine(2);
            Console.ReadLine();
        }
    }
}