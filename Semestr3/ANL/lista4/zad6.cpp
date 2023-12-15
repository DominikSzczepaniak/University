// Chcemy miec y = 1/sqrt(a)
//  Wiec y^2 = 1/a
//  a = 1/y^2
//  1/y^2 - a = 0
//  f(y) = 1/y^2 - a
//  f'(y) = -2/y^3

// mamy wiec
//  y_{n+1} = y_n * (1/y^2 - a) / (-2/y^3)
// https://www.wolframalpha.com/input?i2d=true&i=y+-+Divide%5BDivide%5B1%2CPower%5By%2C2%5D%5D-a%2C-Divide%5B2%2CPower%5By%2C3%5D%5D%5D
#include <iomanip>
#include <iostream>
double licz(float y, float a)
{
    double val = y * (3 - a * y * y);
    return 0.5 * val;
}

float Q_rsqrt(float x)
{
    float xhalf = 0.5f * x;
    int i = *(int*)&x; 
    i = 0x5f375a86 - (i >> 1); 
    //https://www.lomont.org/papers/2003/InvSqrt.pdf
    x = *(float*)&i; 
    x = x * (1.5f - xhalf * x * x);
    x = x * (1.5f - xhalf * x * x); 
    return x;
}

int main()
{
    std::cout << std::setprecision(100);
    //na drodze eksperymentu takie wartosci, 
    double a = 20;
    double y0 = a >= 10 ? (1 / (0.3 * a)) : 0.5;
    for (int i = 0; i < 30; i++) 
    {
        y0 = licz(y0, a);
    }
    std::cout << "Gorszy: " << y0 << std::endl;
    double w = Q_rsqrt(a);
    std::cout << "Lepszy: " << w << std::endl;
}