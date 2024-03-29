from flask.cli import FlaskGroup
from todo import app, db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("init_db")
def init_db():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()