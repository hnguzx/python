'''
Created on 2020年1月7日

@author: Administrator
'''
formatter = "%r %r %r %r"

print (formatter % (1,2,3,4)) 
print (formatter % ("one","two","three","don't")) 

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")