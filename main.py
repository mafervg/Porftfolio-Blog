from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/blog')
def get_post():
    return render_template("blog-post-1.html")


if __name__ == "__main__":
    app.run(debug=True)