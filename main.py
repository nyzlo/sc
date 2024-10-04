from modules.misc import show_menu, user_handling, save_to_file
from modules.scans import top_tcp_scan

def main():
	while True:
		show_menu()

		user_choice = input("Choose an option between (1-2): ")

		if user_choice == "1":
			save_choice, scan_result = user_handling(top_tcp_scan)
			if save_choice == "y":
				save_to_file(scan_result)
				break
			else:
				break
		elif user_choice == "2":
			print("\nGoodbye!")
			break
		else:
			print("\nWrong input, try again!\n")


if __name__ == "__main__":
	main()