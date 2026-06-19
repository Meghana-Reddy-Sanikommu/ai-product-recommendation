from flask import Flask, render_template, request, redirect, session
from models import db, User, SearchHistory
import pandas as pd
from recommender import get_recommendations

app = Flask(__name__)
app.secret_key="mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    if "user_name" not in session:
        return redirect("/login")

    user_name = session.get("user_name")
    return render_template("index.html", user_name=user_name)


@app.route("/products")
def products():

    df = pd.read_csv("dataset/products.csv")

    products_list = df.to_dict(orient="records")

    return render_template(
        "products.html",
        products=products_list
    )


@app.route("/search", methods=["POST"])
def search():

    product_name = request.form["product_name"]

    # Save search history (AI memory)
    if "user_email" in session:
        history = SearchHistory(
            user_email=session["user_email"],
            product_name=product_name
        )
        db.session.add(history)
        db.session.commit()

    # Get user search history
    user_history = []

    if "user_email" in session:

        past_searches = SearchHistory.query.filter_by(
            user_email=session["user_email"]
        ).all()

        user_history = [
            item.product_name
            for item in past_searches
        ]

    best_match, better_options, other_options = get_recommendations(
        product_name,
        user_history
    )
    print("BEST MATCH:", best_match)
    print("BETTER OPTIONS:", better_options)
    print("OTHER OPTIONS:", other_options)

    return render_template(
        "results.html",
        best_match=best_match,
        better_options=better_options,
        other_options=other_options
    )
@app.route("/history")
def history():

    if "user_email" not in session:
        return redirect("/login")

    user_email = session["user_email"]

    searches = SearchHistory.query.filter_by(
        user_email=user_email
    ).all()

    return render_template(
        "history.html",
        searches=searches
    )
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/")

    return render_template("signup.html")
@app.route("/users")
def users():

    all_users = User.query.all()

    output = ""

    for user in all_users:

        output += (
            f"ID: {user.id} | "
            f"Name: {user.name} | "
            f"Email: {user.email}<br>"
        )

    return output
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            session["user_name"] = user.name
            session["user_email"] = user.email
            return redirect("/")

        return "Invalid Email or Password"

    return render_template("login.html")
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/") 

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":

            session["admin"] = True

            return redirect("/admin/dashboard")

        return "Invalid Admin Login"

    return render_template("admin_login.html")
@app.route("/admin/dashboard")
def admin_dashboard():

    if "admin" not in session:
        return redirect("/admin")

    return render_template("admin_dashboard.html")

@app.route("/add_product", methods=["GET", "POST"])
def add_product():

    if "admin" not in session:
        return redirect("/admin")

    if request.method == "POST":

        product = request.form["product"]
        category = request.form["category"]
        brand = request.form["brand"]
        price = request.form["price"]
        rating = request.form["rating"]
        tags = request.form["tags"]
        description = request.form["description"]
        image = request.form["image"]

        with open("dataset/products.csv", "a") as f:

            f.write(
    f"\n{product},{category},{brand},{price},{rating},{tags},{description},{image}"
)

        return "Product Added Successfully"

    return render_template("add_product.html")
if __name__ == "__main__":
    app.run(debug=True)