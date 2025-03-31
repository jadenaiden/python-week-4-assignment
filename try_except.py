inputFileOk = False
while(inputFileOk == False):
    try:
        inputFilename = input("Enter name of  input file: ")
        inputFile = open(inputFilename, "r")
    except FileNotFoundError:
        print("File", inputFilename, " could not be opened for reading")
    else:
        print("Opening file", inputFilename, " for reading")
        inputFileOk = True

        for line in inputFile:
            print(line)