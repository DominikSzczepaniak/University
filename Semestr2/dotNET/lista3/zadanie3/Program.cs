using System;
using System.ComponentModel;
using System.Reflection;
using System.Xml;

public class IgnoreInXML : System.Attribute { }

public class Person
{
    public string Name { get; set; }
    public string Surname { get; set; }
    [IgnoreInXML]
    public int Wiek { get; set; }
    public int ID { get; set; }
}

public class XMLGenerator
{
    public string GenerateXML(object dataObject)
    {
        var prop = dataObject.GetType().GetProperties();
        List<string> fieldNames = new List<string>();
        for (int i = 0; i < prop.Length; i++)
        {
            //sprawdzamy czy nasz property ma atrybut o nazwie IgnoreInXML
            var hasIgnoreInXml = dataObject.GetType().GetProperty(prop[i].Name).GetCustomAttribute<IgnoreInXML>();
            if (hasIgnoreInXml is IgnoreInXML)
            {
                continue;
            }
            fieldNames.Add(prop[i].Name);
        }
        
        XmlDocument doc = new XmlDocument();
        XmlElement root = doc.CreateElement("root");
        doc.AppendChild(root);
        foreach (string fieldName in fieldNames)
        {
            var fieldValue = dataObject.GetType().GetProperty(fieldName).GetValue(dataObject, null);
            XmlElement fieldElement = doc.CreateElement(fieldName);
            fieldElement.InnerText = fieldValue.ToString();
            root.AppendChild(fieldElement);
        }
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