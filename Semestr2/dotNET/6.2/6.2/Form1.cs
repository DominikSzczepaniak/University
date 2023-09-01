using System.Configuration;

namespace _6._2
{
    public partial class Form1 : Form
    {
        private OpenFileDialog ofd;
        private SaveFileDialog saveFileDialog;
        private FolderBrowserDialog folderBrowserDialog;
        private string wartosc1 = ConfigurationManager.AppSettings.Get("parametr1");
        private int wartosc2 = int.Parse(ConfigurationManager.AppSettings.Get("parametr2"));
        private bool wartosc3 = bool.Parse(ConfigurationManager.AppSettings.Get("parametr3"));

        public Form1()
        {
            InitializeComponent();
            ofd = new OpenFileDialog();
            String text = "Wartosci z wejscia programu: " + wartosc1 + " " + wartosc2 + " " + wartosc3;
            MessageBox.Show(text);
        }
        private void button1_Click(object sender, EventArgs e)
        {
            var v = ofd.ShowDialog();
            if (v == DialogResult.OK)
            {
                var fileStream = ofd.OpenFile();
                using (StreamReader sr = new StreamReader(fileStream))
                {
                    var fileContent = sr.ReadToEnd();
                    MessageBox.Show(fileContent);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            saveFileDialog = new SaveFileDialog();
            saveFileDialog.ShowDialog();
            var text = saveFileDialog.FileName;
            MessageBox.Show(text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            folderBrowserDialog = new FolderBrowserDialog();
            folderBrowserDialog.ShowDialog();
            var path = folderBrowserDialog.SelectedPath;
            MessageBox.Show(path);


        }
    }
}