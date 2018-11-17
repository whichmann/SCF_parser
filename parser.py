import re
import matplotlib.pyplot as plt


data = []
indexList = []
valueList_E = []
valueList_dE = []
valueList_dH = []

# flag is used to mark a line that contains relevant information
flag = False


# file handling manager, opens log from 
with open('log.log', 'r') as f:
    for line in f:
        if "E =" in line:
            flag = True
            if flag:
                data.append(line)
            if line.strip().endswith('|'):
                flag = False

with open('cleanData.txt', 'a+') as cleanFile:
    for i in data:
        i = i[6:57]
        cleanFile.write(i + '\n')

# in this scenario, each relevant line, contains three seperate interesting data.
# code below slices it accordingly and store each piece of information in a seperate list
# to use it later as a source data for the graph
for i in data:
    i = i[6:57]
    indexList.append(len(indexList))
    valueList_E.append(float(re.search(r'-?\d*\.\d*', i).group()))
    i = i[16:]
    valueList_dE.append(float(re.search(r'[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)', i).group()))
    i = i[16:]
    valueList_dH.append(float(re.search(r'[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)', i).group()))

# console check for validation purpose:
print(indexList)
print(len(indexList))
print(valueList_E)
print(len(valueList_E))
print(valueList_dE)
print(len(valueList_dE))
print(valueList_dH)
print(len(valueList_dH))


x = indexList
y = valueList_dH
z = valueList_dE
u = valueList_E

plt.plot(x, z, y)
plt.ylabel('dH & dE')
plt.xlabel('index')
plt.show()

plt.ylabel('E')
plt.xlabel('index')
plt.plot(x, u)
plt.show()

# appr wielomianem