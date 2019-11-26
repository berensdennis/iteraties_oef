#met while
from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
i = 1
while i <= 10:
    print( i, "*", num, "=", i*num )
    i += 1
#met for
from pcinput import getInteger

num = getInteger( "Geef een nummer: " )
for i in range( 1, 11 ):
    print( i, "*", num, "=", i*num )
