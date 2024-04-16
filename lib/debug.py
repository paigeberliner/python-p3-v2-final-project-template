#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import db_connection, db_cursor
from models.user import User
from models.listing import Listing

import ipdb

def reset_database(): 
    User.drop_table()
    User.create_table()
    Listing.drop_table()
    Listing.create_table()
    

#paige = User("PaigeBerliner", "paigeberliner@gmail.com")
#print(paige)

#paige.save()
#print(paige)

Listing1 = Listing("Listing1", 10.00, 1)
print(Listing1)

ipdb.set_trace() #Once code runs and hits this line code freezes to test 
