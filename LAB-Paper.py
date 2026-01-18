import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import queue

def checkprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        print(i)
        if n % i == 0:
            return False
    return True

res=checkprime(11)
print(res) 

def fibonacciseries(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


result = fibonacciseries(5)
print(result)


def reverse(n):
    while(n > 0):
        digit = n % 10
        print(digit, end="")
        n = n // 10
    print()  # For a new line after printing the digits

reverse(1234)

sensor_performance = {
    "SENSOR_01": {"Successful_Readings": 120},
    "SENSOR_02": {"Successful_Readings": 0},
    "SENSOR_03": {"Successful_Readings": 45},
    "SENSOR_04": {"Successful_Readings": 0},
    "SENSOR_05": {"Successful_Readings": 89}
}

for(sensor, data) in sensor_performance.items():
    if data["Successful_Readings"] == 0:
        print(f"{sensor} has failed.")

n=0
while(n<=20):
    if(n%2==0):
        print(f"{n} is even")
    n+=1

count=0
sum=0
n=100
while(count<=n):
    sum=sum+count
    count=count+1


print(f"Counting completed. {sum}")


name="honeypot"
age=19
print(f"My name is {name} and I am {age} years old.")


array=[4,3,2,1,1,"string",True]
print(array)
array.append(5)
print(array)
array.remove(3)
print(array)
array.pop()
print(array)
print(len(array))
array.insert(2,10)
print(array)

tuple_data=(1,2,3,4,5,5,"string",False)
print(tuple_data)

productIDsinPickingQueue=["A001","B002","C003","D004"]
print(productIDsinPickingQueue)
dimensionOfpallet=(100,200,300)
print(dimensionOfpallet)
uniquelocaionid={3,4,1,2,6,8,9,9}
print(uniquelocaionid)
productID={
    "p1":200,
    "p4":322,
    "p2":51,
    "p4":12    
}

for i,j in productID.items():
    print(f"Product ID: {i}, Quantity: {j}") 



def checkstock(dict):
    for i,j in dict.items():
        if i.startswith("p4") and j<100:
            print(f"Product {i} is low in stock with quantity {j}")
        
print(checkstock(productID))


dict2={
    "reading1":0,
    "reading2":23,
    "reading3":45,
    "reading4":0
}

for i,j in dict2.items():
    if j==0:
        print(f"the sensor {i} has failed")
    

dict3={
    ("stud1","stud2","stud3"):[85,90,78,(22,11)],
    ("stud4","stud5"):(88,76,[1,2,3]),
    ("stud6","stud7","stud8"):{90,92,85}
}

print(dict3["stud4","stud5"])
print(dict3["stud1","stud2","stud3"])


list1=[1,2,3,4,5]
list1.insert(4,11)
print(list1)

tuple=(dict3,dict2)
print(tuple)

print(tuple[0]["stud1","stud2","stud3"]) 

list9=[dict3,dict2]
print(list9[1]["reading3"])


set1={1,2,3,4,5,5,6,7,8,8}

print(set1)




np_array=np.array([1,2,3,4,5])
print(np_array) 
print(type(np_array))


graph={
    'A': {'B':10, 'C':5},
    'B': {'D':1},
    'C': {'D':3, 'E':2},
    'D': {'F':4},
    'E': {'F':8},
    'F': {'G':3}
}
start='A'
goal='G'

def ucs(start,goal,graph):
    pq=queue.PriorityQueue()
    pq.put((0,start))
    visited = set()
    while not pq.empty():
        cost,path=pq.get()
        node=path[-1]
        if node==goal:
            return path,cost
        if node not in visited:
            visited.add(node)
            for neighbour,weight in graph[node].items():
                newpath=list(path)
                newpath.append(neighbour)
                pq.put((cost + weight, newpath))  
    return None,float('inf')

path,totalcost=ucs(start,goal,graph)
print("Path found by UCS:",path,"with total cost:",totalcost)


financial_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Revenue": [120000, 135000, 128000, 142000, 150000, 138000, 
                145000, 155000, 160000, 158000, 162000, 170000],
    "Market_Sector": ["Tech", "Finance", "Health", "Tech", "Finance", "Health",
                      "Tech", "Finance", "Health", "Tech", "Finance", "Health"],
    "Trading_Day_Type": ["Bullish", "Bearish", "Bullish", "Bearish", "Bullish", "Bearish",
                         "Bullish", "Bearish", "Bullish", "Bearish", "Bullish", "Bearish"]
})

avgpersector = financial_data.groupby("Market_Sector")["Revenue"].mean()
print("Average Revenue per Market Sector:")
print(avgpersector)

peaktradingdaytype = financial_data.groupby("Trading_Day_Type")["Revenue"].sum().idxmax()
print(f"Trading Day Type with highest total revenue: {peaktradingdaytype}")

varianceinmonthlyrevenue = financial_data["Revenue"].var()
print(f"Variance in Monthly Revenue: {varianceinmonthlyrevenue}")