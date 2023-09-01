``` ini

BenchmarkDotNet=v0.13.5, OS=macOS Ventura 13.2.1 (22D68) [Darwin 22.3.0]
Apple M1, 1 CPU, 8 logical and 8 physical cores
.NET SDK=7.0.202
  [Host]     : .NET 7.0.4 (7.0.423.11508), Arm64 RyuJIT AdvSIMD
  DefaultJob : .NET 7.0.4 (7.0.423.11508), Arm64 RyuJIT AdvSIMD


```
|  Method | x | y | z | t |       Mean |     Error |    StdDev |
|-------- |-- |-- |-- |-- |-----------:|----------:|----------:|
| **DoWork3** | **1** | **2** | **3** | **4** | **46.4068 ns** | **0.0267 ns** | **0.0237 ns** |
| DoWork4 | 1 | 2 | 3 | 4 |  0.0000 ns | 0.0000 ns | 0.0000 ns |
| **DoWork1** | **1** | **3** | **?** | **?** |  **7.0220 ns** | **0.0090 ns** | **0.0075 ns** |
| DoWork2 | 1 | 3 | ? | ? |  0.0015 ns | 0.0010 ns | 0.0009 ns |
