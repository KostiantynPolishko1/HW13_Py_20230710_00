import os

#======================functions======================#

def exit_menu():
    out_submenu = input("\texit -> ")
    if not out_submenu:
        os.system('CLS')
        return True

def print_menu(dict_menu, ind_pos: int=0) ->None:
    print("\n\tContacts\n Menu:")
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

def check_mob(mobile: str) ->bool:

    if not mobile[0].isdigit() and mobile[0] != '+':
        print("\n\tERROR!\n\tenter mob +...digit or 000...digit\n")
        return True

    ind = 1
    while ind < len(mobile):
        if not mobile[ind].isdigit() and mobile[ind] != '-':
            print("\n\tERROR!\n\tenter mob in digit num\n")
            return True
        ind += 1

    return False

def search_name(name_search: str, contacts: dict) -> str:
    for name in contacts:
        name_temp = name.lower()
        if name_temp.find(name_search) != -1:
            return name
        else:
            return ''

#=====================menu main functions==================#

def show_contacts(contacts: dict) ->None:
    print("\tList", end='')
    if not len(contacts):
        print(" is empty", contacts)
    else:
        print(": ")
        for name in sorted(contacts):
            if type(contacts[name]) == dict:
                print(name, ":")
                for ph in contacts[name]:
                    print("\t\t", ph, " -> ", contacts[name][ph])
            elif type(contacts[name]) == list:
                ind = 0
                print(name, ":")
                for ph in contacts[name]:
                    ind += 1
                    print("\t\t phone {} -> {}".format(ind, ph))
            else:
                print(name, " : ", contacts[name])
    exit_menu()

def add_contacts(contacts: dict) ->None:
    while True:
        print(" contact:")
        arr_ph_num = []
        name_add = input("\tenter name -> ")

        while True:  # check if number in digit format
            mob_num = input("\tenter mob.num\t-> ")

            if check_mob(mob_num):
                continue

            arr_ph_num.append(mob_num)
            if not input("+mob? -> "):
                continue

            contacts[name_add] = arr_ph_num
            os.system('CLS')
            break

        if not input("+name? -> "):
            os.system('CLS')
            continue
        break

    os.system('CLS')

def modify_contacts(contacts: dict) ->dict:
    print("func3")
    exit_menu()

def search_contacts(contacts: dict) ->None:
    while True:
        print(" contact:")
        name_search = search_name((input("\tname -> ")).lower(), contacts)

        if not name_search:
            print("\t\"{}\" is absent")
        else:
            if type(contacts[name_search]) == dict:
                print(name_search, ":")
                for ph in contacts[name_search]:
                    print("\t", ph, "\t", contacts[name_search][ph])
            elif type(contacts[name_search]) == list:
                print(name_search, ":")
                for ph in contacts[name_search]:
                    print("\t", ph)
            else:
                print("{} : {}".format(name_search, contacts[name_search]))

        if not input("\n\tcontinue -> "):
            os.system('CLS')
            continue
        break

    os.system('CLS')

def delete_contacts(contacts: dict) ->None:
    while True:
        print(" contact:")
        name_del = search_name((input("\tname -> ")).lower(), contacts)

        if not name_del:
            print("\t\tis absent!")
        else:
            if type(contacts[name_del]) == dict:
                print(name_del, ":")
                for ph in contacts[name_del]:
                    print("\t", ph, "\t", contacts[name_del][ph])
                while True:
                    ph_type = input("enter type phone -> ")
                    if contacts[name_del].get(ph_type, False):
                        print("DELETE! ->", end='')
                        print(ph_type, " : ", contacts[name_del][ph_type])
                        del contacts[name_del][ph_type]
                        break
                    else:
                        print("enter correct type as:")
                        for i in contacts[name_del]:
                            print("\t\t\t", i)
                        continue
            elif type(contacts[name_del]) == list:
                ph_pos: int = 0
                print(name_del, ":")
                for ind in contacts[name_del]:
                    ph_pos += 1
                    print("\t\t", ph_pos, " -> ", ind)
                while True:
                    ph_num = int(input("enter phone Pos. delete -> "))
                    if ph_num > ph_pos:
                        print("\nN phone is out of range")
                        continue
                    print("DELETE! -> phone {}: {}".format(ph_num, contacts[name_del][ph_num - 1]))
                    del contacts[name_del][ph_num - 1]
                    break
            else:
                del contacts[name_del]

        if not input("\n\tcontinue -> "):
            os.system('CLS')
            continue
        break

def exit_function(contacts: dict) ->bool:
    return True

#========================main=========================#

ind_menu: int=0
strTxt: str = ''
#Data
data = {"Kostiantyn": {"mob": "+38-073-340-90-97", "home": "+38-056-790-53-45", "work": "+38-044-750-23-40"},
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

while True:
    print_menu(menu_f, ind_menu)
    print(" \"w\" - Down, \"s\" - Up: ->", end='')
    ind_menu, operation = receive_pos(ind_menu)
    os.system('CLS')

    if not operation:
        print("\n {} {}:".format(ind_menu + 1, menu_f[ind_menu][0])) if ind_menu < 5 else print("\tExit")
        tempValue = menu_f[ind_menu][1](data)
        if type(tempValue) == bool and tempValue:
            break
