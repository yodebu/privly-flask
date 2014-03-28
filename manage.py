from flask.ext.script import Manager

from pyvly import helpers, database, main


# Initialize the manager
manager = Manager(main.app)


@manager.option('-e', '--email', required=True, help="User's email address")
@manager.option('-p', '--password', required=True, help="User's password")
def create_user(email, password):
    """Creates a user in the database"""
    helpers.create_user(email, password)

@manager.command
def init_db():
    """Intializes the Database"""
    database.init_db()

# Run the manager when called directly
if __name__ == '__main__':
    manager.run()