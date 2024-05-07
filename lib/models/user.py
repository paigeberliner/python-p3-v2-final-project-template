# lib/models/user.py
    # Defines a class called 'User' representing user objects
    # The script includes mthods to interact with a database (i.e. creating tables)
    # Saving user instances to the database and retrieving user data from the database 


from .__init__ import db_connection, db_cursor #connection to the database 


class User: # defines a class with attributes (username, email, and id)

    all = {}

    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password 

    #def __repr__(self):
        #return f"<User {self.id}: {self.username}, {self.email}, {self.password}>"
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username):
            self._username = username
        else:
            raise ValueError(
                "Username must be a non-empty string"
            )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email):
            self._email = email
        else:
            raise ValueError(
                "Email must be a non-empty string"
            )


    @classmethod
    def create_table(cls): # class method creates a table if it doesn't exist
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            password TEXT)
        """
        db_cursor.execute(sql)  
        db_connection.commit()

    @classmethod
    def drop_table(cls): # class method drops the tabl for the database if it exists 
        sql = """
            DROP TABLE IF EXISTS users;
        """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self): # saves the current user object to the database by inserting a new row into the table with the attributes
        sql = """
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?) 
        """
        db_cursor.execute(sql, (self.username, self.email, self.password))
        db_connection.commit()

        self.id = db_cursor.lastrowid
        type(self).all[self.id] = self
 

    @classmethod
    def create(cls, username, email, password): #creates a user by inputting a username and email, saving, and returning the new user object 
        """ Initialize a new User instance and save the object to the database """
        user = cls(username, email, password)
        user.save() #insertion of data being handled by save method 
        return user
        

    @classmethod
    def instance_from_db(cls, row): #creates a user object from a database row 
    
        user = cls.all.get(row[0]) #attempts to retrieve a user from the all dictionary attribute of the class
        if user:
            user.username = row[1]
            user.email = row[2]
            user.password = row[3]
        else:
            user = cls(row[1], row[2], row[3])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls): #retrieves all user objects from the 'users' table and converts each row into an object using the instance_from_db()
        sql = """
            SELECT *
            FROM users
        """

        rows = db_cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id): #retrieves a user object based on the id 
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = db_cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_password(cls, password): 
        sql = """
            SELECT *
            FROM users
            WHERE password = ?
        """
        row = db_cursor.execute(sql, (password,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls, username): #retrieves a user object based on the username 
        """Return a User object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM users
            WHERE username is ?
        """

        row = db_cursor.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def listings(self): #retrieves all listings associated with the current user object where the user table id matches the listings table user_id
        from models.listing import Listing
        sql = """
            SELECT * FROM listings
            WHERE user_id = ?
        """
        db_cursor.execute(sql, (self.id,),)

        rows = db_cursor.fetchall()
        return [
            Listing.instance_from_db(row) for row in rows
        ]

