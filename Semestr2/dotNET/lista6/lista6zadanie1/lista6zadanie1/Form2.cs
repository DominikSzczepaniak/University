using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lista6zadanie1
{
    public partial class Form2 : Form
    {
        public string nazwa { get; set; }
        public string adres { get; set; }
        public string cykl { get; set; }
        public string rodzaj { get; set; }
        public Form2()
        {
            InitializeComponent();
        }
        public Form2(string nazwa, string adres, string cykl, string rodzaj) : this()
        {
            this.nazwa = nazwa;
            this.adres = adres;
            this.cykl = cykl;
            this.rodzaj = rodzaj;
            label1.Text = nazwa;
            label2.Text = adres;
            label3.Text = "Studia " + cykl;
            label4.Text = rodzaj;
        }
        
    }
}
