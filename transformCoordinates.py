#Transforms JSON file data for maps into a format compatible with WP Google Maps

#read in json file information
def readIn(fileName):
    #print("inside function")
    #print(fileName)
    #file = open(fileName, 'r')

    #open the file
    with open(fileName) as f:
        contents = f.read() #reading in file contents
    
    f.close()

    return contents

#Delete the unnecessary information at beginning and end and find and replace ],[ with new line
def modifyContents(contents):
    #we need to remove contents before [[[[ 
    #finding index for those characters
    startIndex = contents.find('[[[')

    #modify the string
    contents = contents[startIndex+3:-8]

    #find and replace ],[ with new line
    contents = contents.replace("],[", "\n")
    return contents

#find nth occurance of substring in string - something about recursion
# def findSubstring(stirng, substring, n):
#     if (n == 0):
#         return string.find(substring)
#     else:
#         return string.find(substring, findSubstring(string, substring, n-1) +1)


def findNthSubstring(contents, substring, n):
    start = contents.find(substring)
    while start >= 0 and n > 1:
        start = contents.find(substring, start+len(substring))
        n -= 1
    return start


#switches coordinates
def switcheroo(contents):
    
    #count the number of coordinates to switch
    numCoordinates = 0
    for i in contents:
        if i == ',':
            numCoordinates += 1


    for i in range(1, numCoordinates+1):
        
        if i == 1:
            break0 = 0
        else:
            break0 = findNthSubstring(contents, '\n', i-1) + 1

        break1 = findNthSubstring(contents, ',', i)
        break2 = findNthSubstring(contents, '\n', i)
        
        #finding middle of coordinate line and separating longitude and latitde
        break1 = findNthSubstring(contents, ',', i)
        break2 = findNthSubstring(contents, '\n', i)
        
        longitude = contents[break0:break1]
        latitude = contents[break1+1:break2]

        #print(longitude)
        #print(latitude)
        #contents = contents.replace(contents[break0:break2], "hi")

        contents = (contents.replace(contents[break0:break2], latitude + "," + longitude))
        #print(contents1[break0:break2])
    
    return contents

def transformCoordinates(contents):
    contents = contents.replace("\n", "),(")
    contents = "(" + contents + ")"
    return contents

def writeToFile(contents):
    newFileName = fileName.replace(".json", ".txt")
    print("Writing to file: " + newFileName)
    
    #file object stuff
    f = open(newFileName, "w+")
    f.write(contents)
    f.close()

    print("Done")


#Get file name
fileName = input("JSON file name: ")
contents = readIn(fileName)
modifiedContents = modifyContents(contents)
modifiedContents = switcheroo(modifiedContents)
modifiedContents = transformCoordinates(modifiedContents)

writeToFile(modifiedContents)

#print(modifiedContents)