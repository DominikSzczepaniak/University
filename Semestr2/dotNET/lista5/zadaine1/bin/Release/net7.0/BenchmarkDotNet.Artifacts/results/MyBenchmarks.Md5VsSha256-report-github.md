``` ini

BenchmarkDotNet=v0.13.5, OS=macOS Ventura 13.2.1 (22D68) [Darwin 22.3.0]
Apple M1, 1 CPU, 8 logical and 8 physical cores
.NET SDK=7.0.202
  [Host]     : .NET 7.0.4 (7.0.423.11508), Arm64 RyuJIT AdvSIMD
  DefaultJob : .NET 7.0.4 (7.0.423.11508), Arm64 RyuJIT AdvSIMD


```
| Method |      Mean |     Error |    StdDev |
|------- |----------:|----------:|----------:|
| Sha256 |  6.966 μs | 0.0062 μs | 0.0058 μs |
|    Md5 | 31.019 μs | 0.0932 μs | 0.0778 μs |
