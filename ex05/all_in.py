# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 16:52:26 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 17:17:44 by yonishi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }

if len(sys.argv) != 2:
    sys.exit()

for key in states.keys():
    states[key] = capital_cities[states[key]]

r_states = {}
for key, value in states.items():
   r_states[value] = key

for txt in sys.argv[1].split(','):
    found = False

    txt = txt.strip(' ')
    if txt == '':
        continue

    for key in states.keys():
        if txt.lower() == key.lower():
            print(states[key], 'is the capital of', key)
            found = True
    for key in r_states.keys():
        if txt.lower() == key.lower():
            print(key, 'is the capital of', r_states[key])
            found = True
    if found == False:
        print(txt, 'is neither a capital city nor a state')

