from jjjxutils.decorators import entrypoint, compute, bind


# The compute decorator will execute the function and return the result. This is equivalent to:
# addition = addition()
@compute
# The bind decorator will bind the arguments to the function. This is equivalent to:
# addition = lambda *args, **kwargs: addition(2, 3, *args, **kwargs)
@bind(2, 3)
def addition(x, y) -> int:
    return x + y


# The entrypoint decorator will execute the main function if the script is run directly. This is equivalent to:
# if __name__ == "__main__":
#     main()
@entrypoint
def main() -> None:
    print(addition)


# Executing this will print 5
