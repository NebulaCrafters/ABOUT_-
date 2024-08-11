import subprocess
from colorama import Fore, Style, init
from tabulate import tabulate
import os
import winsound  # Import winsound for sound playback

# initialize colorama
init(autoreset=True)

# retrieve system information
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')

# define colors
header_color = Fore.CYAN
value_color = Fore.GREEN
default_color = Fore.BLACK

# prepare data for the main table
main_table_data = []
# prepare data for the summary table
summary_table_data = []

for item in Id:
    # strip any leading or trailing whitespace and ignore empty lines
    cleaned_item = item.strip()
    if cleaned_item:
        # check for headers and values
        if ':' in cleaned_item:
            header, value = cleaned_item.split(':', 1)
            # add to main table
            main_table_data.append([header_color + header + Style.RESET_ALL, value_color + value])
            
            # add to summary table based on specific headers
            if header == 'OS Name' or header == 'OS Version' or header == 'Processor(s)':
                summary_table_data.append([header_color + header + Style.RESET_ALL, value_color + value])

# format tables
main_table = tabulate(main_table_data, headers=['Header', 'Value'], tablefmt='grid', stralign='left')
summary_table = tabulate(summary_table_data, headers=['Header', 'Value'], tablefmt='grid', stralign='left')

# play scanning sound
frequency = 1000  # Set Frequency To 1000 Hertz
duration = 500  # Set Duration To 500 ms == 0.5 second
winsound.Beep(frequency, duration)

# print tables
print("Full System Information:\n")
print(main_table)

print("\nSummary Information:\n")
print(summary_table)

# prepare content to save
file_content = (
    "Full System Information:\n"
    + main_table
    + "\n\nSummary Information:\n"
    + summary_table
)

# save to file
file_path = 'SYSTEM_INFO.txt'
try:
    with open(file_path, 'w') as file:
        file.write(file_content)
    print(f"\nSystem information saved to {file_path}")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")

# Print the absolute path of the saved file
absolute_file_path = os.path.abspath(file_path)
print(f"\nSystem information file is located at: {absolute_file_path}")
