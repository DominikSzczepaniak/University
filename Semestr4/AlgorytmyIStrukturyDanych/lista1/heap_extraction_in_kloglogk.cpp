#include <iostream>
#include <queue>
#include <tgmath.h>
#include <stack>
#include <algorithm>
using namespace std;
const int MAXN = 64;
int CLANSIZE = 0;
int k;
int heap[MAXN];
#define vec vector<pair<int, int>>

struct ComparePairs {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        return a.first > b.first; 
    }
};

#define pq priority_queue<pair<int, int>, vector<pair<int, int>>, ComparePairs>

struct clan_info{
    vec clan;
    pq os_last;
    pq pr_last;
};

void wypisz_klan(vec& clan){
    for(auto i : clan){
        cout << i.first << " ";
    }
    cout << endl;
}

void wypisz_pq(pq prq){
    while(!prq.empty()){
        cout << prq.top().first << " ";
        prq.pop();
    }
    cout << endl;
}

clan_info create_next_clan(pq os_last, pq pr_last){
    if(os_last.empty()){
        return {};
    }
    //debug =============
    // cout << "Szukam dla os: ";
    // wypisz_pq(os_last);
    // cout << endl;
    //debug =============
    vec clan;
    pq current_values = os_last;
    pq os_return;
    int done_nodes = 0;
    while(!current_values.empty() && done_nodes != CLANSIZE){
        pair<int, int> front_element = current_values.top(); //wyciagamy logk razy dla jednego klanu ktorego wielkosc jest logk, wiec zlozonosc loglogk, a klanow jest logk, wiec ogolna zlozonosc O(logk * loglog k)
        int id = front_element.second;
        current_values.pop();
        if(front_element == os_last.top()){
            os_last.pop();
        }
        if(!os_return.empty() && front_element == os_return.top()){
            os_return.pop();
        }
        done_nodes++;
        clan.push_back(front_element);
        if(heap[id*2] != 0){
            current_values.push({heap[id*2], id*2});
            os_return.push({heap[id*2], id*2});
        }
        if(heap[id*2+1] != 0){
            current_values.push({heap[2*id+1], 2*id+1});
            os_return.push({heap[2*id+1], 2*id+1});
        }
    }
    // //debug =============
    // cout << "Wynik: " << endl;
    // cout << "Klan: ";
    // wypisz_klan(clan);
    // cout << endl;
    // cout << "os: ";
    // wypisz_pq(os_return);
    // cout << endl;
    // cout << "pr: ";
    // wypisz_pq(os_last);
    // cout << endl;
    // //debug =============
    if(clan.size() != CLANSIZE){
        return {};
    }
    return {clan, os_return, os_last};

}

int create_clans(){
    //clan 1 is dijkstra on CLANSIZE elements, add every visited node to some priority_queue called os1
    // dijkstra is E logV
    // but we are looking at small size log
    // so its logE loglogV -> logk loglogK 
    // czyli dla sformowania k/logk klanow mamy k/logk * logk*loglogk = kloglogk
    //clan 1 is created independetly

    // of i pr moze byc co najwyzej 2 logk i 2logk - 1 (-1 bo dla C1 nie ma)
    pq clan1_candidates; //loglogk
    vector<pair<int, int>> clan1;
    int done_clan1 = 0;
    clan1_candidates.push({heap[1], 1});
    while(done_clan1 != CLANSIZE){
        // cout << "done_clan: " << done_clan1 << " ";
        // wypisz_pq(clan1_candidates);
        pair<int, int> front_element = clan1_candidates.top();
        int id = front_element.second;
        clan1_candidates.pop();
        done_clan1++;
        clan1.push_back(front_element);
        clan1_candidates.push({heap[id*2], id*2});
        clan1_candidates.push({heap[2*id+1], 2*id+1});
    }
    pq os_last = clan1_candidates;
    pq pr_last;

    vector<vec> all_clans;
    all_clans.push_back(clan1);
    int wielkosc_petli = ceil(double(k) / floor(log2(k)));

    pq H1;
    H1.push(clan1[0]);

    int clan_number = 1;
    pair<int, int> last_number = clan1.back();
    stack<pq> oss;
    for(int i = 0; i<=wielkosc_petli; i++){
        if(os_last.empty()){
            while(os_last.empty()){
                os_last = oss.top();
                oss.pop();
            }
        }

        //debug =============
        // cout << "wypisuje h1 dla i = " << i << ": ";
        // wypisz_pq(H1);
        //debug =============

        pair<int, int> extractmin_element = H1.top();
        //extract_min jest wykonywany k / logk razy, wiec O(k)
        H1.pop();
        //gdy wyciagamy ten element to wiemy, ze kazdy element < od tego byl juz w kazdmy z innych kopcow
        //dlaczego? Zalozmy ze istnieje element mniejszy ktory nie zostal jeszcze wybrany, no ale to nie moze byc prawda, bo jezeli taki element by istnial to zostalby wybrany przez kolejke priorytetowa szybciej, stad bylby w innym zbiorze.

        // po wyjeciu najmniejszego elementu C_j co najwyzej 2j klanow moze byc stworzonych, wiec po wykonaniu k/logk wyjeciu najmniejszego elementu, x sa mniej niz 2*(k+logk) elementow w kazdym innym klanie
        //skoro ostatnie dwa klany sa tworzone przez wyjecie x, wszystkie elementy w tych klanach sa wieksze od niego. Stad 2k elementow jest <= x
        last_number = extractmin_element;
        clan_info new_clan = create_next_clan(os_last, pr_last);

        // debug =============
        // cout << "wpyisane: " << last_number.first << endl;
        // wypisz_klan(new_clan.clan);
        // wypisz_pq(new_clan.os_last);
        // wypisz_pq(new_clan.pr_last);
        // debug =============


        // all_clans.push_back(new_clan.clan);
        if(!new_clan.clan.empty()){
            H1.push({new_clan.clan[0]});    
        }
        oss.push(new_clan.os_last);
        if(!pr_last.empty()){
            pq dummy;
            // //debug =============
            // cout << "pr istnieje" << endl;
            // wypisz_pq(pr_last);
            // //debug =============

            clan_info pr_clan = create_next_clan(pr_last, dummy);
            all_clans.push_back(pr_clan.clan);
            // //debug =============
            // wypisz_klan(pr_clan.clan);
            // wypisz_pq(pr_clan.os_last);
            // wypisz_pq(pr_clan.pr_last);
            // //debug =============
            H1.push({pr_clan.clan[0]});
            pr_last = pr_clan.pr_last;
            os_last = pr_clan.os_last;
        }
        else{
            pr_last = new_clan.pr_last;
            os_last = new_clan.os_last;
            oss.pop();
        }
        
        
        // clan_info krok = create_next_clan(os_last, pr_last);


        //na tamtym kopcu przykladowym:
        //H2 = <1, 2, 3, 4, 7>
        //C1 = [1, 2, 3]
        //os(C1) = <4, 7, 10, 12> = os_last
        //pr(C1) = [] = pr_last
        // H2 = <4, 7, 10, 12> = os_last

        // tworzymy pusty heap z najwiekszym elementem z C1 - 3
        // H1 = <3>
        // ceil(k/floor(logk)) robimy:
        // wyjmij najmniejszy element z H1 - 3
        // C_2 jest reprezentowany przez 3

        // za pomocą H2 (czyli os(C1)) znajdujemy log_k najmniejszych elementow
        //H2 = <4, 7, 10, 12> + <5, 8> - <4> = <5, 7, 8, 10, 12>
        //C2 = [4]
        //H2 = <5, 7, 8, 10, 12> + <6, 11> - <5> = <6, 7, 8, 10, 11, 12>
        //C2 = [4, 5]
        // H2 = <6, 7, 8, 10, 11, 12> + <17, 19> - <6> = <7, 8, 10, 11, 12, 17, 19>
        //C2 = [4, 5, 6]
        // os(C2) = roznica miedzy H2 i os(C1) : <7, 8, 10, 11, 12, 17, 19> - <4, 7, 10, 12> = <8, 11, 17, 19>
        // pr(C2) = czesc wspolna miedzy os(C1) i H2 : <4, 7, 10, 12> czWS <7, 8, 10, 11, 12, 17, 19> = <7, 10, 12>

        //jeśli pr(C_j (tutaj C_2)) nie jest puste to:
        //szukanie rekurencja na pr i robimy C_3 (C_i+1)

        // wrzucamy do H1 minimalny element z C_2 i C_3 i dajemy petli działać

        





    }

    // cout << "k-ty: " << last_number.first << endl;
    return last_number.first; //miedzy k a 2k
    //robimy k/logk razy petle w ktorej tworzymy klany.
    //k/logk * logk (kazdy klan ma rozmiar logk robimy to tyle razy) = k, wiec dostaniemy k elementow

    //co najwyzej zrobimy 2 * klogk + 1 klanow (dla kazdego moze istniec os i pr)



    //dowod jest, ze kloglogk - przeczytaj


    //klan tworzymy tak:
    // clan_info ans = create_next_clan(os_last, pr_last);
    //robimy albo dwa klany - jesli !ans.pr.empty()
    //albo jeden jesli ans.pr.empty()

}


void example_heap(){
    heap[1] = 1;
    heap[2] = 2;
    heap[3] = 4;
    heap[4] = 7;
    heap[5] = 3;
    heap[6] = 8;
    heap[7] = 5;
    heap[8] = 15;
    heap[9] = 9;
    heap[10] = 10;
    heap[11] = 12;
    heap[12] = 26;
    heap[13] = 13;
    heap[14] = 11;
    heap[15] = 6;
    heap[16] = 43;
    heap[17] = 22;
    heap[18] = 16;
    heap[19] = 32;
    heap[20] = 18;
    heap[21] = 28;
    heap[22] = 38;
    heap[23] = 49;
    heap[24] = 29;
    heap[25] = 63;
    heap[26] = 21;
    heap[27] = 79;
    heap[28] = 20;
    heap[29] = 14;
    heap[30] = 17;
    heap[31] = 19;
    return;
}

vector<int> answer;

void dfs(int s, int waga){
    answer.push_back(heap[s]);
    int left_son_value = heap[2*s];
    int right_son_value = heap[2*s+1];
    if(left_son_value <= waga){
        dfs(2*s, waga);
    }
    if(right_son_value <= waga){
        dfs(2*s+1, waga);
    }
}

int main(){
    example_heap();
    cin >> k;
    CLANSIZE = floor(log2(k));
    int search_until = create_clans();
    dfs(1, search_until);
    nth_element(answer.begin(), answer.begin() + k - 1, answer.end());
    std::cout << "k-ty element to: " << answer[k - 1] << std::endl;
    for(auto i : answer){
        if(i <= k){
            cout << i << " ";
        }
    }
    cout << endl;
    return 0;
}


