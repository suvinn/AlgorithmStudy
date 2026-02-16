a, b, c, d, e, f = map(int, input().split())

'''
aex + bey = ce
bdx + bey = bf
(ae-bd)x = ce-bf
adx + bdy = cd
adx + aey = af
(bd-ae)y = cd-af
'''
x = (c*e - b*f) // (a*e - b*d)
y = (c*d - a*f) // (b*d - a*e)
print(x, y)