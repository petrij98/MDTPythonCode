import os

import docx

import re

validInstances = 0

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
    global validInstances
    testableDoc = document
    #print("Test Flag 1")
    for i in range(0,len(testableDoc)-14):
        print("Testing...")
        for a in range(192,193):
            for b in range(0,20):
               #print(validInstances)
                #print("Testing IPs in range of: " + str(a) +"." + str(b) + ".###.###")
                for c in range(0,20):
                    for d in range(0,120):
                        for k in range(7,15):
                            #print("Pass " + str(k-6) + "/9 completed.")
                            #print("Testing for: " + str(a) + "." + str(b) + "." + str(c) + "."+ str(d))
                            if testableDoc[i:i+k] == str(str(a) + "." + str(b) + "." + str(c) + "." + str(d)):
                                #print("Instance found!")
                                validInstances+=1 #print(pdf[i:i+15])
                                print('Instance found!')
                                print(validInstances)

def findIPs2(document):
    global validInstances
    testableDoc = document
    DesiredIP = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        for i in range(0,len(testableDoc)-6):
            if DesiredIP.match(testableDoc[i:i+):
                validInstances+=1
                #print("Instance found!")
#Main Program        
X = openDoc()
Y = DocumentMaterial(X)
#findIPs(Y)
findIPs2(Y)
print(validInstances)

        
#print()
#print("There are " + str(validInstances) + " instances of IPs found.")