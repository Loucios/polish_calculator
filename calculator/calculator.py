class Calculator:
    def __init__(self, sequence: 'list[str]') -> None:
        self.sequence = sequence

    def get_result(self) -> int:
        stack = Stack()
        result = 0

        for element in self.sequence:
            if element == '+':
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number + second_number
                stack.push(result)
                continue
            if element == '-':
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number - second_number
                stack.push(result)
                continue
            if element == '*':
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number * second_number
                stack.push(result)
                continue
            if element == '/':
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number // second_number
                stack.push(result)
                continue
            stack.push(int(element))

        return stack.pop()


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if not self.items:
            return None
        return self.items.pop()
