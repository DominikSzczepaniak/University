using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace _8._1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string cykl;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e) //Akceptuj
        {
            if(cyklComboBox.SelectedItem == null)
            {
                MessageBox.Show("Wybierz cykl", "", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            if(nameTextBox.Text == null) { 
                MessageBox.Show("Wpisz nazwe uczelni", "", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            if(addressTextBox.Text == null)
            {
                MessageBox.Show("Wpisz adres uczelni", "", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            if(checkbox1.IsChecked == false && checkbox2.IsChecked == false)
            {
                MessageBox.Show("Wybierz rodzaj studiów", "", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            if(checkbox1.IsChecked == true && checkbox2.IsChecked == true)
            {
                MessageBox.Show("Wybierz tylko jeden rodzaj studiów", "", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
            cykl = cyklComboBox.Text;
            string name = nameTextBox.Text;
            string address = addressTextBox.Text;
            string rodzajStudiow = checkbox1.IsChecked == true ? "dzienne" : "uzupelniajace";
            MessageBox.Show(name + "\n" + address + "\n" + cykl + "\n" + rodzajStudiow, "Uczelnia", MessageBoxButton.OK, MessageBoxImage.Information);

        }

        private void Button_Click_1(object sender, RoutedEventArgs e) //Anuluj
        {
            this.Close();
        }

    }
}
