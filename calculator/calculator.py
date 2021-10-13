import operator


class Calculator:
    def __init__(self, sequence: 'list[str]') -> None:
        self.__sequence = sequence

    def get_result(self) -> int:
        stack = Stack()
        result = 0

        operator_sequence = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv
        }

        for element in self.__sequence:

            register = False
            for key, value in operator_sequence.items():
                if element == key:
                    second_number = stack.pop()
                    first_number = stack.pop()
                    result = value(first_number, second_number)
                    stack.push(result)
                    register = True
                    break

            if not register:
                stack.push(int(element))

        return stack.pop()


class Stack:
    def __init__(self) -> None:
        self.__items = []

    def push(self, item: int) -> None:
        self.__items.append(item)

    def pop(self) -> int:
        if not self.__items:
            return None
        return self.__items.pop()
