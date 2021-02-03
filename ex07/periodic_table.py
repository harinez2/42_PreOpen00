# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yonishi <yonishi@student.42tokyo.j>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/03 17:52:15 by yonishi           #+#    #+#              #
#    Updated: 2021/02/03 20:39:23 by yonishi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import ast

html_head = """\
<!doctype html>

<html lang="en">
    <head>
    <meta charset="utf-8">

    <title>The HTML5 Herald</title>
    <meta name="description" content="The HTML5 Herald">
    <meta name="author" content="SitePoint">

    <link rel="stylesheet" href="css/styles.css?v=1.0">

    <!--[if lt IE 9]>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
    <![endif]-->
    </head>

    <body>
        <script src="js/scripts.js"></script>
"""

html_tail = """\
    </body>
</html>
"""

d = {}
f = open('periodic_table.txt', 'r')
lines = f.readlines()
for line in lines:
    name = line.split('=')[0].strip()
    p = line.split('=')[1]
    num = p.split(',')[1].split(':')[1].strip()
    position = p.split(',')[0].split(':')[1].strip()
    short = p.split(',')[2].split(':')[1].strip()
    mol = p.split(',')[3].split(':')[1].strip()
    electron = p.split(',')[4].split(':')[1].strip()
    d[num] = { 'name': name, 'position': position, 'short': short, 'mol': mol, 'electron': electron }
f.close()

data = '<table>\n' 
idx = 1
for i in range(7):
    data += '  <tr>\n'
    for j in range(18):
        if int(d[str(idx)]['position']) == j:
            data += '    <td>' + str(idx) + '<br>' \
                    + d[str(idx)]['name'] + '<br>' \
                    + d[str(idx)]['short'] + '<br>' \
                    + d[str(idx)]['mol'] + '<br>' \
                    + d[str(idx)]['electron'] + '<br>' \
                    + '</td>\n'
            if idx == 56:
                idx = 72
            elif idx == 88:
                idx = 104
            else:
                idx += 1
        else:
            data += '    <td></td>\n'
    data += '  </tr>\n'
data += '</table>\n'
#print(data)

f = open('periodic_table.html', 'w')
f.write(html_head)
f.write(data)
f.write(html_tail)
f.close()

