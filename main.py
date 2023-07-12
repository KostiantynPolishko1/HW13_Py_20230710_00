import os
import time

#======================functions======================#

def exit_menu():
    out_submenu = input("\texit -> ")
    if not out_submenu:
        time.sleep(0)
        os.system('CLS')
        return True

def print_menu(dict_menu, ind_pos: int=0) ->None:
    print("\n Menu:")
    for i in range(len(dict_menu)):
        if i == ind_pos:
            print("-> {} {}".format(str(i+1) + '.', dict_menu[i][0]))
            continue
        print("   {} {}".format(str(i+1) + '.', dict_menu[i][0]))

def receive_pos(ind_pos: int=0) ->tuple:
    min_ind, max_ind = 0, 5

    while True:
        direct = input(" ")

        # increment & decrement
        if not direct:
            return ind_pos, direct
        elif direct == 'W' or direct == 'w':
            ind_pos += 1
        elif direct == 'S' or direct == 's':
            ind_pos -= 1
        else:
            print("ERROR!")
            print(" \"w\" - Down, \"s\" - Up: ->", end='')
            continue

        # check position
        if ind_pos < min_ind:
            ind_pos = max_ind
        elif ind_pos > max_ind:
            ind_pos = min_ind

        return ind_pos, direct

#=====================menu functions==================#

def show_contacts(data: dict) ->None:
    while True:
        print("func1")
        if exit_menu():
            break
        time.sleep(0)
        os.system('CLS')

def add_contacts(data: dict) ->dict:
    print("func2")
    exit_menu()

def modify_contacts(data: dict) ->dict:
    print("func3")
    exit_menu()

def search_contacts(data: dict) ->None:
    print("func4")
    exit_menu()

def delete_contacts(data: dict) ->dict:
    print("func5")
    exit_menu()

def exit_function(data: dict) ->bool:
    return True

#========================main=========================#

ind_menu: int=0
strTxt: str = ''
#Data
contacts = {"Kostiantyn": {"mob": "+38-073-340-90-97", "home": "+38-056-790-53-45", "work": "+38-044-750-23-40"},
            "Margarita": ["+38-096-835-60-27", "+38-096-440-19-46"],
            "Dariya": "+38-066-645-98-81"
}

menu_f = {
    0: ["show",     show_contacts   ],
    1: ["add",      add_contacts    ],
    2: ["modify",   modify_contacts ],
    3: ["search",   search_contacts ],
    4: ["delete",   delete_contacts ],
    5: ["Exit",     exit_function   ]
}

print("\n\tContacts")
while True:
    print_menu(menu_f, ind_menu)
    print(" \"w\" - Down, \"s\" - Up: ->", end='')
    ind_menu, operation = receive_pos(ind_menu)
    time.sleep(0)
    os.system('CLS')

    if not operation:
        print("\n {} {}:".format(ind_menu + 1, menu_f[ind_menu][0])) if ind_menu < 5 else print("\tExit")
        tempValue = menu_f[ind_menu][1](contacts)
        if type(tempValue) == bool and tempValue:
            break
