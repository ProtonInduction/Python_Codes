import os
from tqdm import tqdm

class OneWordPerLine:
    
    def __init__(self):
        # Get the input and output file names from the user
        in_file = input("Enter input file name (with extension): ")
        out_file = input("Enter output file name (without extension): ")
        
        try:
            # Attempt to read the file with utf-8 encoding
            with open(in_file, 'r', encoding='utf-8') as file:
                # Initialize the reading progress bar
                lines = []
                for line in tqdm(file, desc="Reading lines", unit="lines"):
                    lines.append(line)
            
            # Write each word to a new line in the output file
            with open(f'{out_file}.txt', 'w', encoding='utf-8') as file:
                for line in tqdm(lines, desc="Writing words", unit="lines"):
                    words = line.split()  # Split each line into words
                    for word in words:
                        file.write(word + '\n')  # Write each word on a new line
                        
            print(f"Words have been written to {out_file}.txt, one per line.")
        
        except FileNotFoundError:
            print(f"The file {in_file} does not exist. Please check the file name and try again.")
        except UnicodeDecodeError:
            print(f"Could not decode {in_file} using UTF-8. Trying with ISO-8859-1 encoding...")
            # Try reading the file with ISO-8859-1 encoding as a fallback
            try:
                with open(in_file, 'r', encoding='iso-8859-1') as file:
                    lines = []
                    for line in tqdm(file, desc="Reading lines", unit="lines"):
                        lines.append(line)

                with open(f'{out_file}.txt', 'w', encoding='utf-8') as file:
                    for line in tqdm(lines, desc="Writing words", unit="lines"):
                        words = line.split()
                        for word in words:
                            file.write(word + '\n')

                print(f"Words have been written to {out_file}.txt, one per line.")
            except UnicodeDecodeError as e:
                print(f"Failed to decode the file using ISO-8859-1 as well. Error: {e}")

# Instantiate the class and run the script
if __name__ == "__main__":
    OneWordPerLine()
