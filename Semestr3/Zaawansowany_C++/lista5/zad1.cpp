#include <iostream>
#include <forward_list>
#include <string>
#include <queue>
#include <stack>
using namespace std;
enum symbol_rodzaj{
    liczba,
    operatorr,
    funkcja,
    stala,
    nawias
};

class Symbol{
    public:
    symbol_rodzaj rodzaj;
    double wartosc;
    string nazwa;
    int priorytet;
    Symbol(symbol_rodzaj rodzaj, double wartosc, string nazwa, int priorytet) : rodzaj(rodzaj), wartosc(wartosc), nazwa(nazwa), priorytet(priorytet) {}
};

forward_list<Symbol> change(string in){
    forward_list<Symbol> out;
    for(int i = 0; i<in.length(); i++){
        char c = in[i];
        if(c == ' '){
            continue;
        }
        else if(c == '+'){
            out.push_front(Symbol{operatorr, 0, "+", 1});
        }
        else if(c == '-'){
            out.push_front(Symbol{operatorr, 0, "-", 1});
        }
        else if(c == '*'){
            out.push_front(Symbol{operatorr, 0, "*", 2});
        }
        else if(c == '/'){
            out.push_front(Symbol{operatorr, 0, "/", 2});
        }
        else if(c == '^'){
            out.push_front(Symbol{operatorr, 0, "^", 3});
        }
        else if(c == '('){
            out.push_front(Symbol{nawias, 0, "(", 0});
        }
        else if(c == ')'){
            out.push_front(Symbol{nawias, 0, ")", 0});
        }
        else if(c == 's' && i+1 < in.length() && in[i+1] == 'i' && i+2 < in.length() && in[i+2] == 'n' && i+3 < in.length() && in[i+3] == '('){
            out.push_front(Symbol{operatorr, 0, "sin", 4});
            i+=2;
        }
        else if(c == 'c' && i+1 < in.length() && in[i+1] == 'o' && i+2 < in.length() && in[i+2] == 's' && i+3 < in.length() && in[i+3] == '('){
            out.push_front(Symbol{operatorr, 0, "cos", 4});
            i+=2;
        }
        else if(c == 't' && i+1 < in.length() && in[i+1] == 'a' && i+2 < in.length() && in[i+2] == 'n' && i+3 < in.length() && in[i+3] == '('){
            out.push_front(Symbol{operatorr, 0, "tan", 4});
            i+=2;
        }
        else if(c == 'e'){
            out.push_front(Symbol{stala, 2.7182818284590452353602874713527, "e", 0});    
        }
        else if(c=='p' && i+1 < in.length() && in[i+1] == 'i'){
            out.push_front(Symbol{stala, 3.1415926535897932384626433832795, "pi", 0});
            i+=1;
        }
        else{
            if(c >= '0' && c <= '9'){
                string l = "";
                while((c >= '0' && c <= '9') || c=='.'){
                    l += c;
                    i++;
                    c = in[i];
                }
                i--;
                out.push_front(Symbol{liczba, stod(l), l, 0});
            }
            else{
                string nazwa = "";
                while(c >= 'a' && c <= 'z'){
                    nazwa += c;
                    i++;
                    c = in[i];
                }
                i--;
                out.push_front(Symbol{funkcja, 0, nazwa, 4});
            }
        } 
    }
    out.reverse();
    return out;
}

forward_list<Symbol> przeksztalcenie_do_ONP(forward_list<Symbol> infiksowa){
    queue<Symbol> wyjscie;
    stack<Symbol> stos;
    while(!infiksowa.empty()){
        Symbol s = infiksowa.front();
        infiksowa.pop_front();
        if(s.rodzaj == liczba){
            wyjscie.push(s);
        }
        else if(s.rodzaj == stala){
            wyjscie.push(s);
        }
        else if(s.rodzaj == funkcja){
            wyjscie.push(s);
        }
        else if(s.rodzaj == operatorr){
            while(!stos.empty() && stos.top().rodzaj == operatorr && stos.top().priorytet >= s.priorytet){
                wyjscie.push(stos.top());
                stos.pop();
            }
            stos.push(s);
        }
        else if(s.rodzaj == nawias){
            if(s.nazwa == "("){
                // stos.push(s);
                continue;
            }
            else{
                while(!stos.empty() && stos.top().nazwa != "("){
                    wyjscie.push(stos.top());
                    stos.pop();
                }
                if(!stos.empty()){
                    stos.pop();
                }
            }
        }
    }
    while(!stos.empty()){
        wyjscie.push(stos.top());
        stos.pop();
    }
    forward_list<Symbol> odpowiedz;

    for(int i = wyjscie.size(); i>0; i--){
        odpowiedz.push_front(wyjscie.front());
        wyjscie.pop();
    }
    odpowiedz.reverse();
    return odpowiedz;
}

int main(){
    string in = "(2+323)*5-sin(3)+e^2/11+3/2^3+11.11";
    forward_list<Symbol> out = change(in);
    auto test = przeksztalcenie_do_ONP(out);
    for(auto i : test){
        cout << i.nazwa << endl;
    }
    return 0;
}