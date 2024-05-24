function Fx = mojaDystrybuantaRomberg(x, mu, sigma, k)
    % mojaDystrybuantaRomberg - Oblicza dystrybuantę rozkładu normalnego z parametrami mu i sigma
    % za pomocą metody Romberga.
    %   x - punkt, w którym dystrybuanta jest obliczana
    %   mu - średnia rozkładu normalnego
    %   sigma - odchylenie standardowe rozkładu normalnego
    %   k - głębokość iteracji Romberga (zazwyczaj 4-6 jest wystarczające)
    %
    % Przykład użycia:
    %   Fx = mojaDystrybuantaRomberg(0.5, 0, 1, 4)
    
    % Zakres całkowania od -inf do x, ale ograniczymy go do wartości znacznie mniejszej niż mu
    a = mu - 10 * sigma;  
    b = x;
    
    % Inicjalizacja tablicy Romberga
    R = zeros(k, k);
    h = (b - a);
    R(1, 1) = (h / 2) * (normalnaGestosc(a, mu, sigma) + normalnaGestosc(b, mu, sigma));

    % Wypełnienie pierwszej kolumny metodą trapezów
    for j = 2:k
        h = h / 2;
        sum = 0;
        for i = 1:2^(j-2)
            sum = sum + normalnaGestosc(a + (2*i-1)*h, mu, sigma);
        end
        R(j, 1) = 0.5 * R(j-1, 1) + h * sum;
    end

    % Ekstrapolacja Richardsona dla osiągnięcia wyższych rzędów dokładności
    for i = 2:k
        for j = 2:i
            R(i, j) = R(i, j-1) + (R(i, j-1) - R(i-1, j-1)) / (4^(j-1) - 1);
        end
    end

    % Wynik znajduje się w R(k, k)
    Fx = R(k, k);
end

function y = normalnaGestosc(x, mu, sigma)
    % normalnaGestosc - Oblicza wartość funkcji gęstości rozkładu normalnego
    % dla danych mu (średnia) i sigma (odchylenie standardowe)
    y = mojaExp(1)^(-0.5 * ((x - mu) / sigma)^2) / (sigma * sqrt(2 * pi));
end

function y = mojaExp(x)
    % mojaExp - Oblicza wartość e^x korzystając z szeregu Taylora
    %   x - punkt, w którym funkcja eksponencjalna jest obliczana
    %
    % Przykład użycia:
    %   y = mojaExp(1)  % oblicza e^1

    % Ustalamy liczbę składników szeregu, większa liczba daje większą dokładność
    n = 20;  % Dobra równowaga między dokładnością a wydajnością
    
    gora = 1;  % e^0 = 1, zaczynamy od pierwszego wyrazu
    silnia = 1;  % 0! = 1
    wynik = 1;
    for i = 1:n
        silnia = silnia * i;  % Obliczanie i!
        gora = gora * x;  % Dodanie kolejnego wyrazu szeregu
        wynik = wynik + gora/silnia;
    end
    
    y = wynik;
end


mojaDystrybuantaRomberg(7, 5, 10, 6)