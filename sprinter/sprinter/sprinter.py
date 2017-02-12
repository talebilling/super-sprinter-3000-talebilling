import os
from peewee import *
from sprinter.connectdatabase import DatabaseConnection
from sprinter.models import Story
from flask import Flask, request, g, redirect, url_for, render_template, current_app


# create our application
app = Flask(__name__, static_url_path="", static_folder="static")
app.config.from_object(__name__)

# load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'sprinter.db'),
    SECRET_KEY='development key'
))
app.config.from_envvar('SPRINTER_SETTINGS', silent=True)


def init_db():
    DatabaseConnection.db.connect()
    DatabaseConnection.db.create_tables([Story], safe=True)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('OK - Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.sqlite_db.close()


@app.route('/')
@app.route('/list')
def show_stories():
    stories = Story.select().order_by(Story.id.asc())
    return render_template('list.html', stories=stories)


@app.route('/story', methods=['GET'])
def new_story():
    story = Story(title='',
                  story='',
                  criteria='',
                  business=100,
                  estimation=0.5,
                  status='')
    return render_template('story.html', story=story, is_new_story=True)


@app.route('/story', methods=['POST'])
def save_story():
    new_story = Story(title=request.form['title'],
                      story=request.form['story'],
                      criteria=request.form['criteria'],
                      business=request.form['business'],
                      estimation=request.form['estimation'],
                      status=request.form['status']
                      )
    new_story.save()
    return redirect(url_for('show_stories'))


@app.route('/story/<id>', methods=['GET'])
def edit_story(id):
    story = Story.select().where(Story.id == id).get()
    return render_template('story.html', story=story)


@app.route('/story/<id>', methods=['POST'])
def update_story(id):
    edited_story = Story.update(title=request.form['title'],
                                story=request.form['story'],
                                criteria=request.form['criteria'],
                                business=request.form['business'],
                                estimation=request.form['estimation'],
                                status=request.form['status']
                                ).where(Story.id == id).execute()
    return redirect(url_for('show_stories'))


@app.route('/delete/<id>', methods=['GET'])
def delete_story(id):
    Story.delete().where(Story.id == id).execute()
    return redirect(url_for('show_stories'))
