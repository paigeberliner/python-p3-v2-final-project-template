
from .__init__ import db_connection, db_cursor
from models.user import User

class Listing: 
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, title, price, state, user_id, id=None):
        self.id = id
        self.title = title
        self.price = price
        self.state = state
        self.user_id = user_id

    def __repr__(self):
        return (
            f"<Listing {self.id}: {self.title}, {self.price}, {self.state} " +
            f"User ID: {self.user_id}>"
        )
    #
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Title must be a non-empty string"
            )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        try:
            self._price = int(price)
        except ValueError:
            raise ValueError("Price must be an integer")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        try:
            self._state = str(state)
        except ValueError:
            raise ValueError("State must be a string")
        
    @property
    def user_id(self):
        return self._user_id

    def user_id(self, user_id):
        try:
            user_id = int(user_id)  # Convert to integer
        except ValueError:
            raise ValueError("User_id must be an integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE "listings" ( "id" INTEGER, "title" TEXT, "price" INTEGER, "state" TEXT, "user_id" INTEGER, PRIMARY KEY("id"), FOREIGN KEY("user_id") REFERENCES "users"("id") )
        """
        db_cursor.execute(sql)  
        db_connection.commit()


    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Listing instances """
        sql = """
            DROP TABLE IF EXISTS listings;
        """
        db_cursor.execute(sql)  
        db_connection.commit()

    def save(self):
        """ Save the object to the database """
        sql = """
            INSERT INTO listings (title, price, state, user_id)
            VALUES (?, ?, ?, ?)
        """
        db_cursor.execute(sql, (self.title, self.price, self.state, self.user_id))
        db_connection.commit()

        self.id = db_cursor.lastrowid

        self.id = db_cursor.lastrowid
        type(self).all[self.id] = self


    def delete(self, user_password):
    # First, check if the provided user password matches the password stored in the database
        user = User.find_by_password(user_password)
        if user:
        # If the user exists and the password is correct, proceed with deletion
            sql = """
                DELETE FROM listings
                WHERE id = ?
            """
            db_cursor.execute(sql, (self.id,))
            db_connection.commit()

        # Delete the dictionary entry using id as the key
            del type(self).all[self.id]

        # Set the id to None
            self.id = None
            print("Listing deleted successfully.")
        else:
            print("User authentication failed. Listing not deleted.")

    @classmethod
    def create(cls, user, title, price, state, user_id):
        """ a new Listing instance and save the to the database """
        listing = cls(title, price, state, user_id)
        listing.save()
        return listing
    

    @classmethod
    def instance_from_db(cls, row):
        """Return a Listing object having the attribute values from the table row."""
        if row:
        # Check the dictionary for  existing instance using the row's primary key
            listing = cls.all.get(row[0])
            if listing:
            # ensure attributes match row values in case local instance was modified
                listing.title = row[1]
                listing.price = row[2]
                listing.user_id = row[3]
                listing.state = row[4]
    
            else:
            # not in dictionary, create new instance and add to dictionary
                listing = cls(row[1], row[2], row[3], row[4])
                listing.id = row[0]
                cls.all[listing.id] = listing
            return listing
        else:
            return None


    @classmethod
    def get_all(cls):
        """Return a list containing one Listing object per table row"""
        sql = """
            SELECT *
            FROM listings
        """

        rows = db_cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id_):
        """Return Listing object corresponding to the table row matching the ID."""
        sql = """
        SELECT *
        FROM listings
        WHERE id = ?
        """

        row = db_cursor.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_state(cls, state):
        """Return Listing object corresponding to the table row matching the state"""
        sql = """
        SELECT *
        FROM listings
        WHERE state = ?
        """

        row = db_cursor.execute(sql, (state,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return Listing object corresponding to first table row matching specified title"""
        sql = """
            SELECT *
            FROM listings
            WHERE title is ?
        """

        row = db_cursor.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
