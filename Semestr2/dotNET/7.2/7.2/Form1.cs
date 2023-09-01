// Zaimplementowaæ w³asny komponent SmoothProgressBar, który bêdzie imitowaæ
//zachowanie standardowego komponentu ProgressBar (pasek postêpu).
//Komponent powinien mieæ co najmniej 3 w³aœciwoœci: Min, Max i Value, pozwalaj¹ce okreœliæ odpowiednio minimaln¹,
//maksymaln¹ i bie¿¹c¹ wartoœæ paska postêpu. Maj¹c te informacje, SmoothProgressBar w zdarzeniu Paint powinien rysowaæ
//g³adki (w przeciwieñstwie do oryginalnego, który jest z³o¿ony z ”kafelków”) pasek postêpu o odpowiedniej
//d³ugoœci (wed³ug zadanych proporcji).

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