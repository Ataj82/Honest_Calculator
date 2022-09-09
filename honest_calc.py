msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(a):
    try:
        if a == int(a):
            return -10 < a < 10
    except ValueError:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v3):
        msg += msg_6
    if v2 == "*" and (v1 == 1 or v3 == 1):
        msg += msg_7
    if (v1 == 0 or v3 == 0) and (v2 != "/"):
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


running = True
memory = 0
while running:
    print(msg_0)
    user_input = input()
    x, operation, y = user_input.split()

    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if operation not in "+-/*":
        print(msg_2)
        continue

    check(x, operation, y)

    result = 0
    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        if y == 0:
            print(msg_3)
            continue
        else:
            result = x / y
    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:
                    if msg_index == 10:
                        print(msg_10)
                    elif msg_index == 11:
                        print(msg_11)
                    else:
                        print(msg_12)
                    answer = input()
                    if answer == "y":
                        msg_index += 1
                    else:
                        break
                else:
                    memory = result
            else:
                memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            running = False
