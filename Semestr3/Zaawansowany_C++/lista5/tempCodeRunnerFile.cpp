#include <iostream>
#include <forward_list>
#include <string>
using namespace std;
enum symbol_rodzaj{
    liczba,
    operatorr,
    funkcja,
    stala
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
        cout << c << endl;
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
            out.push_front(Symbol{operatorr, 0, "(", 0});
        }
        else if(c == ')'){
            out.push_front(Symbol{operatorr, 0, ")", 0});
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
                while(c >= '0' && c <= '9'){
                    l += c;
                    i++;
                    c = in[i];
                }
                out.push_front(Symbol{liczba, stod(l), l, 0});
            }
            else{
                string nazwa = "";
                while(c >= 'a' && c <= 'z'){
                    nazwa += c;
                    i++;
                    c = in[i];
                }
                out.push_front(Symbol{funkcja, 0, nazwa, 4});
            }
        } 
    }
    return out;
}

int main(){
    string in = "sin(2+3)";
    forward_list<Symbol> out = change(in);
    for(auto i : out){
        cout << i.rodzaj << " " << i.wartosc << " " << i.nazwa << " " << i.priorytet << endl;
    }
    return 0;
}