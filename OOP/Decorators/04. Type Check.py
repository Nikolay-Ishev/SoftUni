def type_check(filtered_type):
    def decorator(function):
        def wrapper(current_type):
            if isinstance(current_type,filtered_type):
                return function(current_type)
            return "Bad Type"
        return wrapper
    return decorator




@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))