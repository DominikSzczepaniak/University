using System;
using System.IO;
using System.Net;
using System.Net.Mail;

public class SmtpFacade
{
    private readonly string _smtpServer;
    private readonly int _smtpPort;
    private readonly string _smtpUser;
    private readonly string _smtpPassword;

    public SmtpFacade(string smtpServer, int smtpPort, string smtpUser, string smtpPassword)
    {
        _smtpServer = smtpServer;
        _smtpPort = smtpPort;
        _smtpUser = smtpUser;
        _smtpPassword = smtpPassword;
    }

    public void Send(string From, string To, string Subject, string Body, Stream Attachment, string AttachmentMimeType)
    {
        using (SmtpClient client = new SmtpClient(_smtpServer, _smtpPort))
        {
            client.EnableSsl = true;
            client.UseDefaultCredentials = false;
            client.Credentials = new NetworkCredential(_smtpUser, _smtpPassword);

            using (MailMessage mailMessage = new MailMessage(From, To))
            {
                mailMessage.Subject = Subject;
                mailMessage.Body = Body;

                if (Attachment != null && !string.IsNullOrEmpty(AttachmentMimeType))
                {
                    Attachment mailAttachment = new Attachment(Attachment, AttachmentMimeType);
                    mailMessage.Attachments.Add(mailAttachment);
                }

                try
                {
                    client.Send(mailMessage);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Błąd podczas wysyłania e-maila: " + ex.Message);
                }
            }
        }
    }
}
