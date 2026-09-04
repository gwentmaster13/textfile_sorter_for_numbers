
def main():
    while True:
        user_file = input("Enter the name of the file: ")
        try:
            with open(user_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                break
        except FileNotFoundError:
            with open("logg.txt", "a", encoding="utf-8") as logg:
                logg.write(f"Could not find {user_file} file.")
            print(f"Could not find {user_file} file.")
        except IOError:
            with open("logg.txt", "a", encoding="utf-8") as logg:
                logg.write(f"Error while getting Input/Output from the {user_file} file.")
            print("Something went wrong while working with file.")

    lines_checked = 0
    ignored_lines = 0
    failed_lines = 0
    validated_lines = 0
    validated_numbers = []

    for number_line, line in enumerate(lines):
        lines_checked += 1
        stripped_line = line.strip().split(" ")
        print(f"({number_line + 1}) {stripped_line}")

        try:
            valid_line = float(stripped_line[0].replace(",", "."))
            with open("rapport.txt", "a", encoding="utf-8") as rapport:
                rapport.write(str(valid_line) + "\n")
            validated_lines += 1
            validated_numbers.append(valid_line)

        except ValueError:
            if stripped_line[0] == "#" or stripped_line[0] == "":
                with open("logg.txt", "a", encoding="utf-8") as logg:
                    logg.write(f'({number_line + 1}) line ignored: "{line.strip()}" \nReason: Commented or empty line\n')
                    ignored_lines += 1
            else:
                with open("logg.txt", "a", encoding="utf-8") as logg:
                    logg.write(f'({number_line + 1}) line failed to validate: : "{line.strip()}" \nReason: Line consists only of string(s)\n')                
                    failed_lines += 1

    with open("rapport.txt", "a", encoding="utf-8") as rapport:
        rapport.write(f"Valid lines: {validated_lines}\n")

        if len(validated_numbers) > 0:
            rapport.write(f"Average value: {sum(validated_numbers) / validated_lines}\n")
            rapport.write(f"Sum of data: {sum(validated_numbers):.2f}\n")
            rapport.write(f"Max. value: {max(validated_numbers):.2f}\n")
            rapport.write(f"Min. value: {min(validated_numbers):.2f}\n")
        else:
            rapport.write("No valid data was given to calculate.")

    with open("logg.txt", "a", encoding="utf-8") as logg:
        if len(validated_numbers) > 0:
            logg.write("=========RESULTS==========\n")
            logg.write(f"Valid lines: {validated_lines}\n")
            logg.write(f"Ignored lines: {ignored_lines}\n")
            logg.write(f"Lines with fails: {failed_lines}\n")
            logg.write(f"Max. value: {(max(validated_numbers)):.2f}\n")
            logg.write(f"Min. value: {(min(validated_numbers)):.2f}\n")
            logg.write(f"Average value: {(sum(validated_numbers) / validated_lines):.2f}\n")






        


        




    
if __name__ == "__main__":
    main()