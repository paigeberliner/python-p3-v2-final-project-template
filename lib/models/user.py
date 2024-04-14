# lib/models/user.py
from models.__init__ import CURSOR, CONN


class User:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User {self.id}: {self.username}, {self.email}>"

    @property
    def username(self):
        return self._username

    @name.setter
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
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists User instances """
        sql = """
            DROP TABLE IF EXISTS user;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the username and email values of the current User instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO user (username, email)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, username, email):
        """ Initialize a new User instance and save the object to the database """
        user = cls(username, email)
        user.save()
        return user

    def update(self):
        """Update the table row corresponding to the current User instance."""
        sql = """
            UPDATE user
            SET username = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.email, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM user
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        user = cls.all.get(row[0])
        if user:
            # ensure attributes match row values in case local instance was modified
            user.username = row[1]
            user.email = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            user = cls(row[1], row[2])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing a User object per row in the table"""
        sql = """
            SELECT *
            FROM user
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM user
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls, username):
        """Return a User object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM user
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def listings(self):
        """Return list of listings associated with current user"""
        from models.listings import Listing
        sql = """
            SELECT * FROM listings
            WHERE department_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Listing.instance_from_db(row) for row in rows
        ]
