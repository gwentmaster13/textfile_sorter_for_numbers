def file_open_action(file_name: str, text: str = "", method: str ="a") -> list[str] | None:
    with open(file_name, method, encoding="UTF-8") as f:
        if method == "r":
            return f.readlines()
        f.write(text)
        return None


def main():
    while True:
        user_file = input("Enter the name of the file: ")
        try:
            lines = file_open_action(file_name=user_file, method= "r")
            break
        except FileNotFoundError:
            file_open_action(file_name="logg.txt", text= f"Could not find {user_file} file.")
            print(f"Could not find {user_file} file.")
        except IOError:
            file_open_action(file_name="logg.txt", text= f"Error while getting Input/Output from the {user_file} file.")
            print("Something went wrong while working with file.")

    lines_checked = 0
    ignored_lines = 0
    failed_lines = 0
    validated_lines = 0
    validated_numbers = []

    for number_line, line in enumerate(lines):
        lines_checked += 1
        stripped_line = line.strip().split(" ")

        try:
            valid_line = float(stripped_line[0].replace(",", "."))
            validated_lines += 1
            validated_numbers.append(valid_line)

        except ValueError:
            if stripped_line[0] == "#" or stripped_line[0] == "":
                file_open_action(file_name="logg.txt", text= f'({number_line + 1}) line ignored: "{line.strip()}" \n /_Reason: Commented or empty line\n')
                ignored_lines += 1
            else:
                file_open_action(file_name="logg.txt", text= f'({number_line + 1}) line failed to validate: : "{line.strip()}" \n /_Reason: Line consists only of string(s)\n')               
                failed_lines += 1

    file_open_action(file_name="rapport.txt", text= f"Valid lines: {validated_lines}\n")

    if len(validated_numbers) > 0:
        rapport_text = (
        f"Average value: {sum(validated_numbers) / validated_lines}\n"
        f"Sum of data: {sum(validated_numbers):.2f}\n"
        f"Max. value: {max(validated_numbers):.2f}\n"
        f"Min. value: {min(validated_numbers):.2f}\n"
        )
    else:
        rapport_text = "No valid data was given to calculate."

    file_open_action(file_name= "rapport.txt", text= rapport_text)


    if len(validated_numbers) > 0:
        logg_text = (
        "=========RESULTS==========\n"
        f"Valid lines: {validated_lines}\n"
        f"Ignored lines: {ignored_lines}\n"
        f"Lines with fails: {failed_lines}\n"
        f"Max. value: {(max(validated_numbers)):.2f}\n"
        f"Min. value: {(min(validated_numbers)):.2f}\n"
        f"Average value: {(sum(validated_numbers) / validated_lines):.2f}\n"
        )
        file_open_action(file_name="logg.txt", text= logg_text)

    
if __name__ == "__main__":
    main()