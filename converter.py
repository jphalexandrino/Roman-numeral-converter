from colorama import Fore, Style, init

# Teste
init(autoreset=True)

def int_to_roman(number):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num


def roman_to_int(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0
    for numeral in reversed(roman):
        value = roman_dict[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result


def main():
    while True:
        print(f"\n{Fore.BLUE}Select an option:")
        print(f"\n{Fore.BLUE}1. {Fore.GREEN}Convert number to Roman numeral")
        print(f"{Fore.BLUE}2. {Fore.GREEN}Convert Roman numeral to number")
        print(f"{Fore.BLUE}3. {Fore.GREEN}Exit")

        choice = input(f"\n{Fore.YELLOW}Enter the number of the desired option: ")

        if choice == "1":
            num = int(input("\nEnter the number to convert to Roman numeral: "))
            print(f"\n{Fore.YELLOW}Roman numeral: {int_to_roman(num)}")
        elif choice == "2":
            roman = input("Enter the Roman numeral to convert to number: ")
            print(f"\n{Fore.YELLOW}Number: {roman_to_int(roman)}")
        elif choice == "3":
            print(f"\n{Fore.RED}Exiting the program.")
            break
        else:
            print(f"\n{Fore.RED}Invalid option. Please try again.")


if __name__ == "__main__":
    main()
