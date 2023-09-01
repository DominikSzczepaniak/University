using WinFormsControlLibrary1;
namespace _7._3
{
    public partial class Form1 : Form
    {
        SmoothProgressBar s1 = new SmoothProgressBar();
        public Form1()
        {
            InitializeComponent();
            s1.Location = new Point(10, 10);
            s1.Size = new Size(200, 20);
            s1.Value = 0;
            s1.Max = 100;
            s1.Min = 0;
            Controls.Add(s1);
        }
        private bool IsPrime(long n)
        {
            if (n < 2)
                return false;
            else if (n == 2)
                return true;
            else if (n % 2 == 0)
                return false;
            else
            {
                for (long i = 3; i * i <= n; i += 2)
                    if (n % i == 0)
                        return false;
                return true;
            }
        }
        private void backgroundWorker1_DoWork(object sender, System.ComponentModel.DoWorkEventArgs e)
        {
            long start = 1;
            long end = 10000000;
            s1.Max = (int)end;
            s1.Min = (int)start;
            int PrimeCount = 0;
            for (long i = start; i <= end; i++)
            {
                if (IsPrime(i))
                {
                    PrimeCount++;
                }
                if (i % 1000 == 0)
                {
                    backgroundWorker1.ReportProgress((int)i);
                }
            }
            e.Result = PrimeCount;
        }

        private void backgroundWorker1_ProgressChanged(object sender, System.ComponentModel.ProgressChangedEventArgs e)
        {
            s1.Value = e.ProgressPercentage;
        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, System.ComponentModel.RunWorkerCompletedEventArgs e)
        {
            if (e.Error != null)
            {
                MessageBox.Show("Error: " + e.Error.Message);
            }
            else if (e.Cancelled)
            {
                MessageBox.Show("Operation cancelled.");
            }
            else
            {
                int primeCount = (int)e.Result;
                if(MessageBox.Show("Found " + primeCount + " prime numbers.", "", MessageBoxButtons.OK) == DialogResult.OK)
                {
                    Application.Exit();
                }
                
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            backgroundWorker1.WorkerReportsProgress = true;
            if (!backgroundWorker1.IsBusy)
                backgroundWorker1.RunWorkerAsync();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ThreadStart threadred = new ThreadStart(CalculatePrimes);
            Thread thread = new Thread(threadred);
            thread.Start();
        }

        private void CalculatePrimes()
        {
            long startNum = 1;
            long endNum = 10000000;
            s1.Max = (int)endNum;
            s1.Value = 0;
            s1.Min = 0;
            int primeCount = 0;
            for (long i = startNum; i <= endNum; i++)
            {
                if(i%1000 == 0)
                {
                    s1.Value = (int)i;
                }
                //s1.Value = (int)i;
                if (IsPrime(i))
                {
                    primeCount++;
                }
            }
            if (MessageBox.Show("Found " + primeCount + " prime numbers.", "", MessageBoxButtons.OK) == DialogResult.OK)
            {
                Application.Exit();
            }
        }

    }
}