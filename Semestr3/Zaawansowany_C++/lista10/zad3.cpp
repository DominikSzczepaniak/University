#include <iconv.h>
#include <fstream>
#include <sstream>
#include <vector>

std::string convertEncoding(const std::string& str, const char* toEncoding, const char* fromEncoding) {
    iconv_t cd = iconv_open(toEncoding, fromEncoding);
    if (cd == (iconv_t)-1) {
        perror("iconv_open");
        return "";
    }

    std::vector<char> inbuf(str.begin(), str.end());
    size_t inbytesleft = inbuf.size();
    size_t outbytesleft = inbytesleft * 4;
    std::vector<char> outbuf(outbytesleft);

    char* inptr = inbuf.data();
    char* outptr = outbuf.data();

    if (iconv(cd, &inptr, &inbytesleft, &outptr, &outbytesleft) == (size_t)-1) {
        perror("iconv");
        iconv_close(cd);
        return "";
    }

    iconv_close(cd);
    return std::string(outbuf.data(), outbuf.size() - outbytesleft);
}

int main() {
    std::ifstream utf8File("input.txt");
    std::stringstream ss;
    ss << utf8File.rdbuf();
    std::string utf8Content = ss.str();

    std::string utf32Content = convertEncoding(utf8Content, "UTF-32LE", "UTF-8");
    std::ofstream utf32File("output_utf32.txt", std::ios::binary);
    utf32File.write(utf32Content.data(), utf32Content.size());

    std::string iso88592Content = convertEncoding(utf8Content, "ISO-8859-2", "UTF-8");
    std::ofstream iso88592File("output_iso88592.txt");
    iso88592File.write(iso88592Content.data(), iso88592Content.size());

    return 0;
}