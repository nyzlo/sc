def show_menu():
	print("[---NMAP Clown Fiesta---]")
	print("-------------------------")
	print("1. Top 1000 tcp port discovery")
	print("2. Quit\n")

def print_scan(scanner):
	result = []

	for host in scanner.all_hosts():
		host_info = f"\nHost: {host}\nState: {scanner[host].state()}"
		print(host_info)
		result.append(host_info)

		for proto in scanner[host].all_protocols():
			proto_info = f"Protocol: {proto}"
			print(proto_info)
			result.append(proto_info)

			ports = scanner[host][proto].keys()
			for port in ports:
				port_info = f"Port: {port} State: {scanner[host][proto][port]['state']}"
				print(port_info)
				result.append(port_info)

	return "\n".join(result)

def save_to_file(scan_result):
	filename = input("Save file as: ")
	with open(filename, "w") as file:
		file.write(scan_result)
	print(f"\nFile successfully saved as: {filename}")

def user_handling(scan):
	direct_or_file = input("\nHosts directly(1) or file(2): ")

	if direct_or_file == "1":
		target = input("Input target host/s (e.g. IP or IP IP IP): ")
		print(f"\nScanning {target}")
	elif direct_or_file == "2":
		while True:
			target = input("\nInput txt file: ")
			try:
				with open(target, "r") as file:
					target = file.readline()
				print(f"\nScanning {target}")
				break
			except FileNotFoundError:
				print(f"Error: the file {target} was not found. Try again!")
	else:
		print("Wrong input, try again!")

	scan_result = scan(target)

	save_choice = input("\nSave the result to file? (Y/N): ").strip().lower()
	return save_choice, scan_result