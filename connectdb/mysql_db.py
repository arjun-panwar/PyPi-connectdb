import mysql.connector as connection #importing MYSQL connector

class sql:
    '''
    SQL class through with we can perform most of the SQL tasks using python
    
    Parameters
    ----------
    host: host URL of MySQL server
    user: user name
    passwd: password
    db: database name- default empty string ("")
    '''
 
    def __init__(self,host,user,passwd,db=""): 
        '''
        init function of sql class       
        '''
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
    def conn(self):
        '''
        Function conn is used to make connection to SQL server
        
        Parameters
        ----------

        '''
        try:
            if self.db=="":
                #connection without db
                return connection.connect(host=self.host,user=self.user,passwd=self.passwd)
            else:
               # connection with db
                return connection.connect(host=self.host,user=self.user, database=self.db,passwd=self.passwd)
        except Exception as e:
            return f"connection error : {str(e)}"
            
            
    def db_list(self):
        '''
        Function db_list is used to show databases list
        
        Parameters
        ----------
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            q="SHOW DATABASES" #qyery
            cursor.execute(q) #executing Query
            print(cursor.fetchall()) #printing result
            conn.close() #connection closed
            return "DB list displayed"
        except Exception as e:
            conn.close()#connection closed
            return f"db list error : {str(e)}"
    
    def create_db(self,db_name):
        '''
        Function create_ db is used to create a new database
        
        Parameters
        ----------
        db_name: database name
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            cursor.execute(f"create database {db_name}") #executing Query
            self.db=db_name #Initializing database name to class variable so that it can be used while making next connection with server
            conn.close()#connection closed
            return f"{db_name} DB created"
        except Exception as e:
            conn.close()#connection closed
            return f"db not created error : {str(e)}"
    
    def drop_db(self,db_name):
        '''
        Function drop_ db is used to drop a database
        
        Parameters
        ----------
        db_name: database name
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            cursor.execute(f"drop database {db_name}") #executing Query
            conn.close() #connection closed
            return f"{db_name} DB droped"
        except Exception as e:
            conn.close()#connection closed
            
            return f"db not Droped error : {str(e)}" 
            
    def create_table(self,table_name,columns):
        '''
        Function create_ table is used to create a new table
        
        Parameters
        ----------
        table_name: table name
        columns: columns names with data type and other discription in SQL format
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            cursor.execute(f"CREATE TABLE {table_name} ({columns})") #executing Query
            conn.close() #connection closed
            return f"{table_name} table created with columns: {columns}"
        except Exception as e:
            conn.close() #connection closed
            
            return f"table not created error : {str(e)}"
            
            
    def insert(self,table_name,data):
        '''
        Function insert is used to insert value in table
        
        Parameters
        ----------
        table_name: table name
        data: values to be inserted
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            
            cursor.execute(f"INSERT INTO {table_name} VALUES ({data})") #executing Query
            conn.commit() #commiting the query
            conn.close() #connection closed
        except Exception as e:
            conn.close() #connection closed
            return f"insert error : {str(e)}"
            
            
    
    def select_db(self,db_name):
        '''
        Function select_db is used to select a database
        
        Parameters
        ----------
        db_name: database name
        '''
        self.db=db_name #Initializing database name to class variable so that it can be used while making next connection with server
        

    
    def columns(self,t_name):
        '''
        Function columns is used to print columns names
        
        Parameters
        ----------
        t_name: table name
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{t_name}' ") #executing Query
            for result in cursor.fetchall(): #printing result 
                print(result[3],end=",")
            conn.close() #connection closed
             
        except Exception as e:
            conn.close() #connection closed
            return f"columns name not displayed : {str(e)} "  
  

    def query(self,query):
        '''
        Function query is used to run a SQL query 
        
        Parameters
        ----------
        query: SQL query
        '''
        try:
            conn=self.conn() #making connection
            cursor = conn.cursor() #create a cursor to execute queries
            cursor.execute(query) #executing Query
            for result in cursor.fetchall(): #printing result line by line
                print(result)
                

            conn.close() #connection closed
            return "info", f"Query is performed : {query} " 
        except Exception as e:
            conn.close() #connection closed
            return f"Query not performed : {query} : {str(e)}"  
     

    

