
filename = input("Enter the name of the file to read: ")

try:
    file = open(filename, "r")
    content = file.read()
    file.close()

    print("File content:")
    print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")
