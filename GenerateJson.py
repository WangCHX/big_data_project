'''
Created on Nov 25, 2014

@author: zhangtong
'''
import json

def genJson(inFile, outFile):
    dic = dict()
    dic["name"] = "flare"
    dic["children"] = []
    
    subdic = dict()
    count = 0
    
    for line in inFile:
        print line + '\t'
        str1, str2 = line.strip().split(',', 1)
        print str1, " ", str2
        if count == 0:
            subdic["name"] = str1
            subdic["children"] = []
        if int(str2) > 100:
            item = dict()
            item["name"] = str1
            item["size"] = int(str2)
            subdic["children"].append(item)
            count = count + 1
        if count == 5:
            dic["children"].append(dict(subdic))
            count = 0
    if count != 0:
        dic["children"].append(dict(subdic))
        
    outFile.write(json.dumps(dic))
    
def main():
    inFile = open("/Users/zhangtong/Desktop/PROGRAMMING_FOR_BIG_DATA/final_project/num.tsv")
    outFile = open("/Users/zhangtong/Desktop/PROGRAMMING_FOR_BIG_DATA/final_project/output.json", 'w')
    genJson(inFile, outFile)
    
if __name__ == '__main__':
    main()
            