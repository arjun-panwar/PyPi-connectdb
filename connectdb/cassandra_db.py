from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


class cass:
    """
    It helps to connect cassandra database and perform below operation
    connect
    create_table
    insert
    select
    update
    delete
    query
    """

    def __init__(self):
        self.session = ""

    def connect(self, path, clientId, clientSecret, keyspace):
        """
        It is used for connect with Casandra DB

        Parameters
        ----------
        path: secure connect bundle zip file Path
        clientId: clientId of database
        clientSecret: clientSecret of database
        keyspace: name of current keyspace
        """
        cloud_config = {"secure_connect_bundle": path}
        auth_provider = PlainTextAuthProvider(clientId, clientSecret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect(keyspace)
        row = self.session.execute("select release_version from system.local").one()
        if row:
            return "Cassandra DB- connected" + row[0]
        else:
            return "Cassandra DB- connection error"

    def create_table(self, table, columns_with_datatype):
        """
        To create table

        Parameters
        ----------
        table:table name
        columns_with_datatype: columns name with datatypes as string
        """
        try:
            qry = f"""
            create table {table} ({columns_with_datatype});
            """
            self.session.execute(qry)
            return f"Cassandra DB- table created--Name={table}, columns={columns_with_datatype} "

        except Exception as e:
            return f"Cassandra DB-create table error--{str(e)}"

    def insert(self, table, columns, values):
        """
        To insert in table

        Parameters
        ----------
        table:table name
        columns: columns name
        values: values
        """
        try:
            qry = f"""
            insert into {table} ({columns}) values ({values});
             """
            self.session.execute(qry)
            return f"Cassandra DB- data inserted -- Table={table}, columns={columns},values={values} "
        except Exception as e:
            return f"Cassandra DB-data insert error--{str(e)}"

    def select(self, table, columns, where=""):
        """
        To select row in table

        Parameters
        ----------
        table:table name
        columns: columns name
        where: where condition
        """
        try:
            if where == "":
                qry = f"""
                     select {columns} from {table} ALLOW FILTERING;
                      """
            else:
                qry = f"""
                    select {columns} from {table} where {where} ALLOW FILTERING;
                    """

            rows = self.session.execute(qry)
            return rows
        except Exception as e:
            return f"Cassandra DB-data selection error--{str(e)}"

    def update(self, table, columns_with_values, where):
        """
        To update row in table

        Parameters
        ----------
        table:table name
        columns_with_values: columns name with values eg age=88
        where: where condition
        """
        try:
            qry = f"""
            update {table} set {columns_with_values} where {where};
             """
            self.session.execute(qry)
            return f"Cassandra DB- data updated -- Table={table}, columns={columns_with_values}, where={where} "
        except Exception as e:
            return f"Cassandra DB-data updating error--{str(e)}"

    def delete(self, table, where):
        """
        To delete row in table

        Parameters
        ----------
        table:table name
        where: where condition
        """
        try:
            qry = f"""
            delete from {table} where {where};
             """
            self.session.execute(qry)
            return f"Cassandra DB- data deleted-- Table={table}, where={where} "
        except Exception as e:
            return f"Cassandra DB-data deleting error--{str(e)}"

    def execute(self, query):
        """
        To execute any Cassandra query

        Parameters
        ----------
        query:Cassandra query
        """
        try:

            self.session.execute(query)
            return f"Cassandra Query executed successfully - Query={query}"
        except Exception as e:
            return f"Cassandra Query not executed - Query={query} error--{str(e)}"


#ob = cassandra()
#ob.connect("secure-connect-image-scrapper.zip", "gpJgkOAuHfZBaiwtkZiTBInR","-DeDEiUWk2,5tQrBZGrZuiYSqUaLUifZsFdNos2ual+D01CAMfg,A_FGScwC1l-_+PTugfOs0X3EIvHF4Az_ZZ2eRytKoptf6f0u7r2U8,9wTbTKfSZnuA452tlUiSvi", "user_data")
