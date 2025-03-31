with open("input.txt", "w") as file:
    file.write("learning python file writing and reading is fun\n")



fileName = 'input.txt'
with open(fileName,"a") as fileObject:
    fileObject.write("i love software dev\n")
    fileObject.write("i hope to make it in the software dev field\n")


with open("input.txt","r") as file:
    data = file.read()
    print(data)

inputFilename = input("Enter name of  input file: ")
inputFile = open(inputFilename, "r")
print("Opening file", inputFilename, " for reading")

for line in inputFile:
    print(line)

print("Completed reading", inputFilename)


