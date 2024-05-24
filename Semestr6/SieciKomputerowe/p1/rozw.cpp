#include <arpa/inet.h>
#include <assert.h>
#include <errno.h>
#include <netinet/ip.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <stdbool.h>
#include <netdb.h>
#include <string.h>
#include <netinet/ip_icmp.h>
#include <iostream>
#include <chrono>
#include <thread>
#include <string>
#define ICMP_ECHO 8

u_int16_t compute_icmp_checksum(const void *buff, int length)
{
    const u_int16_t *ptr = (const uint16_t *)buff;
    u_int32_t sum = 0;
    assert(length % 2 == 0);
    for (; length > 0; length -= 2)
    {
        sum += *ptr++;
    }
    sum = (sum >> 16U) + (sum & 0xffffU);
    return (u_int16_t)(~(sum + (sum >> 16U)));
}

void print_as_bytes(unsigned char *buff, ssize_t length)
{
    for (ssize_t i = 0; i < length; i++, buff++)
    {
        printf("%.2x ", *buff);
    }
}

int incoming_packet(){
    int sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if(sock_fd < 0){
        fprintf(stderr, "socket error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }
    struct sockaddr_in sender;
    socklen_t sender_len = sizeof(sender);
    u_int8_t buffer[IP_MAXPACKET];

    ssize_t packet_len = recvfrom(sock_fd, buffer, IP_MAXPACKET, 0, (struct sockaddr *)&sender, &sender_len);
    if (packet_len < 0)
    {
        fprintf(stderr, "recvfrom error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    char sender_ip_str[20];
    inet_ntop(AF_INET, &(sender.sin_addr), sender_ip_str, sizeof(sender_ip_str));

    struct ip *ip_header = (struct ip *)buffer;
    ssize_t ip_header_len = 4 * (ssize_t)(ip_header->ip_hl);
    // if buffer[ip_header] starts with 0b then print ip:
    if(buffer[ip_header_len] == 0x0b){
        printf("ICMP packet from %s\n", sender_ip_str);
    }
    else{
        printf("Not an ICMP packet, %s\n", sender_ip_str);
        return 200;
    }
    // printf("IP header: ");
    // print_as_bytes(buffer, ip_header_len);

    return 0;
}


int incoming_packets_infinite(){
    int sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock_fd < 0)
    {
        fprintf(stderr, "socket error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }
    for (;;)
    {
        //kontynuuje petle dopiero gdy dostanie jakis pakiet
        struct sockaddr_in sender;
        socklen_t sender_len = sizeof(sender);
        u_int8_t buffer[IP_MAXPACKET];

        ssize_t packet_len = recvfrom(sock_fd, buffer, IP_MAXPACKET, 0, (struct sockaddr *)&sender, &sender_len);
        if (packet_len < 0)
        {
            fprintf(stderr, "recvfrom error: %s\n", strerror(errno));
            return EXIT_FAILURE;
        }

        char sender_ip_str[20];
        inet_ntop(AF_INET, &(sender.sin_addr), sender_ip_str, sizeof(sender_ip_str));
        printf("Received IP packet with ICMP content from: %s\n", sender_ip_str);

        struct ip *ip_header = (struct ip *)buffer;
        ssize_t ip_header_len = 4 * (ssize_t)(ip_header->ip_hl);

        printf("IP header: ");
        print_as_bytes(buffer, ip_header_len);
        printf("\n");

        printf("IP data:   ");
        
        std::cout << (buffer[ip_header_len] == 0x0b) << '\n';
        if(buffer[ip_header_len] == 0x0b){
            printf("ICMP packet %s\n", sender_ip_str);
        }
        else{
            printf("Not an ICMP packet\n");
        }
        print_as_bytes(buffer + ip_header_len, packet_len - ip_header_len);
        printf("\n\n");
    }
}

void send_packets(int sockfd, int TTL, char* dest, short id, short seq){
    struct icmp header;
    header.icmp_type = ICMP_ECHO;
    header.icmp_code = 0;
    header.icmp_hun.ih_idseq.icd_id = id;
    header.icmp_hun.ih_idseq.icd_seq = seq;
    header.icmp_cksum = 0;
    header.icmp_cksum = compute_icmp_checksum (
    (u_int16_t*)&header, sizeof(header));

    struct sockaddr_in recipient;
    bzero(&recipient, sizeof(recipient));
    recipient.sin_family = AF_INET;
    inet_pton(AF_INET, dest, &recipient.sin_addr);
    
    setsockopt(sockfd, IPPROTO_IP, IP_TTL, &TTL, sizeof(int));

    ssize_t bytes_sent = sendto(sockfd, &header, sizeof(header), 0, (struct sockaddr*)&recipient, sizeof(recipient));
    if (bytes_sent < 0)
    {
        fprintf(stderr, "sendto error: %s\n", strerror(errno));
        return;
    }
    // printf("Sent %ld bytes to %s\n", bytes_sent, dest);
}

int main(int argc, char* argv[])
{
    std::cout << argv[1] << '\n';
    int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sockfd < 0)
    {
        fprintf(stderr, "socket error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }
    for(int i = 1; i<=64; i++){
        send_packets(sockfd, i, argv[1], 123, 321);
        int ans1 = incoming_packet();
        send_packets(sockfd, i, argv[1], 123, 321);
        int ans2 = incoming_packet();
        send_packets(sockfd, i, argv[1], 123, 321);
        int ans3 = incoming_packet();
        if(ans1 == 200 && ans2 == 200 && ans3 == 200){
            break;
        }
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    //odpalic w osobnym watku incoming_packets?
    
}
