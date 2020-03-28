#export API_KEY=pk_4f72371f4d654123aec51e40e3b9c1f2
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")
# create portfolios table

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio_q = db.execute("SELECT DISTINCT(stock), price, SUM(num_shares) as num_shares, name FROM portfolios WHERE num_shares <> 0 AND id= :ID GROUP BY stock",
                            ID=session["user_id"])

    print("stonks =", portfolio_q)

    cash_q = db.execute("SELECT cash FROM users WHERE id = :ID",
                            ID=session["user_id"])

    portfolio_q2 = []
    val_sum = 0.0

    for p in portfolio_q: # clean up the price formatting
        if p["num_shares"] != 0:
            #portfolio_q.remove(p)
            portfolio_q2.append(p)

    for p in portfolio_q2:
        p["price"] =  usd(p["price"])
        p["current_price"] = lookup(p["stock"])["price"]
        p["value"] = p["current_price"]*p["num_shares"]
        val_sum+=float(p["value"])
        p["value"] = usd(p["value"])
        p["current_price"] = usd(p["current_price"])



    print(portfolio_q)

    total_value = float(cash_q[0]["cash"]) + float(val_sum)
    user_cash = usd(cash_q[0]["cash"])
    total_value = usd(total_value)

    return render_template("index.html", stonks=portfolio_q2, user_cash=user_cash, total_value=total_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        print(session)
        user_cash = db.execute("SELECT cash FROM users WHERE id = :ID",
                                ID=session["user_id"])

        buy = lookup(request.form.get("symbol"))
        if not buy: # return apology if stock symbol does not exist
            return apology("Stock does not exist!", 400)

         # TO DO: Generalize for anyone that has logged in
        shares = request.form.get("shares")
        if not shares.isnumeric():
             return apology("Please enter a positive integer for the number of shares!", 400)


        purchase = (float(request.form.get("shares")) * buy["price"])


        if (user_cash[0]["cash"] < purchase):
            return apology("Cannot afford!", 400)

        # insert buy order into the portfolios table
        db.execute("INSERT INTO 'portfolios' ('id','stock', 'name', 'price','num_shares') VALUES (:user_id,:ticker, :company_name,:stock_price,:num_shares)",
                    user_id=session["user_id"],
                    ticker=request.form.get("symbol").upper(),
                    company_name=lookup(request.form.get("symbol"))["name"],
                    stock_price=buy["price"],
                    num_shares=request.form.get("shares"))

        db.execute("UPDATE users SET cash = cash - :purchase WHERE id = :user_id",
                    purchase = buy["price"]*float(request.form.get("shares")),
                    user_id=session["user_id"])
        # TO DO: update cash balance for user

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    username = request.args.get("username")

    user_q = db.execute("SELECT * FROM users WHERE username = :username",
                username=username)
    if user_q:
        return jsonify(False)
    else:
        return jsonify(True)




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transaction_history = db.execute("SELECT * FROM portfolios WHERE id = :ID",
                                    ID=session["user_id"])

    for t in transaction_history:
        t["price"] = usd(t["price"])

    print(transaction_history)
    return render_template("history.html", stonks=transaction_history)

    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        print("\n")
        print(rows)
        print("\n")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        #"""Get stock quote."""
        quote = lookup(request.form.get("symbol"))

        if not quote: # return apology if stock symbol does not exist
            return apology("Stock does not exist!", 400)

        stock_name = quote["name"]
        stock_symbol = quote["symbol"]
        stock_price = quote["price"]

        return render_template("quoted.html", stock_name=stock_name, stock_symbol=stock_symbol, stock_price=usd(stock_price))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
    #"""Register user"""
    #username = requests.form.get("username")
        if not request.form.get("username"):
            return apology("Missing username!", 400)

        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("Must enter password twice!", 400)

        elif not request.form.get("password") == request.form.get("confirmation"): # passwords don't match
            return apology("Passwords must match!", 400)

        # TO DO: check to see if user already exists on table
        row = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if row:
           return apology("Username has already been registered!", 400)


        db.execute("INSERT INTO users (id, username, hash) VALUES (NULL,:user,:pw)",
                       user=request.form.get("username"),
                       pw=generate_password_hash(request.form.get("password")))

        row1 = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        session["username"] = request.form.get("username")
        session["user_id"] = row1[0]["id"]

        print("new registered user_id is", session["user_id"])
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    portfolio_q = db.execute("SELECT distinct(stock), SUM(num_shares) AS num_shares FROM portfolios WHERE id= :ID GROUP BY stock", ID=session["user_id"])
    stock_p = []

    for p in portfolio_q:
        if p["num_shares"] >= 1:
            stock_p.append(p)

    if request.method == "POST":
#        portfolio_q = db.execute("SELECT distinct(stock), SUM(num_shares) AS num_shares FROM portfolios WHERE id= :ID GROUP BY stock", ID=session["user_id"])

        sell_shares = request.form.get("shares")
        actual_shares = db.execute("SELECT distinct(stock), sum(num_shares) AS num_shares FROM portfolios WHERE id= :ID AND stock = :STOCK GROUP BY :STOCK",
                                ID=session["user_id"],
                                STOCK=request.form.get("symbol"))
        #print(actual_shares)

        user_cash = db.execute("SELECT cash FROM users WHERE id = :ID",
                                ID=session["user_id"])

        if (int(sell_shares) > actual_shares[0]["num_shares"]):
            return apology("Too many shares!", 400)

        # insert sell order into portfolios
        db.execute("INSERT INTO 'portfolios' ('id','stock', 'name', 'price','num_shares') VALUES (:user_id,:ticker, :company_name,:stock_price,:num_shares)",
                    user_id=session["user_id"],
                    ticker=request.form.get("symbol"),
                    company_name=lookup(request.form.get("symbol"))["name"],
                    stock_price=lookup(request.form.get("symbol"))["price"],
                    num_shares=int(sell_shares)*-1)

        db.execute("UPDATE users SET cash = cash + :sell WHERE id = :user_id",
                    sell = lookup(request.form.get("symbol"))["price"]*float(sell_shares),
                    user_id=session["user_id"])



        print(stock_p)

        print("portfolio is", portfolio_q)


        return redirect("/")
    else:
        return render_template("sell.html", stonks=stock_p)



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
