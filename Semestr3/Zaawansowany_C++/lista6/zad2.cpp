#include <iostream>
#include <list>
#include <algorithm>
using namespace std;
class Point {
public:
    double x;
    double y;
    int r; 
    int g; 
    int b; 
    string name;

    Point(double xCoord, double yCoord, int red, int green, int blue, string pointName)
        : x(xCoord), y(yCoord), r(red), g(green), b(blue), name(pointName) {}
};

int main() {
    list<Point> points = {
        {1.5, 2.0, 255, 0, 0, "abc"},
        {3.0, -1.5, 0, 255, 0, "abcd"},
        {-2.5, 1.0, 0, 0, 255, "qwer"},
        {0.0, 0.0, 128, 128, 128, "asdf"},
        {4.5, -2.0, 100, 100, 0, "qwe"},
        {-3.0, 1.5, 255, 255, 0, "ahdfhg"},
        {2.5, -1.0, 0, 255, 255, "hergheg"},
        {0.0, -3.0, 255, 0, 255, "asdfg"},
        {1.0, 2.5, 100, 50, 150, "zxcv"},
        {-2.0, -1.5, 200, 100, 0, "xdecr"},
        {3.5, 0.0, 50, 200, 50, "Poigjfhklnt11"},
        {-1.0, 2.0, 0, 100, 200, "fghklop"},
        {2.0, -3.0, 150, 150, 0, "tioewqtr"},
        {-4.0, 1.0, 50, 150, 100, "ejirojklsdf"},
        {0.5, 2.5, 200, 0, 100, "dsfg"},
        {-2.5, -2.0, 100, 0, 200, "dfhg"},
        {1.0, 1.5, 0, 200, 100, "kjhgf"},
        {2.5, -2.5, 200, 50, 50, "uhbg"},
        {-3.5, 3.0, 150, 100, 50, "uhbnjh"},
        {0.0, 1.0, 100, 200, 0, "cnb"},
        {-1.5, -0.5, 50, 50, 200, "oiuyte"},
        {4.0, 0.5, 150, 0, 100, "tyuq"},
        {-0.5, -1.0, 100, 100, 100, "aklo"},
    };

    // 1. Usuwanie punktów o długich nazwach
    points.remove_if([](const Point& point) {
        return point.name.length() > 5;
    });

    cout << "Punkty po usunięciu punktów o długich nazwach:" << endl;
    for (const auto& point : points) {
        cout << "Nazwa: " << point.name << ", Współrzędne: (" << point.x << ", " << point.y << "), Kolor: (" << point.r << ", " << point.g << ", " << point.b << ")" << endl;
    }

    // 2. Liczenie punktów w poszczególnych ćwiartkach układu współrzędnych
    int q1 = count_if(points.begin(), points.end(), [](const Point& point) {
        return point.x > 0 && point.y > 0;
    });

    int q2 = count_if(points.begin(), points.end(), [](const Point& point) {
        return point.x < 0 && point.y > 0;
    });

    int q3 = count_if(points.begin(), points.end(), [](const Point& point) {
        return point.x < 0 && point.y < 0;
    });

    int q4 = count_if(points.begin(), points.end(), [](const Point& point) {
        return point.x > 0 && point.y < 0;
    });

    cout << "\nLiczba punktów w poszczególnych ćwiartkach:" << endl;
    cout << "I ćwiartka: " << q1 << " punktów" << endl;
    cout << "II ćwiartka: " << q2 << " punktów" << endl;
    cout << "III ćwiartka: " << q3 << " punktów" << endl;
    cout << "IV ćwiartka: " << q4 << " punktów" << endl;

    // 3. Sortowanie punktów ze względu na jasność
    points.sort([](const Point& a, const Point& b) {
        double luminanceA = 0.3 * a.r + 0.59 * a.g + 0.11 * a.b;
        double luminanceB = 0.3 * b.r + 0.59 * b.g + 0.11 * b.b;
        return luminanceA < luminanceB;
    });

    cout << "\nPunkty po posortowaniu ze względu na jasność:" << endl;
    for (const auto& point : points) {
        cout << "Nazwa: " << point.name << ", Współrzędne: (" << point.x << ", " << point.y << "), Kolor: (" << point.r << ", " << point.g << ", " << point.b << ")" << endl;
    }

    // 4. Wybieranie ciemnych punktów
    list<Point> darkPoints;
    copy_if(points.begin(), points.end(), back_inserter(darkPoints), [](const Point& point) {
        double luminance = 0.3 * point.r + 0.59 * point.g + 0.11 * point.b;
        return luminance < 64.0;
    });


    cout << "\nCiemne punkty (luminancja poniżej 64):" << endl;
    for (const auto& point : darkPoints) {
        cout << "Nazwa: " << point.name << ", Współrzędne: (" << point.x << ", " << point.y << "), Kolor: (" << point.r << ", " << point.g << ", " << point.b << ")" << endl;
    }

    return 0;
}
