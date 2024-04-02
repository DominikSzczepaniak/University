using System;
using System.IO;
using System.Text;

public class CaesarStream : Stream
{
    private readonly Stream _baseStream;
    private readonly int _shift;

    public CaesarStream(Stream baseStream, int shift)
    {
        _baseStream = baseStream;
        _shift = shift;
    }

    public override bool CanRead => _baseStream.CanRead;

    public override bool CanSeek => _baseStream.CanSeek;

    public override bool CanWrite => _baseStream.CanWrite;

    public override long Length => _baseStream.Length;

    public override long Position
    {
        get => _baseStream.Position;
        set => _baseStream.Position = value;
    }

    public override void Flush()
    {
        _baseStream.Flush();
    }

    public override int Read(byte[] buffer, int offset, int count)
    {
        var bytesRead = _baseStream.Read(buffer, offset, count);
        for (int i = 0; i < bytesRead; i++)
        {
            buffer[offset + i] = (byte)((buffer[offset + i] - _shift) % 256);
        }

        return bytesRead;
    }

    public string ReadStream()
    {
        byte[] buffer = new byte[_baseStream.Length];
        int bytesRead = _baseStream.Read(buffer, 0, buffer.Length);
        for (int i = 0; i < bytesRead; i++)
        {
            buffer[i] = (byte)((buffer[i] - _shift) % 256);
        }
        return Encoding.UTF8.GetString(buffer, 0, bytesRead);
    }

    public override void Write(byte[] buffer, int offset, int count)
    {
        var tempBuffer = new byte[count];
        Array.Copy(buffer, offset, tempBuffer, 0, count);

        for (int i = 0; i < tempBuffer.Length; i++)
        {
            tempBuffer[i] = (byte)((tempBuffer[i] + _shift) % 256);
        }

        _baseStream.Write(tempBuffer, 0, tempBuffer.Length);
    }

    public void Write(string message)
    {
        var messageBytes = Encoding.UTF8.GetBytes(message);
        for (int i = 0; i < messageBytes.Length; i++)
        {
            messageBytes[i] = (byte)((messageBytes[i] + _shift) % 256);
        }
        _baseStream.Write(messageBytes, 0, messageBytes.Length);
    }

    public override long Seek(long offset, SeekOrigin origin)
    {
        return _baseStream.Seek(offset, origin);
    }

    public override void SetLength(long value)
    {
        _baseStream.SetLength(value);
    }
}

class Program
{
    public static void Main()
    {
        string filePath = "test.txt";
        string message = "wiadomosc";
        
        using (FileStream fileStream = File.Create(filePath))
        {
            CaesarStream caesarStream = new CaesarStream(fileStream, 5);
            caesarStream.Write(message);
            caesarStream.ReadStream();
        }
        
        using (FileStream fileStream = File.Open(filePath, FileMode.Open))
        {
            CaesarStream caesarStream = new CaesarStream(fileStream, -5);
            string decodedMessage = caesarStream.ReadStream();
            Console.WriteLine(decodedMessage); 
        }
        
    }
}