# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 15:28:42 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 15:46:36 by yonishi          ###   ########.fr        #
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

if sys.argv[1] in states:
    print(states[sys.argv[1]])
else:
    print('Unknown state')
