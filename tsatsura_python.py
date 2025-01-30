import re


# Task 1
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_splitable_and_int(input_string):
    # Split the input string by spaces
    split_result = input_string.split()
    
    # Check if the split result has more than one element
    if len(split_result) > 1:
        for i in split_result:
            if not is_int(i):
                # print("Array must be of integer data only!")
                return False
        return True
    else:
        # print("Array was entered not properly!")
        return False
# Task 1


# Task 2
def get_key_from_value(d, value):
    return next((key for key, val in d.items() if val == value), None)


#def contains_brackets(s):
#    return '(' in s or ')' in s or '[' in s or ']' in s or '{' in s or '}' in s


def contains_brackets(s):
    return bool(re.search(r'[\(\)\[\]\{\}]', s))


def only_contains_brackets(s):
    return bool(re.fullmatch(r'[()\[\]{}]*', s))


def are_brackets_balanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False
    return stack == []


def correct_brackets(s):
    stack = []
    result = []

    # Dictionary to match opening and closing brackets
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(matching_bracket.values())

    for char in s:
        if char in opening_brackets:
            stack.append(char)
            result.append(char)
        elif char in matching_bracket:
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
                result.append(char)
            else:
                # If the closing bracket doesn't match, ignore it
                continue
        else:
            result.append(char)

    # Add any unmatched opening brackets at the end
    while stack:   
        try:
            # result.append(matching_bracket[stack.pop()])
            # print(stack)
            # print(matching_bracket)
            # print(get_key_from_value(matching_bracket, stack.pop()))

            result.append(get_key_from_value(matching_bracket, stack.pop()))
        except KeyError:
            print(KeyError)

    return ''.join(result)
# Task 2


#####


def task_number_input():
    while True:
        task = input("Choose task number by entering '1' or '2': ")
        if task == "1" or task == "2":
            return task
        else:
            print("It's must be '1' or '2'.")
            print("But you entered: " + task)
            print("Try again.")


def task_number_one():
    while True:
        value = input("Enter number, it must be integer (1, 10, 100) or float (1.1, 10.1, 100.1 and only with dot): ")
        if is_float(value) and float(value) > 7:
            print("Hello.")
            break
        elif is_float(value) and float(value) <= 7: 
            print("Nothing.")
            break
        else:
            print("Not a number or number was entered not properly, try again.")
    value = input("Enter name: ")
    if value == "John":
        print("Hello, " + value)
    else:
        print("There is no such name.")
    while True:
        value = input("Enter numeric array of integer numbers splited by spaces (for example: 1 2 3 4 5 ): ")
        if is_splitable_and_int(value):
            count = 0
            for i in value.split():
                if int(i) % 3 == 0:
                    print(i)
                    count += 1
            if count == 0:
                print("There is no elements in array that are multiples of 3.")
            else:
                print("Number of elements that are multiples of 3 is " + str(count))
            break
        else: 
            print("Not proper array, try again.")  


def task_number_two():
    while True:
        input_string = input("Enter sequence that contains brackets [] or {} or (): ")
        if contains_brackets(input_string): # or only_contains_brackets(input_string):
            if are_brackets_balanced(input_string):
                print("The sequence is correct because brackets are balanced in given sequence: " + input_string)
                break
            else:
                print("The sequence is not correct because brackets are not balanced in given sequence: " + input_string)
                balanced_string = correct_brackets(input_string)
                if are_brackets_balanced(balanced_string):
                    print("This is a correct sequence: " + balanced_string)
                    break
                else:
                    print("Something went wrong, try again.")
        else:
            print("No brackets in sequence at all, try again.")


def task_runner():
    task_number = task_number_input()
    print("Task number " + task_number)
    if task_number == "1":
        task_number_one()
    elif task_number == "2":
        task_number_two()


#####


task_runner()
while True:
    repeat = input("Do you want to repeat task 1 or 2? Enter 'yes' or 'no': ")
    if repeat.lower() == "yes":
        print("Good!")
        task_runner()
    elif repeat.lower() == "no":
        print("Ok, Good Bye!")
        break
    else:
        print("It's must be 'yes' or 'no'.")
        print("But you entered: " + repeat)
        print("Try again.")

