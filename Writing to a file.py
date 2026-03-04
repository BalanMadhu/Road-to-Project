# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, Python!\nThis is file handling practice.")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)