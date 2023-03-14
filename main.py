alphabet = "abcdefghijklmnopqrstuvwxyz"

precedence = {
    "*": 3,
    "|": 2,
    "&": 2,
    "+": 1
}

operators = {
    "!": (1, lambda a : not a),
    "*": (2, lambda a, b: a and b),
    "|": (2, lambda a, b: a != b),
    "&": (2, lambda a, b: a == b),
    "+": (2, lambda a, b: a or b)
}

def clean(data):
    data = data.replace(" ", "").lower()
    i = 0
    while i < len(data):
        if data[i] in alphabet + ")" and i + 1 < len(data) and data[i + 1] in alphabet + "!" + "(":
            data = data[0:i + 1] + "*" + data[i + 1:]
        if data[i] == "!":
            if data[i + 1] != "(":
                end = i + 1
                while data[end] == "!":
                    end += 1
                data = data[0:i + 1] + "(" + data[i + 1:end + 1] + ")" + data[end + 1:]
        i += 1
    return data

def postfix(data):
    output = []
    stack = []
    for char in data:
        if char in alphabet:
            output.append(char)
        elif char == "!":
            stack.append(char)
        elif char in precedence.keys():
            while len(stack) > 0 and stack[-1] != "(" and precedence[stack[-1]] >= precedence[char]:
                output.append(stack.pop())
            stack.append(char)
        elif char == "(":
            stack.append(char)
        else:
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
            if len(stack) > 0 and stack[-1] == "!":
                output.append(stack.pop())
    while len(stack) > 0:
        output.append(stack.pop())
    return "".join(output)

def evaluate(data, parameters):
    stack = []
    for char in data:
        if char in alphabet:
            stack.append(parameters[alphabet.index(char)])
        else:
            number_of_values, do_it = operators[char]
            stack.append(do_it(*[stack.pop() for i in range(number_of_values)][::-1]))
    return stack[0]

if __name__ == "__main__":
    data = input()
    data = postfix(clean(data))
    number_of_variables = 0
    while alphabet[number_of_variables] in data:
        number_of_variables += 1
    all_variables = []
    queue = [[]]
    while queue:
        item = queue.pop()
        if len(item) == number_of_variables:
            all_variables.append(item)
        else:
            queue.append(item + [False])
            queue.append(item + [True])
    correct_variables = list(filter(lambda x : evaluate(data, x), all_variables))
    print("\n".join([str(variables).replace("True", "1").replace("False", "0") for variables in correct_variables]))
