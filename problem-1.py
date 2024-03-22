def sqrt(number):
    if number == 0 or number == 1:
        return number
    
    start, end = 1, number // 2
    
    while start <= end:
        mid = (start + end) // 2
        mid_squared = mid * mid
        
        if mid_squared == number:
            return mid
        elif mid_squared < number:
            start = mid + 1
            floor_sqrt = mid
        else:
            end = mid - 1
    return floor_sqrt

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print("Pass" if (2 == sqrt(8)) else "Fail")  
print("Pass" if (10 == sqrt(100)) else "Fail")  
print("Pass" if (31 == sqrt(1000)) else "Fail") 
print("Pass" if (0 == sqrt(0)) else "Fail") 
print("Pass" if (1 == sqrt(2)) else "Fail")  
print("Pass" if (999 == sqrt(998001)) else "Fail") 
print("Pass" if (316 == sqrt(100000)) else "Fail")  

print("Pass" if (46340 == sqrt(2147483647)) else "Fail") 
print("Pass" if (1 == sqrt(3)) else "Fail") 