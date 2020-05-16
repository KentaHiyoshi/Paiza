
import numpy as np

input_line = int(input())

numbers = np.zeros((input_line, input_line))
ZeroPointList=[]
for i in range(input_line):
    input_line_num=input().rstrip().split(' ')
    
    for j in range(len(input_line_num)):
        numbers[i][j]=int(input_line_num[j])
        if(numbers[i][j]==0):
            #zeropointlistは[x1,y1,x2,y2]の形式
            ZeroPointList.append(i)
            ZeroPointList.append(j)
            
            
#ある列の総和を求める
CalcNumber=None
SumNumber=0
for i in range(input_line):
    if ZeroPointList[1]!=i and ZeroPointList[3]!=i:
        CalcNumber=i

for i in range(input_line):
    SumNumber=SumNumber+numbers[i][CalcNumber]

#一つ目の値の算出
FirstSum1=int(0)
FirstSum2=int(0)
FirstValue=int(0)

for i in range(input_line):
    FirstSum1=FirstSum1 + numbers[i][ZeroPointList[1]]
    FirstSum2=FirstSum2 + numbers[ZeroPointList[0]][i]
    
if FirstSum1 >= FirstSum2:
    FirstValue = int(SumNumber - FirstSum1)
else:
    FirstValue = int(SumNumber - FirstSum2)

    
#二つ目の値を算出
SecondSum1=int(0)
SecondSum2=int(0)
SecondValue=int(0)
for i in range(input_line):
    SecondSum1=SecondSum1 + numbers[i][ZeroPointList[3]]
    SecondSum2=SecondSum2 + numbers[ZeroPointList[2]][i]
    
if FirstSum1 >= FirstSum2:
    SecondValue = int(SumNumber - SecondSum1)
else:
    SecondValue = int(SumNumber - SecondSum2)


numbers[ZeroPointList[0]][ZeroPointList[1]] = int(FirstValue)
numbers[ZeroPointList[2]][ZeroPointList[3]] = int(SecondValue)
        


for i in range(input_line):
    PrintStr=""
    for j in range(input_line):
        if(j == input_line-1):
            PrintStr += str(int(numbers[i][j]))
        else:
            PrintStr += str(int(numbers[i][j])) + " "
    print(PrintStr)
        