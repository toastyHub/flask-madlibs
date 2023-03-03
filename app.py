from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "toasty"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_form():
    prompts = story.prompts
    return render_template('madform.html', prompts=prompts)


@app.route('/story')
def show_story():
    ans = story.generate(request.args)
    return render_template('story.html', ans=ans)