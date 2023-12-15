var n = 1;
console.log(Object.getPrototypeOf(n)) //typy proste nie maja prototypow
//W przypadku próby dodania pola lub funkcji do wartości typu prostego, takiej jak liczba (w tym przypadku n = 1), JavaScript tymczasowo zamienia wartość prostą w obiekt, umożliwiając operacje na tej wartości jako obiekcie, a następnie usuwa te zmiany po zakończeniu operacji. Jednak ta zmiana nie jest trwała i nie wpływa na sam typ prosty, ponieważ liczby, stringi, booleany itp. nie są obiektami i nie mają właściwości ani metody.
//Dlatego próba przypisania n.foo = 'foo'; jest wykonana, ale nie zostanie trwale zapisana do samej wartości liczby (n). Jeśli spróbujesz wyświetlić n.foo, otrzymasz wynik undefined, ponieważ to pole zostało dodane tymczasowo i nie jest właściwością liczby jako wartości prostej.
n.foo = "foo"
console.log(n.foo)