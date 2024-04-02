// Dominik Szczepaniak

using System;
using System.Collections.Generic;



public class MyDictionary<K, V>
{
    private List<K> keys;
    private List<V> values;

    public MyDictionary()
    {
        keys = new List<K>();
        values = new List<V>();
    }

    public void Add(K key, V value)
    {
        if (ContainsKey(key))
            throw new ArgumentException("Klucz już istnieje w słowniku.");

        keys.Add(key);
        values.Add(value);
    }

    public bool ContainsKey(K key)
    {
        return keys.Contains(key);
    }

    public V Find(K key)
    {
        int index = keys.IndexOf(key);
        if (index == -1)
            throw new KeyNotFoundException("Podany klucz nie istnieje w słowniku.");

        return values[index];
    }

    public void Remove(K key)
    {
        int index = keys.IndexOf(key);
        if (index == -1)
            throw new KeyNotFoundException("Podany klucz nie istnieje w słowniku.");

        keys.RemoveAt(index);
        values.RemoveAt(index);
    }
}



