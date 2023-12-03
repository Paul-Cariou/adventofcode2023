import re

def adjacent(previous_line,actual_line,next_line):
    
    nbr_list=[]
        
    matches=re.finditer(r'\d+',actual_line)
    nbr_with_index=[(match.group(), match.start()) for match in matches] #ex : [('12',1),('154',13)]
    
    for elt in nbr_with_index:   
        
        #nombre a gauche
        if elt[1] == 0: 
            au_dessus = previous_line[ elt[1]: elt[1]+len(elt[0])+1]
            en_dessous = next_line[ elt[1]: elt[1]+len(elt[0])+1]
            a_gauche = ""
            a_droite = actual_line[elt[1]+len(elt[0])]
            
        #nombre a droite
        elif elt[1]+len(elt[0])+1 > len(actual_line)-1:
            au_dessus = previous_line[ elt[1]-1: elt[1]+len(elt[0])]
            en_dessous = next_line[ elt[1]-1: elt[1]+len(elt[0])]
            a_gauche = actual_line[elt[1]-1]
            a_droite = ""
        
        #nombre normal
        else:
            au_dessus = previous_line[ elt[1]-1: elt[1]+len(elt[0])+1]
            en_dessous = next_line[ elt[1]-1: elt[1]+len(elt[0])+1]
            a_gauche = actual_line[elt[1]-1]
            a_droite = actual_line[elt[1]+len(elt[0])]
        
        contour = au_dessus + en_dessous + a_droite + a_gauche
        casual=".0123456789"
        
        for i in contour:
            if i not in casual:
                nbr_list.append(int(elt[0]))
            
    return nbr_list

def day3_part1(): 
    
    res=0   
    with open("C:\\ESILV\\A4\\Calendar\\day3.txt","r") as file:
        
        actual_line = file.readline().strip()
        previous_line = "."*len(actual_line)
        
        while actual_line:
            next_line = file.readline().strip()
    
            # print(previous_line, " Previous line")
            # print(actual_line, " Actual line")
            # print(next_line, " Next line")
            
            nbr_list = adjacent(previous_line,actual_line,next_line)
            # print("Number saved", nbr_list)            
    
            for nbr in nbr_list:
                res+=nbr
                
            # print("TOTAL : ",res)
            # print("-----------------------------------------")
    
            previous_line = actual_line
            actual_line = next_line
    return res

#%%

def gear_nbrs(previous_nbr,actual_nbr,next_nbr,star_index, length):
    
    res=[]
    
    for ind in star_index:
        
        temp_nbr=[]
        
        for elt in previous_nbr:
            if ind in [i for i in range(elt[1]-1,elt[1]+len(elt[0])+1)]:
                temp_nbr.append(int(elt[0]))
        for elt in next_nbr:
            if ind in [i for i in range(elt[1]-1,elt[1]+len(elt[0])+1)]:
                temp_nbr.append(int(elt[0]))
        for elt in actual_nbr:
            if ind == elt[1]+len(elt[0]):
                temp_nbr.append(int(elt[0]))
            if ind == elt[1]-1:
                temp_nbr.append(int(elt[0]))
        
        if len(temp_nbr)==2:
            res+=(temp_nbr[0],temp_nbr[1])
    
    return res

def day3_part2(): 
    
    res=0   
    with open("C:\\ESILV\\A4\\Calendar\\day3.txt","r") as file:
        
        actual_line = file.readline().strip()
        length = len(actual_line)
        previous_line = "."*len(actual_line)
        
        find_previous = re.finditer(r'\d+', previous_line)
        previous_nbr = [(find.group(), find.start()) for find in find_previous]
        
        find_actual = re.finditer(r'\d+', actual_line)
        actual_nbr = [(find.group(), find.start()) for find in find_actual]
        
        while actual_line:
            next_line = file.readline().strip()
            
            find_next = re.finditer(r'\d+', next_line)
            next_nbr = [(find.group(), find.start()) for find in find_next]
    
            # print(previous_line, " Previous line")
            # print(actual_line, " Actual line")
            # print(next_line, " Next line") 
            
            matches = re.finditer(r'\*', actual_line)
            star_index = [match.start() for match in matches]
                        
            nbr_list = gear_nbrs(previous_nbr, actual_nbr, next_nbr, star_index, length)
            # print("Number saved", nbr_list)   
            
            # print(nbr_list)
            product = 0
            for k in range(0,len(nbr_list),2):
                product += nbr_list[k]*nbr_list[k+1]
            
            res+=product
                
            # print("TOTAL : ",res)
            # print("-----------------------------------------")
    
            previous_line = actual_line
            actual_line = next_line
            
            previous_nbr = actual_nbr
            actual_nbr = next_nbr
    return res    
    

        