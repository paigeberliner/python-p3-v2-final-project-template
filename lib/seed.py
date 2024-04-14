#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.user import User
from models.listing import Listing

def seed_database():
    Listing.drop_table()
    User.drop_table()
    User.create_table()
    Listing.create_table()

    # Create seed data
    PaigeBerliner = User.create("PaigeBerliner", "Paigeberliner@gmail.com")
    GrantBerliner = User.create("GrantBerliner", "GrantBerliner@gmail.com")
    #Listing.create("Listing 2", "20.00", PaigeBerliner.id)
    #Listing.create("Listing 1", "15.00", GrantBerliner.id)
    #Listing.create("Listing 2", "5.00", GrantBerliner.id)
    #Listing.create("Listing 3", "25.00", GrantBerliner.id)


seed_database()
print("Seeded database")
