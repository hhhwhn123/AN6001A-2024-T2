#
#Syn code space is very high risk, somrtimes fail

from flask import Flask
from flask import render_template, request
import textblob
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POSTpython "])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA", methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result", methods=["GET","POST"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r))

@app.route("/AI", methods=["GET", "POST"])
def AI():
    
    return render_template("AI.html")

@app.route("/AI_result", methods=["GET","POST"])
def AI_result():
    q = request.form.get("q")
    r = ask_gemini(q)
    return (render_template("AI_result.html", r=r))

def ask_gemini(q):
    api = os.getenv("maskersuite")
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    r = model.generate_content(q)
    text = r.candidates[0].content.parts[0].text
    return text

if __name__ == "__main__":
    app.run()
    api = os.getenv("maskersuite")
    genai.configure(api_key=api)
    m = genai.GenerativeModel("gemini-1.5-flash")
