# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dict.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 15:10:09 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 15:25:46 by yonishi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

data = [['Caleb' , 24],
        ['Calixte' , 84],
        ['Calliste', 65],
        ['Calvin' , 12],
        ['Cameron' , 54],
        ['Camil' , 32],
        ['Camille' , 5],
        ['Can' , 52],
        ['Caner' , 56],
        ['Cantin' , 4],
        ['Carl' , 1],
        ['Carlito' , 23],
        ['Carlo' , 19],
        ['Carlos' , 26],
        ['Carter' , 54],
        ['Casey' , 2]]

d = {}
for value, key in data:
    d[key] = value

for key in d.keys():
    if len(str(key)) == 1:
        print(' ', end='')
    print(key, ':', d[key])
