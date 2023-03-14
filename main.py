alphabet = "abcdefghijklmnopqrstuvwxyz"
data = "!a + !(!b + c)"
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
        if data[i] in alphabet and data[i + 1] in alphabet + "!" + "(":
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
            if stack[-1] == "!":
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
            if char == "!":

