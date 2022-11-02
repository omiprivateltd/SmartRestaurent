import sqlite3
from tabnanny import check


def get_file_bytes(file_name:str):
    """Function Used to return byte data of a file"""
    with open("./images/"+file_name,'rb') as file:
        return file.read()
        
class Database:
    def __init__(self,db_name):
        self.db_name = db_name
        self.conn =  sqlite3.connect(db_name,check_same_thread=False)


    def connect_db(self,db_name):
        """Function Used To Connect With Database"""
        self.conn=  sqlite3.connect(db_name)

    def get_menu(self):
        """Function Used to Get All Item's of a MENU"""
        output = list(self.execute_command('''SELECT * FROM MENU'''))
        print(output)
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
        return self.execute_command(f'''INSERT INTO MENU (ITEMNAME,ITEMDESC,ITEMPRICE,ITEMIMAGE) VALUES ('{item_name}', '{item_desc}', '{item_price}', '{item_image}')''')
    


        
        
if __name__=="__main__":
    database = Database('test.db')
    output = database.execute_command("""DELETE FROM MENU WHERE ITEMNAME='Test Shot 2';""")
    print("output",list(output))
    for k in output:
        print(k)
    # for k in database.get_menu():
    #     print("k",k)

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
    # print('output',database.insert_item('Aloochalo','made of aloo',100,"randomimagetextfromjavascript"))
    # # output = db.execute_command('''INSERT INTO ORDERBOOK (NAME,MOVNAME,PRICE,SEATS) \
    # #   VALUES ('shubham', 32, 'California', 20000.00 )''')

