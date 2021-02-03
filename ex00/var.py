# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 13:47:12 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 14:45:12 by yonishi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = 42
print('%d is type of %s' % (num, type(num)))

s = '42'
print('%s is type of %s' % (s, type(s)))

str2 = 'quarante-deux'
print('%s is type of %s' % (str2, type(str2)))

fl = 42.0
print('%.1f is type of %s' % (fl, type(fl)))

lst = [42, 42]
print('%s is type of %s' % (lst, type(lst)))

dct = {42: 42}
print('%s is type of %s' % (dct, type(dct)))

tpl = (42, )
print('%s is type of %s' % (tpl, type(tpl)))

set = set()
print('%s is type of %s' % (set, type(set)))

