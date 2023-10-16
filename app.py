from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page_form():
    return render_template("madlib_form.html")


@app.route('/story')
def create_story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")

    story = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

    ans = {"verb": verb, "noun": noun, "place": place,
           "plural_noun": plural_noun, "adjective": adjective}

    madlib_story = story.generate(ans)

    return render_template("story.html", madlib_story=madlib_story)
