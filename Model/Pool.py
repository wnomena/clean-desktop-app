from sqlalchemy.ext.asyncio import create_async_engine

class Getter_For_Txt_File:
    def initaliser(self):
        with open("database_info.txt","r+") as file:
            data = file.readline().split(",")
            self.user = data[2]
            self.password = data[3]
            self.host = data[0]
            self.database_name = data[1]
            self.port = data[4]

class Mysql_Pool(Getter_For_Txt_File):
    def __init__(self):
        self.initaliser()
        #pour le moment, root et localhost mais à changer apres quand il y aura une base de données en ligne
        if self.user:
            self._engine = create_async_engine(f"mysql+aiomysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}") 
        else:
            self._engine = None
