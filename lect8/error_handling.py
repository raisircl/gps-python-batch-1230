try:
    with open("abcdata.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Error: The file 'abcdata.txt' was not found.")