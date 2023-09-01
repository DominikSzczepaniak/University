using System;
using System.ComponentModel;
using System.Reflection;
using System.Xml;

public class Person
{
    public string Name { get; set; }
    public string Surname { get; set; }
    public int Wiek { get; set; }
    public int ID { get; set; }
}

public class XMLGenerator
{
    public string GenerateXML(object dataObject)
    {
        //Pobieranie nazw pól
        var prop = dataObject.GetType().GetProperties();
        string[] fieldNames = new string[prop.Length];
        for (int i = 0; i < prop.Length; i++)
        {
            fieldNames[i] = prop[i].Name;
        }
        
        // Tworzenie nowego dokumentu XML   
        XmlDocument doc = new XmlDocument();
        XmlElement root = doc.CreateElement("root");
        doc.AppendChild(root);
        // Dodawanie elementów do dokumentu na podstawie informacji o polach klasy
        foreach (string fieldName in fieldNames)
        {
            var fieldValue = dataObject.GetType().GetProperty(fieldName).GetValue(dataObject, null); 

            // Dodawanie elementu o nazwie pola i wartości z pola
            XmlElement fieldElement = doc.CreateElement(fieldName);
            fieldElement.InnerText = fieldValue.ToString();
            root.AppendChild(fieldElement);
        }

        // Zwracanie dokumentu XML jako ciągu znaków
        return doc.OuterXml;
    }
}

class Program
{
    public static void Main()
    {
        Person person = new Person()
        {
            Name = "Jan",
            Surname = "Kowalski",
            Wiek = 31,
            ID = 51
        };
        XMLGenerator generator = new XMLGenerator();
        string xml = generator.GenerateXML(person);
        Console.WriteLine(xml);
    }
}



