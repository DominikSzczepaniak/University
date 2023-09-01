using System.Net;

namespace _7._4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private async Task<string> GetWebsiteContentAsync(string url)
        {
            using (HttpClient httpClient = new HttpClient())
            {
                return await httpClient.GetStringAsync(url);
            }
        }
        private string GetWebsiteContent(string url)
        {
            using (WebClient webClient = new WebClient())
            {
                return webClient.DownloadString(url);
            }
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            string result = await GetWebsiteContentAsync("https://www.microsoft.com");
            MessageBox.Show(result);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string websiteContent = GetWebsiteContent("https://microsoft.com");
            MessageBox.Show(websiteContent);
        }
    }
}