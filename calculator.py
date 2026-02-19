from statistics import mean, median, mode, multimode


def get_numbers(prompt="Enter numbers separated by spaces: "):
    while True:
        try:
            nums = list(map(float, input(prompt).split()))
            if not nums:
                print("Please enter at least one number.")
                continue
            return nums
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def get_two_numbers():
    while True:
        try:
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def display_menu():
    print("\n" + "=" * 40)
    print("       🧮  PYTHON CALCULATOR")
    print("=" * 40)
    print("  Basic Operations:")
    print("   1. Addition       (+)")
    print("   2. Subtraction    (-)")
    print("   3. Multiplication (*)")
    print("   4. Division       (/)")
    print("   5. Modulus        (%)")
    print()
    print("  Statistical Operations:")
    print("   6. Mean")
    print("   7. Median")
    print("   8. Mode")
    print("   9. Average (same as Mean)")
    print()
    print("   0. Exit")
    print("=" * 40)


def run_calculator():
    while True:
        display_menu()
        choice = input("Select an option (0-9): ").strip()

        # ── Basic Operations ──────────────────────────────────────
        if choice == "1":
            a, b = get_two_numbers()
            result = a + b
            print(f"\n  {a} + {b} = {result}")

        elif choice == "2":
            a, b = get_two_numbers()
            result = a - b
            print(f"\n  {a} - {b} = {result}")

        elif choice == "3":
            a, b = get_two_numbers()
            result = a * b
            print(f"\n  {a} × {b} = {result}")

        elif choice == "4":
            a, b = get_two_numbers()
            if b == 0:
                print("\n  ❌ Error: Division by zero is not allowed.")
            else:
                result = a / b
                print(f"\n  {a} ÷ {b} = {result}")

        elif choice == "5":
            a, b = get_two_numbers()
            if b == 0:
                print("\n  ❌ Error: Modulus by zero is not allowed.")
            else:
                result = a % b
                print(f"\n  {a} % {b} = {result}")

        # ── Statistical Operations ────────────────────────────────
        elif choice in ("6", "9"):
            label = "Mean / Average"
            nums = get_numbers()
            result = mean(nums)
            print(f"\n  Numbers : {nums}")
            print(f"  {label} : {result}")

        elif choice == "7":
            nums = get_numbers()
            result = median(nums)
            print(f"\n  Numbers : {nums}")
            print(f"  Median  : {result}")

        elif choice == "8":
            nums = get_numbers()
            modes = multimode(nums)
            print(f"\n  Numbers : {nums}")
            if len(modes) == len(set(nums)):
                print("  Mode    : No mode (all values appear equally)")
            else:
                print(f"  Mode    : {modes[0] if len(modes) == 1 else modes}")

        elif choice == "0":
            print("\n  👋 Goodbye! Thanks for using the calculator.\n")
            break

        else:
            print("\n  ⚠️  Invalid option. Please choose between 0 and 9.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    run_calculator()
