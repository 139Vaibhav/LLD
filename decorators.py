def lower_case_decorator(function):
    def wrapper(*args, **kwargs):
        original_result = function(*args, **kwargs)
        modified_result = original_result.lower()
        return modified_result
    return wrapper

if __name__ == "__main__":
    @lower_case_decorator
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Vaibhav is GREAT"))  # Output: hello, vaibhav is great
