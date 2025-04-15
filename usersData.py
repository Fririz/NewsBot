import sqlite3

class usrDataEdit:
        
    def checkIDInDataBase(self, ID:int) -> bool:
        """
        Якщо користувач є в базі вертає False, Якщо нема то True
        """
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM users WHERE id = ?", (ID,))
            result = cursor.fetchone()
            if result is None:
                return True
            return False
        
    def addUsersToDataBase(self, ID:int, name:str) -> None:
        """
        Додає користувача в базу данних
        """
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (ID, name))
            conn.commit()