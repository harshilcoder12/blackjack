import random
usr_lst = []
comp_lst = []
def cards():
    card = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    usr_c1 = random.choice(card)
    usr_c2 = random.choice(card)
    usr_lst.append(usr_c1)
    usr_lst.append(usr_c2)
    comp_c1 = random.choice(card)
    comp_c2 = random.choice(card)
    comp_lst.append(comp_c1)
    comp_lst.append(comp_c2)

def after_card():
    card = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    usr_c = random.choice(card)
    usr_lst.append(usr_c)

def after_comp_card():
    card = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    comp_c = random.choice(card)
    comp_lst.append(comp_c)
def check():
    if 11 in usr_lst:
        usr_lst.remove(11)
        usr_lst.append(1)
    elif 11 in comp_lst:
        comp_lst.remove(11)
        comp_lst.append(1)

def compare_reveal():
    print('your cards: ',usr_lst)
    print("compter's first card: ",comp_lst[0])
    is_game_over = False
    while is_game_over == False:
        ask_usr = input('do you want to hit or pass: ')
        if ask_usr == 'hit':
            after_card()
            after_comp_card()
            sum_usr = sum(usr_lst)
            sum_comp = sum(comp_lst)
            if sum_usr > 21 and sum_comp>21:
                print('you loose')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
                is_game_over = True
            elif sum_usr == 21 and sum_comp < 21:
                print('you win')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
                is_game_over = True
            elif sum_usr == sum_comp:
                print('its a draw')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
            elif sum_usr < 21 and sum_comp <21:
                is_game_over = False
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
            elif sum_usr < 21 and sum_comp > 21:
                print('you win')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
                is_game_over = True 
        elif ask_usr =='pass':
            after_comp_card()
            print('your cards', usr_lst)
            print("computer's cards ",comp_lst)
            sum_usr = sum(usr_lst)
            sum_comp = sum(comp_lst)
            if sum_usr > 21 and sum_comp>21:
                print('you loose')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
                is_game_over = True  
            elif sum_usr == 21 and sum_comp < 21:
                print('you win')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
                is_game_over = True
            elif sum_usr == sum_comp:
                print('its a draw')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
            elif sum_usr < 21 and sum_comp <21:
                is_game_over = False
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
            elif sum_usr < 21 and sum_comp > 21:
                print('you win')
                print('your cards ',usr_lst)
                print('computer cards',comp_lst)
                is_game_over = True  
cards()
check()
compare_reveal()
