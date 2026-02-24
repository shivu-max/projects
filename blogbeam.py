from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# -------------------- APP SETUP --------------------
blogbeam = Flask(__name__)
blogbeam.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
blogbeam.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(blogbeam)

# -------------------- MODELS --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    posts = db.relationship('BlogPost', backref='author', lazy=True)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# -------------------- DATABASE --------------------
with blogbeam.app_context():
    db.create_all()
    # Create a default user if not exists
    if not User.query.filter_by(username='admin').first():
        default_user = User(username='admin', email='admin@blogbeam.com', password='admin123')
        db.session.add(default_user)
        db.session.commit()
    print("👍 Database and tables created.")

# -------------------- ROUTES --------------------
@blogbeam.route("/")
def index():
    return redirect(url_for('home'))

@blogbeam.route("/home")
def home():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template("index.html", posts=posts, title="Home")

@blogbeam.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        
        new_post = BlogPost(title=title, content=content, author_id=1)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add_post.html", title="Add New Post")


@blogbeam.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


@blogbeam.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit_post.html", post=post, title="Edit Post")

     
# -------------------- RUN --------------------
if __name__ == "__main__":
    blogbeam.run(host='0.0.0.0', port=5001, debug=True)
