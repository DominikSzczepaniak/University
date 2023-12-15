// InnyPlik.ts
import Foo from './zad4'; // Importowanie eksportu domyślnego z pliku 'Foo.ts'

const mojaZmienna = new Foo(); // Utworzenie instancji klasy Foo

// InnyPlik.ts
import { Bar, someFunction, someVariable } from './zad4'; // Importowanie eksportów nazwanych z pliku 'Bar.ts'

const mojaZmienna2 = new Bar(); // Utworzenie instancji klasy Bar
someFunction(); // Wywołanie funkcji someFunction
console.log(someVariable); // Wyświetlenie wartości zmiennej someVariable

