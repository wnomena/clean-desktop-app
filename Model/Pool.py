from sqlalchemy import create_engine


class Mysql_Pool:
    def __init__(self):
        #pour le moment, root et localhost mais à changer apres quand il y aura une base de données en ligne
        self._engine = create_engine("mysql+aiomysql://root:root@localhost:3306/local_caponmada")
