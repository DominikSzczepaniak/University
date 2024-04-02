using System;

public class Wektor
{
    private float[] wspolrzedne;

    public Wektor(int wymiar)
    {
        wspolrzedne = new float[wymiar];
    }

    public float this[int index]
    {
        get { return wspolrzedne[index]; }
        set { wspolrzedne[index] = value; }
    }

    public static Wektor operator +(Wektor v1, Wektor v2)
    {
        if (v1.wspolrzedne.Length != v2.wspolrzedne.Length)
            throw new ArgumentException("Wektory muszą być tego samego wymiaru.");

        Wektor suma = new Wektor(v1.wspolrzedne.Length);
        for (int i = 0; i < v1.wspolrzedne.Length; i++)
        {
            suma[i] = v1[i] + v2[i];
        }
        return suma;
    }

    public static float operator *(Wektor v1, Wektor v2)
    {
        if (v1.wspolrzedne.Length != v2.wspolrzedne.Length)
            throw new ArgumentException("Wektory muszą być tego samego wymiaru.");

        float iloczynSkalarny = 0;
        for (int i = 0; i < v1.wspolrzedne.Length; i++)
        {
            iloczynSkalarny += v1[i] * v2[i];
        }
        return iloczynSkalarny;
    }

    public static Wektor operator *(Wektor v, float skalar)
    {
        Wektor iloczyn = new Wektor(v.wspolrzedne.Length);
        for (int i = 0; i < v.wspolrzedne.Length; i++)
        {
            iloczyn[i] = v[i] * skalar;
        }
        return iloczyn;
    }

    public float Norma()
    {
        float sumaKwadratow = 0;
        foreach (float wspolrzedna in wspolrzedne)
        {
            sumaKwadratow += wspolrzedna * wspolrzedna;
        }
        return (float)Math.Sqrt(sumaKwadratow);
    }
}

