# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 13:47:12 by yonishi           #+#    #+#              #
#    Updated: 2021/02/05 22:34:56 by yonishi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def my_var(num, str1, str2, fl, b, lst, dct, tpl, setdata):
    print('%d is type of %s' % (num, type(num)))
    print('%s is type of %s' % (str1, type(str1)))
    print('%s is type of %s' % (str2, type(str2)))
    print('%.1f is type of %s' % (fl, type(fl)))
    print('%s is type of %s' % (b, type(b)))
    print('%s is type of %s' % (lst, type(lst)))
    print('%s is type of %s' % (dct, type(dct)))
    print('%s is type of %s' % (tpl, type(tpl)))
    print('%s is type of %s' % (setdata, type(setdata)))

my_var(42, '42', 'quarante-deux', 42.0, True, [42, 42], {42: 42}, (42, ), set())
