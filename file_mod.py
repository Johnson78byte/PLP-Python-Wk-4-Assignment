
file = open("read.txt", "r")
content = file.read()
file.close()

# Modify the content
modified_content = content.upper()

new_file = open("write.txt", "w")
new_file.write(modified_content)
new_file.close()

print("Modified content written to write.txt")