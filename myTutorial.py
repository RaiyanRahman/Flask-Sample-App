from tutorial import create_app, db, cli
from tutorial.models import User, Post, Message, Notification

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}