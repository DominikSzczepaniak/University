using System;
using System.Security.Cryptography;
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

namespace MyBenchmarks
{
    public class Program
    {
        [Benchmark]
        [Arguments(1, 3)]
        public dynamic DoWork1(dynamic x, dynamic y) //Mean 7.0336ns
        {
            return x + y;
        }
        [Benchmark]
        [Arguments(1, 3)]
        public int DoWork2(int x, int y) //Mean 0.0021ns
        {
            return x + y;
        }
        [Benchmark]
        [Arguments(1,2,3,4)]
        public dynamic DoWork3(dynamic x, dynamic y, dynamic z, dynamic t) //Mean 46.4068ns
        {
            return x * y * t + z * x - z * y;
        }
        [Benchmark]
        [Arguments(1,2,3,4)]
        public int DoWork4(int x, int y, int z, int t)//The method duration is indistinguishable from the empty method duration
        {
            return x * y * t + z * x - z * y;
        }
        public static void Main(string[] args)
        {
            var summary = BenchmarkRunner.Run<Program>();
        }
    }
}
