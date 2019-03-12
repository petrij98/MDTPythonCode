import os

import docx

import re

docLength = 0
validPages = 0

#Opens Document
def openDoc():
    desiredDoc = input("Enter desired document: ")
    Doc = docx.Document(str(desiredDoc))
    return Doc
    
#Grabs Material
def DocumentMaterial(Doc):
    Material = []
    for para in Doc.paragraphs:
        Material.append(para.text)
    #print(Material)
    return '\n'.join(Material)

#Searches current page for IPs
def findIPs(document):
    global validPages
    testableDoc = document
    DesiredIP = "192."#re.compile("%03d" + '.' "%03d" + '.' "%03d" + '.' "%03d") #"192.168.0.1"# #("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$") 
    #print(DesiredIP)
    #print(testableDoc)
    for i in range(0,len(testableDoc)-3):
        if testableDoc[i:i+4]==DesiredIP:#.match(document[i:i+15]):
            validPages+=1#print(pdf[i:i+15])
            #return "true"
 
#Main Program        
X = openDoc()
Y = DocumentMaterial(X)
findIPs(Y)
#print(validPages)

        
#print()
print("There are " + str(validPages) + " instances of IPs found.")