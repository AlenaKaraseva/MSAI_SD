import typing as t
from dataclasses import dataclass
from datetime import datetime

import flask

app = flask.Flask(__name__)


@dataclass
class Post:
    post_id: int
    title: str
    content: str
    date: datetime

    def serialize(self):
        return {
            'id': self.post_id,
            'title': self.title,
            'content': self.content,
            'date': self.date
        }


class Storage:
    def __init__(self) -> None:
        self._counter: int = 0
        self._posts_by_id = {}
        self._posts = []

    def _generate_next_id(self) -> int:
        self._counter += 1
        return self._counter

    def create(self, title: str, content: str) -> Post:
        post = Post(
            post_id=self._generate_next_id(),
            title=title,
            content=content,
            date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )

        self._posts_by_id[post.post_id] = post
        self._posts.append(post)

        return post

    def all(self) -> t.List[Post]:
        return list(reversed(self._posts))

    def get_by_id(self, post_id: int) -> t.Optional[Post]:
        if post_id not in self._posts_by_id:
            return None  # exception

        return self._posts_by_id[post_id]


posts_storage = Storage()


@app.route('/')
def view_index():
    posts = []

    for post in posts_storage.all():
        posts.append(post.serialize())

    return flask.render_template(
        'index.html',
        posts=posts,
        create_url=flask.url_for('view_create_post_form'),
    )


@app.route('/<int:post_id>')
def view_post_detail(post_id: int):
    post = posts_storage.get_by_id(post_id)
    if post is None:
        return flask.abort(404)

    return flask.render_template('detail.html', post=post.serialize())


@app.route('/create-form', methods=('GET',))
def view_create_post_form():
    return flask.render_template('create.html')


@app.route('/create-post', methods=('POST',))
def view_create_post():
    post = posts_storage.create(
        title=flask.request.form['title'],
        content=flask.request.form['content'],
    )

    return flask.redirect(flask.url_for('view_post_detail', post_id=post.post_id))
