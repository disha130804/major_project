

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secret123"

# Temporary users storage (for demo purpose)
users = {}

# ✅ Sign Up route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        

        if username in users:
            flash("User already exists! Please sign in.", "error")
            return redirect(url_for("signin"))

        users[username] = password
        flash("Signup successful! Please login.", "success")
        return redirect(url_for("signin"))

    return render_template("signup.html")

# ✅ Sign In route
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["user"] = username
            flash("Login successful!", "success")
            return render_template("front.html")
        else:
            flash("Invalid username or password", "error")

    return render_template("signin.html")

# ✅ Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("signin"))


# ✅ Home page (check login required)
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("signin"))
    return render_template("signin.html", user=session["user"])


# ✅ Correct answers dictionary
answers = {
    "english": {
        "q1": "glad",
        "q2": "She went to school everyday",
        "q3": "sofa",
        "q4": "The lesson is explained by the teacher.",
        "q5": "coward"
    },
    "science": {
        "q1": "newton",
        "q2": "Water",
        "q3": "Litmus",
        "q4": "Nucleus",
        "q5": "Photosynthesis"
    },
    "geography": {
        "q1": "Asia",
        "q2": "Nile",
        "q3": "Himalayas",
        "q4": "Arctic Ocean",
        "q5": "Arunachal Pradesh"
    },
    "gk": {
        "q1": "Mahatma Gandhi",
        "q2": "Lotus",
        "q3": "1947",
        "q4": "Jupiter",
        "q5": "Rabindranath Tagore"
    }
}



@app.route("/english_quiz", methods=["GET", "POST"])
def english_quiz():
    if request.method == "POST":
        score = check_score(request.form, "english")
        return render_template("result.html", subject="English", score=score, total=5)
    return render_template("Englishquiz.html")

@app.route("/science_quiz", methods=["GET", "POST"])
def science_quiz():
    if request.method == "POST":
        score = check_score(request.form, "science")
        return render_template("result.html", subject="Science", score=score, total=5)
    return render_template("Sciencequiz.html")

@app.route("/geography_quiz", methods=["GET", "POST"])
def geography_quiz():
    if request.method == "POST":
        score = check_score(request.form, "geography")
        return render_template("result.html", subject="Geography", score=score, total=5)
    return render_template("Geography.html")

@app.route("/gk_quiz", methods=["GET", "POST"])
def gk_quiz():
    if request.method == "POST":
        score = check_score(request.form, "gk")
        return render_template("result.html", subject="General Knowledge", score=score, total=5)
    return render_template("Gk.html")

# ✅ Score checking function
def check_score(form_data, subject):
    score = 0
    for q, correct in answers[subject].items():
        if form_data.get(q) == correct:
            score += 1
    return score

if __name__ == "__main__":
    app.run(debug=True)





