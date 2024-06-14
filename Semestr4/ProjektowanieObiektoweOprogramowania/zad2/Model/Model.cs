using System.Collections.Generic;

namespace SimpleTaskManager.Domain
{

    public class Parent
    {
        public int id { get; set; }
        public string imie { get; set; }
        public string nazwisko { get; set; }
        public ICollection<Child> Children { get; set; }
    }

    public class Child
    {
        public int id { get; set; }
        public string imie { get; set; }
        public string nazwisko { get; set; }
        public int id_parent { get; set; }
        public Parent Parent { get; set; }
    }
}