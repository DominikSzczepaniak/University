// Zaimplementowa� w�asny komponent SmoothProgressBar, kt�ry b�dzie imitowa�
//zachowanie standardowego komponentu ProgressBar (pasek post�pu).
//Komponent powinien mie� co najmniej 3 w�a�ciwo�ci: Min, Max i Value, pozwalaj�ce okre�li� odpowiednio minimaln�,
//maksymaln� i bie��c� warto�� paska post�pu. Maj�c te informacje, SmoothProgressBar w zdarzeniu Paint powinien rysowa�
//g�adki (w przeciwie�stwie do oryginalnego, kt�ry jest z�o�ony z �kafelk�w�) pasek post�pu o odpowiedniej
//d�ugo�ci (wed�ug zadanych proporcji).

using WinFormsControlLibrary1;

namespace _7._2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            SmoothProgressBar progressBar = new SmoothProgressBar();
            progressBar.Location = new Point(50, 50);
            progressBar.Size = new Size(200, 20);
            progressBar.Min = 0;
            progressBar.Max = 100;
            progressBar.Value = 76;
            Controls.Add(progressBar);
        }
    }
}