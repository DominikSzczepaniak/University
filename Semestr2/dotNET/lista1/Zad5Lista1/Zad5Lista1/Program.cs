using System;
using System.Collections.Generic;
namespace Zadanie5Lista1;
/// <summary>
///  Klasa tworząca siątkę dwuwiarową grid.
/// </summary>


public class Grid
{
    int[,] gridtab = new int[5, 5];
    int rows = 0;
    int columns = 0;
    public Grid(int columns, int rows)
    {
        gridtab = new int[columns, rows];
        this.columns = columns;
        this.rows = rows;
    }
    /// <summary>
    /// Indekser zwracający wiersz o id index1
    /// </summary>
    /// <param name="index1">Wiersz siatki</param>
    /// <returns>int[] array</returns>
    public int[] this[int index1]
    {
        get
        {
            int[] returnarray = new int[rows];
            for (int i = 0; i < rows; i++)
            {
                returnarray[i] = gridtab[index1, i];
            }
            return returnarray;
        }
    }
    /// <summary>
    /// Indekser zwracający wartość w komórce gridtab[index1, index2] i ustawiający komórkę gridtab[index1, index2] na wartość podaną przez użytkownika.
    /// </summary>
    /// <param name="index1">Wiersz siatki</param>
    /// <param name="index2">Kolumna siatki</param>
    /// <returns>int - wartość z gridtab[index1, index2]</returns>
    public int this[int index1, int index2]
    {
        get
        {
            return gridtab[index1, index2];
        }
        set
        {
            gridtab[index1, index2] = value;
        }
    }
}
class main
{
    public static void Main(String[] args)
    {
        Grid g1 = new Grid(4, 4);
        g1[1, 1] = 5;
        g1[1, 2] = 3;
        g1[1, 3] = 4;
        int element = g1[1, 3];
        int[] row1 = g1[1];
        for (int i = 0; i < 4; i++)
        {
            Console.Write(row1[i] + " ");
        }
        Console.WriteLine();
        Console.WriteLine(element);
        Console.Read();
    }
}
