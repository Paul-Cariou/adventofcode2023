def day1_part1():
    f=open("C:\\ESILV\\A4\\Calendar\\day1.txt","r")
 
    total=0
    right_order=True
    for l in f:
        res=0
        for i in l:
            if i.isdigit() & right_order:
                res+=int(i)*10
                right_order=False
        for i in l[::-1]:
             if i.isdigit() & (not right_order):
                 res+=int(i)
                 right_order=True
        total+=res
    return total

numbers={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def day1_part2():
    f=open("C:\\ESILV\\A4\\Calendar\\day1.txt","r")
    
    total=0
    right_order=True
    for l in f:
        res=0
        for i in range(len(l)):
                if l[i].isdigit() & right_order:
                    res+=int(l[i])*10
                    right_order=False
                for key in numbers.keys():
                    if (l[i:i+len(key)]==key) & right_order:
                        res+=numbers[key]*10
                        right_order=False
        for i in range(len(l)-1,-1,-1):
                if l[i].isdigit() & (not right_order):
                    res+=int(l[i])
                    right_order=True
                for key in numbers.keys():
                    if (l[i-len(key):i]==key) & (not right_order):
                        res+=numbers[key]
                        right_order=True
        total+=res
    return total
            
            
        