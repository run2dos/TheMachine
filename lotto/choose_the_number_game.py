#choose_the_number_game.py

target_number = [5,2,7,4,6]
number = [0,0,0,0,0]
inc_dict = {'0':[],
            '1':[],
            '2':[],
            '3':[],
            '4':[]}

for idx,n in enumerate(target_number):
    while target_number[idx] > number[idx]:
        print(target_number)
        print(number)
        print('target[{0}] != number[{0}]'.format(idx))
        usr_input = input('>')
        number[idx] += int(usr_input)
        inc_dict[str(idx)].append(int(usr_input))
    print('target[{0}] == number[{0}]'.format(idx)) 
print('target == number')

for idx,x in enumerate(range(5)):
    print('idx[{0}] was incremented by'.format(idx),inc_dict[str(x)])

new_target = [1,1,1,1,1]
print('before', new_target)

for idx, x in enumerate(new_target):
    for y in inc_dict[str(idx)]:
        new_target[idx] += y

print('after', new_target)