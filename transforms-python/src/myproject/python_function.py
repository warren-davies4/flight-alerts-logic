from functions.api import function, String


@function
def my_function() -> String:
    return "Hello World!"
