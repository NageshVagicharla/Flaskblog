from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Nagesh Vagicharla',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 12, 2021'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 12, 2021'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

if __name__ == '__main__':
    app.run(debug=True)