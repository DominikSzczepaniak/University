class Person2
{
    private string _name;
    private string _surname;
    public delegate void ValueChangedEventHandler(object sender, string PropertyName, object PropertyValue);

    public event ValueChangedEventHandler ValueChanged;

    protected virtual void onValueChanged(string PropertyName, object PropertyValue)
    {
        if (ValueChanged != null) //czym sie rozni Invoke od != null?
        {
            ValueChanged(this, PropertyName, PropertyValue);
        }
        //ValueChanged?.Invoke(this, PropertyName, PropertyValue);
    }

    public string Name
    {
        get
        {
            return _name;
        }
        set
        {
            if (value != _name)
            {
                onValueChanged("Name", value);
            }
            _name = value;


        }
    }
    public string Surname
    {
        get { return _surname; }
        set
        {
            if(value != _surname)
            {
                onValueChanged("Surname", value);
            }
            _surname = value;
        }
    }

    private static void Person_PropertyValueChanged(object source, string PropertyName,  object PropertyValue)
    {
        Console.WriteLine("Wlasciwosc {0}, nowa wartosc {1}", PropertyName, PropertyValue);
    }
 

    public static void Main()
    {
        Person2 person = new Person2();
        person.ValueChanged += Person_PropertyValueChanged;
        person.Name = "imie";
        person.Surname = "nazwisko";
        person.Name = "imie321";
        person.Surname = "nazwisko123";

    }
}