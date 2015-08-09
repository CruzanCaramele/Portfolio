from flask import Flask, render_template, url_for

app = Flask(__name__)

#constants
DEBUG = True
PORT = 8030
HOST = "0.0.0.0"

#home page
@app.route("/")
def index():
	return render_template("index.html")


#skills
@app.route("/skills")
def skills():
	return render_template("skills.html")


if __name__ == '__main__':
	app.run(debug=DEBUG,
		  port=PORT,
		  host=HOST
		)


