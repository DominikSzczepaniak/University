#include <iostream>
#include <cmath>

double f(double x){
    return x - 0.49;
}
//alfa jest rowna 0.49 bo lim n->inf m_{n+1} dazy do 0.49
//wyniki sa wiarygodne, nie mamy problemow z ucinaniem miejsc znaczacych dla pierwszych 5 krokow
int main(){
    double a = 0;
    double b = 1;
    int ilosc_krokow = 5;
    for(int i = 0; i<ilosc_krokow; i++){
        double m = 0.5 * (a + b);
        double wartosc = f(m);
        double e_n = 0.49 - m;
        std::cout << "Dla kroku: " << i << " wartosc e_n rowna jest " << 0.49 - m << " a szacowana była z gory poprzez: " << pow(2, -i-1) << std::endl;
        if(wartosc < 0){
            a = m;
        }
        else{
            b = m;
        }
    }

}