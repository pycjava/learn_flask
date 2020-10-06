# coding:utf-8

from ihome import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


#创建flask的应用对象
app = create_app("develop")



if __name__ == "__main__":
    app.run()