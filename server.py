"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      Hi! This is the home page.
      <a href="http://localhost:5000/hello">Click here to say hello!</a>

    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    options_string = ""

    for compliment in AWESOMENESS:
        option_text = "<option value='%s'>%s</option>\n" % (compliment, compliment)
        options_string += option_text

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          <select name="compliment"><br>
            <option value=" " disabled selected>Choose a compliment!</option>
            %s
          </select>
          <input type="submit" value="Submit"><br><br>
        </form>
        <form action="/diss">
        What's your name? <input type="text" name="person"><br>
        <select name="diss">
            <option value=" " disabled selected>Choose a diss!</option>
            <option value="smelly">smelly</option>
            <option value="stupid">stupid</option>
            <option value="ugly">ugly</option>
            <option value="mean">mean</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """ % (options_string)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment", "silent")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():
    """Disses user."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Ew, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
