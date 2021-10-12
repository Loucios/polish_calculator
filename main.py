# https://github.com/Loucios/polish_calculator
# ID 54487318

from calculator.calculator import Calculator


def main():
    try:
        sequence = [element for element in input().split(' ')]
    except ValueError as e:
        print(f'Wrong input {e}')
        return

    calculator = Calculator(sequence)
    result = calculator.get_result()

    print(result)


if __name__ == "__main__":
    main()
