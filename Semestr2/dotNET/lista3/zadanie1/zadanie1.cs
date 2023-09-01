using System;
using System.Xml;

public interface IClassInfo
{
    string[] GetFieldNames();
    object GetFieldValue( string fieldName );
}

public class Person : IClassInfo
{
    public string Name { get; set; }
    public string Surname { get; set; }
    public int Wiek { get; set; }
    public int ID { get; set; }

    public string[] GetFieldNames()
    {
        return new[] { "Name", "Surname", "Wiek", "ID" };
    }

    public object GetFieldValue(string fieldName)
    {
        switch (fieldName)
        {
            case "Name":
                return this.Name;
            case "Surname":
                return this.Surname;
            case "Wiek":
                return this.Wiek;
            case "ID":
                return this.ID;
            default:
                return null;
        }

        throw new NotImplementedException();
    }
}

public class XMLGenerator
{
    public string GenerateXML(IClassInfo dataObject)
    {
        // Tworzenie nowego dokumentu XML
        XmlDocument doc = new XmlDocument();
        XmlElement root = doc.CreateElement("root");
        doc.AppendChild(root);

        // Dodawanie elementów do dokumentu na podstawie informacji o polach klasy
        string[] fieldNames = dataObject.GetFieldNames();
        foreach (string fieldName in fieldNames)
        {
            object fieldValue = dataObject.GetFieldValue(fieldName);

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
            ID = 11
        };
        XMLGenerator generator = new XMLGenerator();
        string xml = generator.GenerateXML(person);
        Console.WriteLine(xml);
    }
}



