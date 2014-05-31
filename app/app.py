from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__.split(".")[0])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lon.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    with app.app_context():
        import routes
    manager.run()
