# MIME (Multipurpose Internet Mail Extensions) types. Browser use the MIME-type, not the file extension to determine
# how to process a URL. Important for Web servers to send correct MIME type in the response "Content-Type" header.
""" Types:
Application/octet-stream: Default for binary files. Browsers usually don't execute or even ask if it should
be executed. Treat it as if the "content-Disposition header was set to attachment and propose a "Save as" dialog.

text/plain: Default for textual files. Even if it really means "unknown textual file", browsers assume they can display
it.

text/css: CSS files used to style a Web page MUST be sent with text/css. If a server doesn't recognize the .css suffix
for CSS files, it may send them with text/plain or "application/octet-stream" MIME types. If so, won't be recognized as
CSS by most browsers and will be ignored.

text/html: All HTML content should be served with this type.

text/javascript: Per the HTML specification, JavaScript files should always be served using this MIME type. No other
values are considered valid, and using any of those may result in scripts that don't run or load.
Or can also be: application/javascript

Image types. example image/png....

...etc
"""

from flask import Flask, render_template, url_for, request, redirect
import csv
html_database_txt = "C:/Users/Fikret/PycharmProjects/WebsitesPython/venv/database.txt"
html_database_csv = "C:/Users/Fikret/PycharmProjects/WebsitesPython/venv/database.csv"

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

# we can use following to make sure we don't use multiple route and functions.
# note, works isn't working for now, need to be changed.
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)



def write_to_txt_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv_file(data): # to add data to our CSV-file database.
    with open("database.csv", newline="", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_txt_file(data)
            write_to_csv_file(data)
            return redirect("/thankyou.html") # Redirecting to a different page.
        except:
            return "Did not save to database"
    else:
        return "Something went wrong, try again"

# Database // Database management system (DBMS)

# Type of Databases:

#Relational Databases: MySQL, Oracle Databases, Access (Microsoft)
"""
Relationship DB Consists of two or more tables with columns and rows.
example: Users is a table (name of the table) and full_name, username, etc... are colums under it.
values for the (columns) full_name, username are the rows.
Each row represents an entry and each column sorts a very specific type of information, like name, address...
Relationship between tables and field is called schema.

if we take twitter as an example (tables: "users", "tweets" and "following"): username in the "users" table, we can 
connect with, username in the "tweets" table (and username in users table is the Foreign Key in the tweets table) and
the from_user & to_user in the "following" table will be the Foreign Key in the users table (for username).
Things like Full name or ID, something that identifies each row in a table: It's called a Primary key.

All Relational Databases uses SQL to communicate with the server
"""

# NoSQL / Non Relational Database (redis, riak, Cassandra, CouchDB, Hypertable, mongoDB:
"""
This can be defined as we go, while Rel DB requires it be defined first (pre-defined).
This type, is good if data requirements are not clear outside the project.
And offer great flexibility, like folders.

mongoDB (is document oriented) stores information as documents.
this database app will for example store <each users> information (tweets, followers...) as separate documents.
(relationships DB have them; users, tweets, followers, stored in each separate files)

mongoDB uses MongoDB query language to communicate with the server.
"""

# PythonAnywhere (pythonanywhere.com)