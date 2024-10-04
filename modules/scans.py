import nmap
from modules.misc import print_scan

scanner = nmap.PortScanner()

def top_tcp_scan(target):
	args = "-Pn -T4"
	scanner.scan(hosts=target, arguments=args)

	return print_scan(scanner)