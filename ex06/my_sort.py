# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 17:19:41 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 17:41:25 by yonishi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

d = {
        'Hendrix':'1942',
        'Allman':'1946',
        'King':'1925',
        'Clapton':'1945',
        'Johnson':'1911',
        'Berry':'1926',
        'Vaughan':'1954',
        'Cooder':'1947',
        'Page':'1944',
        'Richards':'1943',
        'Hammett':'1962',
        'Cobain':'1967',
        'Garcia':'1942',
        'Beck':'1944',
        'Santana':'1947',
        'Ramone':'1948',
        'White':'1975',
        'Frusciante':'1970',
        'Thompson':'1949',
        'Burton':'1939',
        }

d_sortedbyname = dict(sorted(d.items(), key=lambda x: x[0]))
d_sortedbyyear = dict(sorted(d_sortedbyname.items(), key=lambda x: x[1]))

for name in d_sortedbyyear.keys():
    print(name)
