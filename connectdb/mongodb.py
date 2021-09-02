import pymongo
import pandas as pd

class mongo:
    '''
    mongodb class through which we can perform most of the mongodb tasks using python

    '''

    def __init__(self):
        '''
        init function 
        '''
        self.db = ""

    def connect(self, connection_url,db):
        '''
        connect function to connect with mongo server
        
        Parameters
        ----------
        connection_url: connection url with password
        db:db name
        '''

        # Establish a connection with mongoDB
        self.client = pymongo.MongoClient(connection_url)
        # Create a DB
        self.db = self.client[db]



    def create_collection(self, COLLECTION_NAME):
        '''
        Function create_ table is used to create a new table

        Parameters
        ----------
        COLLECTION_NAME: collection name
        '''
        try:
            self.db[COLLECTION_NAME]
            print(f"{COLLECTION_NAME}  collection created")  
        except Exception as e:

            print(f"collectionqw not created error : {str(e)}")  

    def insert(self, collection_name,record):
        '''
        Function insert is used to insert value in table

        Parameters
        ----------
        record: data to be inserted as dict, to insert many data use list of dict
        '''
        try:
            if type(record)==dict:
                collection = self.db[collection_name]
                collection.insert_one(record)
            elif type(record)==list:
                collection = self.db[collection_name]
                collection.insert_many(record)
            print(f"inserted successfully")  
        except Exception as e:

            print(f"insert error : {str(e)}")  


    def update(self, collection_name,new_dict,where_dict):
        '''
        Function delete is used to delete record from collection

        Parameters
        ----------
        collection_name: collection name
        where_dict: condition as dict
        new_dict:new values
        '''
        try:

            collection = self.db[collection_name]

            collection.update_many(where_dict,{"$set":new_dict} )
            print(f"update successfully")  
        except Exception as e:
            print(f"update error : {str(e)}")  


    def delete(self, collection_name,where_dict):
        '''
        Function delete is used to delete record from collection

        Parameters
        ----------
        collection_name: collection name
        where_dict: condition as dict
        '''
        try:
            query_to_delete = where_dict
            collection = self.db[collection_name]

            collection.delete_one(query_to_delete)
            print(f"deleted successfully")  
        except Exception as e:
            print(f"delete error : {str(e)}")  


    def download(self,collection_name):

        # make an API call to the MongoDB server
        collection = self.db[collection_name]
        mongo_docs = collection.find()

        # Convert the mongo docs to a DataFrame
        docs = pd.DataFrame(mongo_docs)
        # Discard the Mongo ID for the documents
        docs.pop("_id")

        #df = pd.read_sql_query(f"SELECT * FROM {table_name}", self.conn())
        docs.to_csv(f"{collection_name}.csv",index=False)
        return f"{collection_name}.csv"

