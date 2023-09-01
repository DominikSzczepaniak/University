using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.Mail;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

class Example
{
    public static async Task Main()
    {
        await FtpExample.DownloadFileAsync("ftp://example.com/file.txt", "local/path/file.txt");

        await HttpExample.DownloadFileAsync("http://example.com/file.txt", "local/path/file.txt");

        await WebClientExample.DownloadFileAsync("http://example.com/file.txt", "local/path/file.txt");

        await HttpClientExample.DownloadFileAsync("http://example.com/file.txt", "local/path/file.txt");

        await HttpListenerExample.StartListeningAsync("http://localhost:8080/");

        await TcpListenerExample.StartListeningAsync("127.0.0.1", 1234);

        await TcpClientExample.SendDataAsync("127.0.0.1", 1234, "Hello, server!");

        await SmtpClientExample.SendEmailAsync("from@example.com", "to@example.com", "Hello", "This is a test email.");
    }
}

class FtpExample
{
    public static async Task DownloadFileAsync(string ftpUrl, string localPath)
    {
        FtpWebRequest request = (FtpWebRequest)WebRequest.Create(ftpUrl);
        request.Method = WebRequestMethods.Ftp.DownloadFile;

        using (FtpWebResponse response = (FtpWebResponse)await request.GetResponseAsync())
        using (Stream responseStream = response.GetResponseStream())
        using (FileStream fileStream = new FileStream(localPath, FileMode.Create))
        {
            await responseStream.CopyToAsync(fileStream);
        }
    }
}

class HttpExample
{
    public static async Task DownloadFileAsync(string url, string localPath)
    {
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
        request.Method = "GET";

        using (HttpWebResponse response = (HttpWebResponse)await request.GetResponseAsync())
        using (Stream responseStream = response.GetResponseStream())
        using (FileStream fileStream = new FileStream(localPath, FileMode.Create))
        {
            await responseStream.CopyToAsync(fileStream);
        }
    }
}

class WebClientExample
{
    public static async Task DownloadFileAsync(string url, string localPath)
    {
        using (WebClient client = new WebClient())
        {
            await client.DownloadFileTaskAsync(url, localPath);
        }
    }
}

class HttpClientExample
{
    public static async Task DownloadFileAsync(string url, string localPath)
    {
        using (HttpClient client = new HttpClient())
        {
            using (HttpResponseMessage response = await client.GetAsync(url))
            using (Stream responseStream = await response.Content.ReadAsStreamAsync())
            using (FileStream fileStream = new FileStream(localPath, FileMode.Create))
            {
                await responseStream.CopyToAsync(fileStream);
            }
        }
    }
}

class HttpListenerExample
{
    public static async Task StartListeningAsync(string url)
    {
        HttpListener listener = new HttpListener();
        listener.Prefixes.Add(url);
        listener.Start();

        while (true)
        {
            HttpListenerContext context = await listener.GetContextAsync();
            HttpListenerRequest request = context.Request;
            HttpListenerResponse response = context.Response;

            string responseString = "Hello, World!";
            byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseString);

            response.ContentLength64 = buffer.Length;
            Stream output = response.OutputStream;

            await output.WriteAsync(buffer, 0, buffer.Length);
            output.Close();
        }
    }
}

class TcpListenerExample
{
    public static async Task StartListeningAsync(string ipAddress, int port)
    {
        IPAddress localAddress = IPAddress.Parse(ipAddress);
        TcpListener listener = new TcpListener(localAddress, port);
        listener.Start();

        while (true)
        {
            TcpClient client = await listener.AcceptTcpClientAsync();

            byte[] buffer = new byte[1024];
            using (NetworkStream stream = client.GetStream())
            {
                int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                string requestData = Encoding.ASCII.GetString(buffer, 0, bytesRead);

                // Process the received data or perform other operations
                // ...

                byte[] responseData = Encoding.ASCII.GetBytes("Response from server");
                await stream.WriteAsync(responseData, 0, responseData.Length);
            }

            client.Close();
        }
    }
}

class TcpClientExample
{
    public static async Task SendDataAsync(string serverIp, int serverPort, string data)
    {
        using (TcpClient client = new TcpClient())
        {
            await client.ConnectAsync(serverIp, serverPort);

            byte[] buffer = Encoding.ASCII.GetBytes(data);
            using (NetworkStream stream = client.GetStream())
            {
                await stream.WriteAsync(buffer, 0, buffer.Length);

                buffer = new byte[1024];
                int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                string responseData = Encoding.ASCII.GetString(buffer, 0, bytesRead);

                Console.WriteLine("Response from server: " + responseData);
            }
        }
    }
}

class SmtpClientExample
{
    public static async Task SendEmailAsync(string from, string to, string subject, string body)
    {
        using (SmtpClient client = new SmtpClient("smtp.example.com", 587))
        {
            client.UseDefaultCredentials = false;
            client.Credentials = new NetworkCredential("username", "password");
            client.EnableSsl = true;

            MailMessage message = new MailMessage(from, to, subject, body);
            await client.SendMailAsync(message);
        }
    }
}
