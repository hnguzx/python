from sys import argv
script,user_name,promt = argv
#promt = '>'
print("Hi %s I'm the %s script." % (user_name,script))
print("I'd like to ask you a few questions")
print("Do you like me %s?" % user_name)
likes = input(promt)

print("Where do you live %s" % user_name)
lives = input(promt)

print("what kind of computer do you have")
computer = input(promt)

print("""
Alright ,so you said %r about likeing me
you live %r ,not sure where that is 
and you hava a %r computer ,Nice
"""
%
(likes,lives,computer)
)