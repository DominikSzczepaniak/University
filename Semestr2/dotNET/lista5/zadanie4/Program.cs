using System.Runtime.CompilerServices;
using System.Timers;

namespace Test
{
    public static class TaskExtensions
    {

        public static TaskAwaiter<object> GetAwaiter(this string url)
        {
            return Delay(url).GetAwaiter();
        }

        public static Task<object> Delay(string url)
        {
            TaskCompletionSource<object> tcs = new TaskCompletionSource<object>();
            System.Timers.Timer t = new System.Timers.Timer();
            HttpClient Client = new HttpClient();
            var result = Client.GetAsync(url);
            var test = result.Result;
            tcs.SetResult(result.Result.ToString());
            return tcs.Task;
        }
    }

    class Program 
    {
        public static void Main()
        {
            Test();
        }
        private static async void Test()
        {
            Console.WriteLine(1);
            Console.WriteLine(await "https://www.google.com");
            Console.WriteLine(1);
        }
    }
}