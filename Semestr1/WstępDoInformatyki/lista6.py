from wdi import *
def zad1():
    #zad 1 
    # {  x=a[i];
    #              lewy=0;
    #              prawy=i-1;
    #              while (lewy<prawy) {
    #                k=(lewy+prawy)/2; //dzielenie całkowite!
    #                if (a[k]<x) lewy=k+1;
    #                else prawy=k;
    # } 
    #kontprzyklad: 0 2 1
    # lewy = 0
    # prawy = 1
    # k = 0
    # a[k] < 1
    # lewy = 0
    # prawy = 0
    # ...
    pass
def zad2():
    #a)
    def selSort(A):
        for i in range(len(A)):
            min_idx = i
            for j in range(i+1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j      
            A[i], A[min_idx] = A[min_idx], A[i]
    #b) dwie iteracji o dlugosci n
    #c) duza instrukcja n^2
    #d) a1<a2<...<an - n*(n-1) porownan, 0 podstawien
    #   a1>a2>a3>...>an n*n-1 porownan 2*n*n-1 podstawien 
def zad3():
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    #b) dwie petle
    #c) dwie petla
    #d) a1<a2<...<an - n*(n-1) porownan, 0 podstawien
    #   a1>a2>a3>...>an n*n-1 porownan 2*n*n-1 podstawien  
def zad5():
    #specyfikacja:
    #wejscie: liczba n
    #wyjscie: tablica s w której 1 oznacza ze liczbaj est liczba pierwsza, a 0 oznacza ze nie jest
    def sito(n):
        s = Array(n+1)
        for i in range(n+1):
            s[i] = 1
        s[0] = s[1] = 0
        for i in range(2, n+1):
            if(s[i] == 0):
                continue 
            for j in range(i+i, n+1):
                s[j] = False 
        return s
def zad6():
    

