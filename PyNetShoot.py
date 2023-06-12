import subprocess
import socket
import argparse


def ping(host):
    command = ['ping', '-c', '4', host]
    try:
        output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)


def traceroute(host):
    command = ['traceroute', host]
    try:
        output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)


def dns_lookup(host):
    try:
        ip_address = socket.gethostbyname(host)
        return f'IP address: {ip_address}'
    except socket.gaierror as e:
        return str(e)


def reverse_dns_lookup(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return f'Domain name: {domain_name}'
    except socket.herror as e:
        return str(e)


def main():
    parser = argparse.ArgumentParser(description='Network Troubleshooting Tool')
    parser.add_argument('host', help='Host or IP address to troubleshoot')
    parser.add_argument('--ping', action='store_true', help='Perform ping test')
    parser.add_argument('--traceroute', action='store_true', help='Perform traceroute')
    parser.add_argument('--dnslookup', action='store_true', help='Perform DNS lookup')
    parser.add_argument('--reversedns', action='store_true', help='Perform reverse DNS lookup')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error('Please specify at least one option to perform network troubleshooting.')

    print(f'Troubleshooting for: {args.host}\n')

    if args.ping:
        print('Ping Test:')
        result = ping(args.host)
        print(result)

    if args.traceroute:
        print('\nTraceroute:')
        result = traceroute(args.host)
        print(result)

    if args.dnslookup:
        print('\nDNS Lookup:')
        result = dns_lookup(args.host)
        print(result)

    if args.reversedns:
        print('\nReverse DNS Lookup:')
        try:
            result = reverse_dns_lookup(args.host)
            print(result)
        except (socket.herror, socket.timeout) as e:
            print(f'Error: {str(e)}')


if __name__ == '__main__':
    main()
