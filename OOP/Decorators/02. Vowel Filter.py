def vowel_filter(function):
    def wrapper():
        pattern = "AEOUYIaeouyi"
        return [x for x in function() if x in pattern]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
