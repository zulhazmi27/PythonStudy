def calcWeight(totalValue,totalweight, sortedweight, sortedvalue, w, i):
        excessweight = totalweight - w
        totalweight -= sortedweight[i]
        totalweight +=  ((sortedweight[i] - excessweight)/sortedweight[i]) * sortedweight[i]
        totalValue += ((sortedweight[i] - excessweight)/sortedweight[i]) * sortedvalue[i]
        
        print(f"total weight = {totalweight} and total value = {totalValue}")

def greedyAlgo(w, weight, value, n):
    if n == 0 or w == 0:
        return 0; #base case
    
    valueperweight = []
    
    for things in range(n):
        valueperweight.append(value[things]/weight[things])
    
    myDict = dict(zip(value, valueperweight))
    myDict2 = dict(zip(valueperweight, weight))
    
    sortedMyDict = sorted(myDict.items(), key = lambda x:x[1], reverse = True)
    myDict.clear()
    sortedMyDict2 = sorted(myDict2.items(), reverse = True)
    myDict2.clear()
    
    for keys, values in sortedMyDict:
        myDict[keys] = values
        
    for keys, values in sortedMyDict2:
        myDict2[keys] = values
    
    sortedweight = list(myDict2.values())
    sortedvalueperweight = list(myDict.values())
    sortedvalue = list(myDict.keys())
    
    totalWeight = 0
    totalValue = 0
    
    for i in range(n):
        if totalWeight < w:
            if sortedvalueperweight[i] >= sortedvalueperweight[i + 1]:
                totalWeight += sortedweight[i]
                if totalWeight > w:
                    return calcWeight(totalValue, totalWeight, sortedweight, sortedvalue, w, i)
                else:
                    totalValue += sortedvalue[i]
                        
            else:
                totalWeight += sortedweight[i + 1]
                if totalWeight > w:
                    return calcWeight(totalValue, totalWeight, sortedweight, sortedvalue, w, i + 1)
                else:
                    totalValue += sortedvalue[i + 1]
    
    return print(f"total weight = {totalWeight} and total value = {totalValue}")                
                    
            
        
weight = [2, 5, 10, 5]
value = [20, 30, 50, 10]
w = 16
n = len(weight)
greedyAlgo(w, weight, value, n)