namespace lista6zadanie1
{
    public partial class Form1 : Form
    {
        private bool chbx1_checked = false;
        private bool chbx2_checked = false;
        public string nazwa { get; set; }
        public string adres { get; set; }
        public string cykl { get; set; }
        public string rodzaj { get; set; }
        private bool changing = false;
        public Form1()
        {
            InitializeComponent();
        }

        private void btnAccept_Click(object sender, EventArgs e)
        {
            // raise error if anything empty

            var form2 = new Form2(nazwa, adres, cykl, rodzaj);
            form2.ShowDialog();

        }
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            nazwa = textBox1.Text;
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            adres = textBox2.Text;
        }

        private void checkBox1_Click(object sender, EventArgs e)
        {

        }

        private void checkBox2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            cykl = (string)comboBox1.SelectedItem;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked && !changing)
            {
                changing = true;
                checkBox2.Checked = false;
                checkBox1.Checked = true;
                changing = false;
            }
            rodzaj = "dzienne";

        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

            if (checkBox1.Checked && !changing)
            {
                changing = true;
                checkBox1.Checked = false;
                checkBox2.Checked = true;
                changing = false;
            }
            rodzaj = "uzupelniajace";
        }
    }
}