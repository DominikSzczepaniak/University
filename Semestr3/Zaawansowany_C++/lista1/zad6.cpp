#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double a, b, c;
    cout << "a ";
    cin >> a;
    cout << "b ";
    cin >> b;
    cout << "c ";
    cin >> c;
    if (double delta = b * b - 4 * a * c)
    {
        double x1 = (-b + sqrt(delta)) / (2 * a);
        double x2 = (-b - sqrt(delta)) / (2 * a);
        cout << "pierwiastki x1 = " << x1 << ", x2 = " << x2 << endl;
    }
    else if (delta == 0)
    {
        double x = -b / (2 * a);
        cout << "pierwiastek x = " << x << endl;
    }
    else
    {
        cout << "brak peirwiastkow" << endl;
    }

    return 0;
}