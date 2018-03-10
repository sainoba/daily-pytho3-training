# Import the library that makes it easier to write context managers 

# Implement a context manager that writes to a text file
# using a class:
class MyContextManager:
    pass


# Implement a context manager using a method with a decorator
def my_context_manager():
    raise Exception("Method not implemented")


def call_class_context_manager(file_name="class_hi.txt", text="hello", access_mode="w"):
    with MyContextManager(file_name, access_mode) as f:
        f.write(text)


def call_function_context_manager(file_name="function_hi.txt", text="hello", access_mode="w"):
    with my_context_manager(file_name, access_mode) as f:
        f.write(text)
