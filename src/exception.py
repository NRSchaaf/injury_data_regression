class CustomException(Exception):
    """A custom exception class"""

    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"


def main():
    try:
        # Example code that may raise the custom exception
        raise CustomException("This is a custom exception.")
    except CustomException as e:
        print(e)


if __name__ == "__main__":
    main()