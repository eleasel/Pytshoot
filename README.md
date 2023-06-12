# Network Troubleshooting Tool

A simple command-line tool for network troubleshooting. This tool allows you to perform various network tests and lookups to diagnose and troubleshoot network connectivity issues.

## Features

- **Ping Test**: Perform a ping test to check the availability and round-trip time of a network host.
- **Traceroute**: Trace the route that packets take to reach a destination, helping identify network bottlenecks or connectivity issues.
- **DNS Lookup**: Perform a DNS lookup to retrieve information about a domain name or IP address.
- **Reverse DNS Lookup**: Perform a reverse DNS lookup to find the domain name associated with an IP address.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eleasel/Pytshoot.git

2. Navigate to the project directory:

3. Install the required dependencies:
    pip install -r requirements.txt
    
## Usage

  python main.py <host> [--ping] [--traceroute] [--dnslookup] [--reversedns]
  
Replace <host> with the target host or IP address you want to troubleshoot.

Specify at least one option to perform network troubleshooting:

--ping: Perform a ping test.
--traceroute: Perform a traceroute.
--dnslookup: Perform a DNS lookup.
--reversedns: Perform a reverse DNS lookup.
  
![Screenshot 2023-06-12 at 5 41 29 PM](https://github.com/eleasel/Pytshoot/assets/101367394/bf5fff66-9212-40bf-8cd9-71af5d025944)



## Contributing
Contributions are welcome! If you encounter any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments

This project was made possible thanks to the following resources:

- [Pingman Tools](https://www.pingman.com/resources/articles/what-is-ping/): An informative article by Pingman Tools that explains the concept of ping and its use in network troubleshooting.
- [Geekflare](https://geekflare.com/traceroute-command-explained/): A detailed guide on the traceroute command and how it can be used to identify network issues by Geekflare.
- [Google Cloud DNS Documentation](https://cloud.google.com/dns/docs/quickstart): The official documentation provided by Google Cloud DNS, which was a valuable resource for understanding DNS lookups and their implementation.
- [RIPE Atlas](https://labs.ripe.net/Members/marco_hogewoning/a-look-into-dnssec-and-dns-trace-route): An interesting research article by RIPE Atlas that explores DNSSEC and its impact on traceroute results.

These resources provided valuable insights and knowledge in the field of network troubleshooting, helping to shape the development of this tool.


    
