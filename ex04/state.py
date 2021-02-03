# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 16:46:13 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 16:51:10 by yonishi          ###   ########.fr        #
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

if sys.argv[1] in r_states:
    print(r_states[sys.argv[1]])
else:
    print('Unknown capital city')
