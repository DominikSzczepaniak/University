#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip_icmp.h> // Dodaj nagłówek z definicją struktury icmphdr
#include <netinet/ip.h>
#include <arpa/inet.h> // Dodaj nagłówek zawierający inet_pton i inet_ntop

#define PACKET_SIZE 64
#define TIMEOUT 1

// Funkcja do obliczania sumy kontrolnej
unsigned short checksum(void *b, int len) {
    unsigned short *buf = (unsigned short *)b;
    unsigned int sum = 0;
    unsigned short result;

    for (sum = 0; len > 1; len -= 2)
        sum += *buf++;

    if (len == 1)
        sum += *(unsigned char *)buf;

    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    result = ~sum;
    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <destination_ip>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock_fd < 0) {
        fprintf(stderr, "socket error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    struct sockaddr_in destination;
    memset(&destination, 0, sizeof(destination));
    destination.sin_family = AF_INET;
    if (inet_pton(AF_INET, argv[1], &destination.sin_addr) <= 0) {
        fprintf(stderr, "Invalid destination IP address\n");
        return EXIT_FAILURE;
    }

    char buffer[PACKET_SIZE];
    struct sockaddr_in sender;
    socklen_t sender_len = sizeof(sender);

    printf("Pinging %s...\n", argv[1]);

    // Sending ICMP Echo Request
    struct icmphdr *icmp_header = (struct icmphdr *)buffer;
    icmp_header->type = ICMP_ECHO;
    icmp_header->code = 0;
    icmp_header->checksum = 0;
    icmp_header->un.echo.id = getpid();
    icmp_header->un.echo.sequence = 0;
    memset(buffer + sizeof(struct icmphdr), 0, PACKET_SIZE - sizeof(struct icmphdr));
    icmp_header->checksum = 0;
    icmp_header->checksum = htons(~(0xFFFF & htons(checksum(icmp_header, PACKET_SIZE))));

    if (sendto(sock_fd, buffer, PACKET_SIZE, 0, (struct sockaddr *)&destination, sizeof(destination)) <= 0) {
        fprintf(stderr, "sendto error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    // Receiving ICMP Echo Reply
    ssize_t packet_len = recvfrom(sock_fd, buffer, PACKET_SIZE, 0, (struct sockaddr *)&sender, &sender_len);
    if (packet_len < 0) {
        fprintf(stderr, "recvfrom error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    char sender_ip_str[INET_ADDRSTRLEN];
    if (inet_ntop(AF_INET, &sender.sin_addr, sender_ip_str, sizeof(sender_ip_str)) == NULL) {
        fprintf(stderr, "inet_ntop error\n");
        return EXIT_FAILURE;
    }

    printf("Received ICMP reply from: %s\n", sender_ip_str);

    close(sock_fd);

    return EXIT_SUCCESS;
}
