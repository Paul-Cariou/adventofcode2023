import re
import numpy as np

def day4_part1():
    with open('day4.txt','r') as file:
        
        res=[]
        total_score = 0
        for l in file:
            
            game_res=[]        
            splitted_l = l.split("|")
            
            for i in range(len(splitted_l)):
                bet_numbers = re.findall('\d+', splitted_l[i])
                numbers = list(map(lambda x: int(x), bet_numbers))
                if i == 0:
                    bet = np.sort(numbers[1:])
                    game_nbr = numbers[0]
                    
                else:
                    draw = np.sort(numbers)
            
            # print("Game :", game_nbr)
            # print(bet, draw)
            
            ind_bet = 0
            ind_draw = 0
            score = -1
            
            while (ind_bet <= len(bet)-1) and (ind_draw <= len(draw)-1):
                if bet[ind_bet] < draw[ind_draw]:
                    ind_bet += 1
                elif bet[ind_bet] > draw[ind_draw]:
                    ind_draw += 1
                else:
                    res.append(bet[ind_bet])
                    game_res.append(bet[ind_bet])
                    ind_bet += 1
                    ind_draw +=1
                    score += 1
            
            if game_res != []:
                score = 2**score
                total_score += score
                
        # print("Total :",total_score)
        return total_score    

#%%

def day4_part2():   
    with open('day4.txt','r') as file:
        
        res=[]
        total_score = 0
        scratch_cards= {}
        scratch_cards["Game "+str(1)] = 1
    
        for l in file:
            
            game_res=[]
            
            splitted_l = l.split("|")
            
            for i in range(len(splitted_l)):
                bet_numbers = re.findall('\d+', splitted_l[i])
                numbers = list(map(lambda x: int(x), bet_numbers))
                if i == 0:
                    bet = np.sort(numbers[1:])
                    game_nbr = numbers[0]
                    
                else:
                    draw = np.sort(numbers)
            
            # print("Game :", game_nbr)
            # print(bet, draw)
            
            ind_bet = 0
            ind_draw = 0
            score = 0
            
            while (ind_bet <= len(bet)-1) and (ind_draw <= len(draw)-1):
                if bet[ind_bet] < draw[ind_draw]:
                    ind_bet += 1
                elif bet[ind_bet] > draw[ind_draw]:
                    ind_draw += 1
                else:
                    res.append(bet[ind_bet])
                    game_res.append(bet[ind_bet])
                    ind_bet += 1
                    ind_draw +=1
                    score += 1
            
            # print(game_res, score)
            
            if ("Game "+str(game_nbr) not in scratch_cards.keys()):
                scratch_cards["Game "+str(game_nbr)] = 1 
    
            for i in range(1,score+1):
                if "Game "+str(game_nbr+i) not in scratch_cards.keys():
                    scratch_cards["Game "+str(game_nbr+i)] = 1 
                
                scratch_cards["Game "+str(game_nbr+i)] += 1 * scratch_cards["Game "+str(game_nbr)]
                # print(scratch_cards)
                   
                    
        for value in scratch_cards.values():
            total_score += value
                
        # print("Total :",total_score)
        return total_score