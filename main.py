import os
import pickle

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

def receive_pos(ind_pos: int, max_ind: int) ->tuple:
    min_ind = 0

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

    return ''

def mob_num_print(name_del: str, contacts: dict, ind_pos: int) ->None:
    print(name_del, ":")
    for i in range(len(contacts[name_del])):
        if i == ind_pos:
            print("->\t", contacts[name_del][i])
            continue
        print("\t", contacts[name_del][i])

def mob_num_ind(name_del: str, contacts: dict) ->int:
    ind = 0
    while True:
        mob_num_print(name_del, contacts, ind)
        print(" \"w\" - Down, \"s\" - Up: ->", end='')
        ind, action = receive_pos(ind, len(contacts[name_del])-1)
        os.system('CLS')

        if not action:
            return ind

def mob_num_new(contacts: dict, name_modify: str) ->bool:

    if type(contacts[name_modify]) == list:
        while len(contacts[name_modify]):
            mobile_ind = mob_num_ind(name_modify, contacts)

            mob_num = input("\tnew mobile -> ")
            if check_mob(mob_num):
                continue
            contacts[name_modify][mobile_ind] = mob_num

            if not input("\n\tcontinue -> "):
                os.system('CLS')
                continue
            return True
    else:
        while True:
            mob_num = input("\tnew mobile -> ")
            if check_mob(mob_num):
                continue
            contacts[name_modify] = mob_num
            return True
def file_readb(file_name: str) ->dict:
    data_str: str
    data_dict: dict

    try:
        with open((file_name + '.txt'), 'rb') as file:
            data_str = pickle.load(file)
    except FileNotFoundError:
        print("ERROR! FILE ABSENT")
    except Exception as FileNotWorkError:
        print("ERROR! ABORD FILE READ")

    data_dict = eval(data_str)
    return data_dict

def file_writeb(file_name: str, data_dict: dict) ->None:
    with open((file_name + '.txt'), 'wb') as file:
        try:
            pickle.dump(str(data_dict), file)
        except Exception as FileNotWorkError:
            print("ERROR! ABORD FILE RECORD")

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
        print(" add contact:")
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

def modify_contacts(contacts: dict) ->None:

    while True:
        print(" modify contact:")
        name_search = search_name((input("\tname -> ")).lower(), contacts)

        if not name_search:
            print("\t is absent")
        else:
            if type(contacts[name_search]) == list:
                print(name_search, ":")
                for ph in contacts[name_search]:
                    print("\t\t phone {}".format(ph))
            else:
                print("name {} : phone {}".format(name_search, contacts[name_search]))

            name_modify = input("\n\tnew name -> ")
            contacts[name_modify] = contacts.pop(name_search)  # new key

            if mob_num_new(contacts, name_modify):
                break

        if not input("\n\tcontinue -> "):
            os.system('CLS')
            continue

        break

def search_contacts(contacts: dict) ->None:
    while True:
        print(" search contact:")
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
        print(" delete contact:")
        name_del = search_name((input("\tname -> ")).lower(), contacts)

        if not name_del:
            print("\t\tis absent!")
        else:
            if type(contacts[name_del]) == list:
                while len(contacts[name_del]):
                    del contacts[name_del][mob_num_ind(name_del, contacts)]
                    print("mobile delete:")
                    if not input("\n\tcontinue -> "):
                        os.system('CLS')
                        continue
                    break
            else:
                del contacts[name_del]

        if not input("\n\tcontinue -> "):
            os.system('CLS')
            continue
        os.system('CLS')
        break

def exit_function(contacts: dict) ->bool:
    return True

#========================main=========================#

if __name__ == '__main__':
    ind_menu: int = 0
    strTxt: str = ''
    f_name = 'contacts'
    data: dict

    data = file_readb(f_name)

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
        ind_menu, operation = receive_pos(ind_menu, len(menu_f)-1)
        os.system('CLS')

        if not operation:
            print("\n {} {}:".format(ind_menu + 1, menu_f[ind_menu][0])) if ind_menu < 5 else print("\tExit")
            tempValue = menu_f[ind_menu][1](data)
            if type(tempValue) == bool and tempValue:
                break

    file_writeb(f_name, data)

else:
    print('ERROR!\nApplication is not loaded!')
