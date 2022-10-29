import sqlite3

class Database:
    def __init__(self,db_name):
        self.db_name = db_name
        self.conn =  sqlite3.connect(db_name)


    def connect_db(self,db_name):
        """Function Used To Connect With Database"""
        self.conn=  sqlite3.connect(db_name)

    def get_menu(self):
        """Function Used to Get All Item's of a MENU"""
        output = db.execute_command('''SELECT * FROM MENU''')
        return output

    def execute_command(self,command):
        """Function Used To Execute Any Database Query
        ARGS: COMMAND:str
        RETURN : CURSOR:tuple"""
        if not self.conn:
            return "Please Connect With Database First Use Method connect_db"
        output = self.conn.execute(command)
        self.conn.commit()
        return output
    def insert_item(self,item_name:str,item_desc:str,item_price:int,item_image:str):
        """Function Used To Insert item Data In Database"""
        return db.execute_command(f'''INSERT INTO MENU (ITEMNAME,ITEMDESC,ITEMPRICE,ITEMIMAGE) VALUES ('{item_name}', '{item_desc}', '{item_price}', '{item_image}')''')

        
        
if __name__=="__main__":
    db = Database('test.db')
    # uncomment if you have not created the table
    # try:
    #     db.execute_command('''CREATE TABLE MENU
    #         (ID INT AUTO_INCREMENT ,
    #         ITEMNAME           TEXT    NOT NULL,
    #         ITEMDESC            CHAR(50)     NOT NULL,
    #         ITEMPRICE        INT,
    #         ITEMIMAGE        TEXT NOT NULL);''')
    # except Exception as Error:
    #     print("Exception Handled",Error)
    # print('output',db.insert_item('Aloo Paratha','made of aloo',100,"randomimagetextfromjavascript"))
    # # output = db.execute_command('''INSERT INTO ORDERBOOK (NAME,MOVNAME,PRICE,SEATS) \
    # #   VALUES ('shubham', 32, 'California', 20000.00 )''')
    output = db.execute_command('''SELECT * FROM MENU''')
    for k in output:
        print(k)

