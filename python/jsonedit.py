import json
import sys

if len(sys.argv) < 1:
    print("Error: too few arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Error: too many arguments")
    sys.exit(1)

inputfile = sys.argv[1]
outputfile = sys.argv[1]

if len(sys.argv) > 2:
    outputfile = sys.argv[2]
    
def readfile(filename):
    with open(filename) as contents:
        jsondata = json.load(contents)
        return jsondata
    return []

def writefile(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def update(input):
    output = []
    for value in input:
        newvalue = value.copy()
        
        # Write your transformation of the data here
        
        output.append(newvalue)
    return output

data = readfile(inputfile)
transformed = update(data)
writefile(transformed, outputfile)
