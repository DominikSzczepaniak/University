using System;
using System.Collections.Generic;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsControlLibrary1
{
    public class SmoothProgressBar : Control
    {
        public SmoothProgressBar() 
        { 
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer, true);
        }  
        private int _min;
        private int _max;
        private int _value;

        public int Min
        {
            get { return _min; }
            set { _min = value; Invalidate(); }
        }

        public int Max
        {
            get { return _max; }
            set { _max = value; Invalidate(); }
        }

        public int Value
        {
            get { return _value; }
            set
            {
                if (value < _min)
                {
                    _value = _min;
                }
                else if (value > _max)
                {
                    _value = _max;
                }
                else
                {
                    _value = value;
                }
                Invalidate();
            }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            double ratio = (double)_value / (double)_max;
            // Obliczanie kolorów gradientu
            Color color1 = Color.FromArgb(255, 255, 255);
            Color color2 = Color.FromArgb(0, 0, 255);

            // Tworzenie gradientu
            LinearGradientBrush brush = new LinearGradientBrush(ClientRectangle, color1, color2, LinearGradientMode.Horizontal);

            // Rysowanie gradientu
            e.Graphics.FillRectangle(brush, ClientRectangle.X, ClientRectangle.Y, (int)(ClientRectangle.Width * ratio), ClientRectangle.Height);
            e.Graphics.DrawRectangle(new Pen(Color.Black, 4), ClientRectangle);
            //e.Graphics.FillRectangle(brush, ClientRectangle.X, ClientRectangle.Y, (int)(ClientRectangle.Width*ratio), ClientRectangle.Height);
            
            // Rysowanie tekstu wartości
            string text = string.Format("{0}%", (int)(ratio*100));
            SizeF textSize = e.Graphics.MeasureString(text, Font);
            Point textPos = new Point((int)((Width - textSize.Width) / 2), (int)((Height - textSize.Height) / 2));
            e.Graphics.DrawString(text, Font, new SolidBrush(ForeColor), textPos);
        }
    }
}
