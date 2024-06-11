from models.__init__ import CURSOR, CONN

class Doctor:
    all = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int) and len(id) > 0:
            self._id = id
        else:
            raise ValueError("Enter available docor id")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Enter available doctor name")

    @classmethod
    def get_all(cls):
        sql = """ 
        SELECT * FROM doctors
        """

        row = CURSOR.execute(sql).fetchall()
        return cls(row['id'], row['name']) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """ 
        SELECT * FROM doctors
        WHERE id is ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(row['id'], row['name']) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """ 
        SELECT * FROM doctors
        WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls(row['id'], row['name']) if row else None
        
    def save(self):
        sql = """ 
        INSERT INTO doctors(id, name)
        VALUES (?, ?)"""
        
        CURSOR.execute(sql, (self.id, self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid

