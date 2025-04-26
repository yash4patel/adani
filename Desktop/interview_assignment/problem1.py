
def frequency(num,k):
    freq={} #map initialization
    for n in num: #loop 
        if n in freq:#checking frequence of an element
            freq[n]+=1 
        else:
            freq[n]=1 #if element is not present frequence of element is 1

    freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)) #sorting based on values
 
    result = list(freq.keys())[:k] #taking top k element

    return result


nums = [1, 2, 3]
k=3
print(frequency(nums,k))