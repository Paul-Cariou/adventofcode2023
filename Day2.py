import re

total_count = {"blue":14, "red":12, "green":13}

def day2_part1():  
    f = open("day2.txt")
    
    res = 0
    for l in f:
        
        #liste entiere ['Game 5', '6 red, 1 blue, 3 green', '2 blue, 1 red, 2 green']
        L = re.split(": |; ",l.replace("\n",""))
        game_nbr = int(L[0][5:])
        possible = True
        
        #pour chaque partie de la game #
        for i in range(1,len(L)):
            game_set = re.split(", ", L[i])
            numbers = []
            colors = []
            
            for elt in game_set:
                nbr_color = re.split(" ",elt)
                
                numbers.append(int(nbr_color[0]))
                colors.append(nbr_color[1])
            set_dict=dict(zip(colors,numbers))
                        
            for key in set_dict.keys():
                if total_count[key] < set_dict[key]:
                    possible = False
                    
        if possible:
            res+=game_nbr
    return res


def day2_part2():
    f = open("day2.txt")
    
    res = 0
    for l in f:
        
        #liste entiere ['Game 5', '6 red, 1 blue, 3 green', '2 blue, 1 red, 2 green']
        L = re.split(": |; ",l.replace("\n",""))
        minimum = {"blue":0, "red":0, "green":0}
        power=1
        
        #pour chaque partie de la game #
        for i in range(1,len(L)):
            game_set = re.split(", ", L[i])
            numbers = []
            colors = []
            
            for elt in game_set:
                nbr_color = re.split(" ",elt)
                
                numbers.append(int(nbr_color[0]))
                colors.append(nbr_color[1])
            set_dict=dict(zip(colors,numbers))
                        
            for key in set_dict.keys():
                if minimum[key] < set_dict[key]:
                    minimum[key] = set_dict[key]
        
        for key in minimum.keys():
            power*=minimum[key]
                
        res+=power
    return res
