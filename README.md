
# ConnectDB

Connect python with Mysql, MongoDB, Cassandra database

### Installation
Run below commandto install this package

```pip install connectdb```

## Mysql

#### prerequisite
mysql-connector-pythonmust be installed
To install it, run below command

```pip install mysql-connector-python```

### Connect with Mysql using python

#### import
```from connectdb import mysql_db```
#### connect
```ob=mysql_db.sql("host","user","password")```

#### Check database List
Function db_list is used to show databases list
```ob.db_list```
#### Create Database
 Function create_ db is used to create a new database
        
        Parameters
        ----------
        db_name: database name
```ob.create_db(Data_base_name)```

#### Drop Database
 Function drop_ db is used to drop a database
        
        Parameters
        ----------
        db_name: database name
```ob.drop_db(Data_base_name)```

#### Create table
Function create_ table is used to create a new table
        
        Parameters
        ----------
        table_name: table name
        columns: columns names with data type and other discription in SQL format
        example-columns="CI_n INT(2),CI_m INT(2),IAC_u VARCHAR(10),IAC_v VARCHAR(10),IAC_w VARCHAR(10),CAC_u VARCHAR(10),CAC_v VARCHAR(10),CAC_w VARCHAR(10)"

```ob.create_table(table_name,columns)```

#### Insert into Table
Function insert is used to insert value in table
        
        Parameters
        ----------
        table_name: table name
        data: values to be inserted in order
```ob.insert(table_name,data)```

#### columns
Function columns is used to print columns names
        
        Parameters
        ----------
        t_name: table name
```ob.columns(t_name)```

#### Select DataBase
Function select_db is used to select a database
        
        Parameters
        ----------
        db_name: database name
```ob.select_db(db_name)```

#### Query
Function query is used to run a SQL query 
        
        Parameters
        ----------
        query: SQL query
```ob.query(query)```


## MongoDB

#### prerequisite
pymongo and pandas must be installed
To install pymongo, run below command

```pip install pymongo```
To install pandas, run below command

```pip install pandas```

### Connect with MongoDB using python

#### import
```from connectdb import mongodb```

#### connect
```ob=mongodb.mongo()```

```ob.connect(Connection URL, Database Name)```

#### Create Collection
Function create_ table is used to create a new table

        Parameters
        ----------
        COLLECTION_NAME: collection name
```ob.create_collection(COLLECTION_NAME)```

#### Insert
Function insert is used to insert value in table

        Parameters
        ----------
        record: data to be inserted as dict, to insert many data use list of dict
```ob.insert(collection_name,record)```

#### Update
Function delete is used to delete record from collection

        Parameters
        ----------
        collection_name: collection name
        where_dict: condition as dict
        new_dict:new values
```ob.update(collection_name,new_dict,where_dict)```

#### Delete
Function delete is used to delete record from collection

        Parameters
        ----------
        collection_name: collection name
        where_dict: condition as dict
```ob.delete(self, collection_name,where_dict)```

#### Download
Function To download whole collection
        Parameters
        ----------
        collection_name: collection name
        
```ob.download(collection_name)```


## Cassandra

#### prerequisite
cassandra-driver must be installed
To install cassandra-driver, run below command

```pip install cassandra-driver```


### Connect with Cassandra using python

#### import
```from connectdb import cassandra_db```

#### connect
```ob=cassandra_db.cass()```

```ob.connect(Secure Bundle Zip Path,clientID,clientSecret,keyspace)```

#### Create Table
To create table

        Parameters
        ----------
        table:table name
        columns_with_datatype: columns name with datatypes as string
```ob.create_table(table, columns_with_datatype)```

#### Insert
To insert in table

        Parameters
        ----------
        table:table name
        columns: columns name
        values: values
```ob.insert(table, columns, values)```

#### Select
To select row in table

        Parameters
        ----------
        table:table name
        columns: columns name
        where: where condition
```ob.select(table, columns, where(optional))```

#### Update
To update row in table

        Parameters
        ----------
        table:table name
        columns_with_values: columns name with values eg age=88
        where: where condition
```ob.update(table, columns_with_values, where)```

#### Delete
To delete row in table

        Parameters
        ----------
        table:table name
        where: where condition
```ob.delete(table, where)```

#### Execute Query
To execute any Cassandra query

        Parameters
        ----------
        query:Cassandra query
```ob.execute(query)```



## License

© 2021 Arjun Panwar

This repository is licensed under the MIT license. See LICENSE for details.