using System.Drawing;
using static System.Windows.Forms.DataFormats;

//Przygotowaæ aplikacjê, która wykorzystuje omówiony na wyk³adzie podsystem GDI+
//do rysowania w oknie zegara analogowego prezentuj¹cego bie¿¹cy czas, zgodny z zegarem
//systemowym.
//Rysowany widok powinien poprawnie dostosowywaæ siê do wielkoœci okna podczas zmiany
//jego rozmiarów przez u¿ytkownika.


namespace _7._1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            this.SetStyle(ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint | ControlStyles.OptimizedDoubleBuffer, true);
        }



        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            var czas_obecny = DateTime.Now;
            var hour = czas_obecny.Hour;
            var minute = czas_obecny.Minute;
            var second = czas_obecny.Second;
            int centerX = this.ClientSize.Width / 2;
            int centerY = this.ClientSize.Height / 2;
            var diameter_of_clock = Math.Min(this.ClientSize.Width, this.ClientSize.Height) / 3*2;
            var radius = diameter_of_clock / 2;
            var clock_outline_thickness = 5;
            var full_hour_lines_thickness = 4;
            var other_lines_thickness = 2;
            var minute_and_hour_arrow_thickness = 5;
            var second_arrow_thickness = 2;
            var pen = new Pen(Color.Black, clock_outline_thickness);
            e.Graphics.DrawEllipse(pen, centerX-radius, centerY-radius, diameter_of_clock, diameter_of_clock);
            for(int i = 0; i<60; i++) //tics drawing
            {
                var hourPen = new Pen(Color.Black, full_hour_lines_thickness);
                var minsecPen = new Pen(Color.Black, other_lines_thickness);
                if(i % 5 != 0) 
                {
                    double angle = i * Math.PI / 30;
                    int x1 = (int)(centerX + (radius - 10) * Math.Sin(angle));
                    int y1 = (int)(centerY - (radius - 10) * Math.Cos(angle));
                    int x2 = (int)(centerX + (radius - 20) * Math.Sin(angle));
                    int y2 = (int)(centerY - (radius - 20) * Math.Cos(angle));
                    e.Graphics.DrawLine(minsecPen, x1, y1, x2, y2);
                }
                else
                {
                    double angle = i * Math.PI / 30;
                    int x1 = (int)(centerX + (radius - 10) * Math.Sin(angle));
                    int y1 = (int)(centerY - (radius - 10) * Math.Cos(angle));
                    int x2 = (int)(centerX + (radius - 20) * Math.Sin(angle));
                    int y2 = (int)(centerY - (radius - 20) * Math.Cos(angle));
                    e.Graphics.DrawLine(hourPen, x1, y1, x2, y2);
                } 
            }
            StringFormat format = new StringFormat();
            format.Alignment = StringAlignment.Center;
            format.LineAlignment = StringAlignment.Center;
            var brush = new SolidBrush(Color.Black);
            for (int i = 1; i <= 12; i++)
            {
                double angle = i * Math.PI / 6;
                int x = (int)(centerX + (radius - diameter_of_clock/8) * Math.Sin(angle));
                int y = (int)(centerY - (radius - diameter_of_clock/8) * Math.Cos(angle));
                e.Graphics.DrawString(i.ToString(), new Font("Times New Roman", diameter_of_clock/15), brush, x, y, format);
            }
            double hourAngle = (hour % 12 + minute / 60.0 + second / 3600.0) * Math.PI / 6.0;
            double minuteAngle = (minute + second / 60.0) * Math.PI / 30.0;
            double secondAngle = second * Math.PI / 30.0;
            var minuteHour_arrow_pen = new Pen(Color.Black, minute_and_hour_arrow_thickness);
            var second_arrow_pen = new Pen(Color.Black, second_arrow_thickness);
            e.Graphics.DrawLine(minuteHour_arrow_pen, centerX, centerY, (int)(centerX + radius * 0.5 * Math.Sin(hourAngle)), (int)(centerY - radius * 0.5 * Math.Cos(hourAngle)));
            e.Graphics.DrawLine(minuteHour_arrow_pen, centerX, centerY, (int)(centerX + radius * 0.7 * Math.Sin(minuteAngle)), (int)(centerY - radius * 0.7 * Math.Cos(minuteAngle)));
            e.Graphics.DrawLine(second_arrow_pen, centerX, centerY, (int)(centerX + radius * 0.9 * Math.Sin(secondAngle)), (int)(centerY - radius * 0.9 * Math.Cos(secondAngle)));

        }
    }
}