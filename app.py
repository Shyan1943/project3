from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

DB_NAME = "pro3"

@app.route("/")
def home():
    return "Home"

@app.route("/schedule/create")
def schedule_create_form():
    return render_template("schedule_create.template.html")

@app.route("/schedule/create", methods=["POST"])
def schedule_create_process():
    eta_pol_date = request.form.get("eta_pol_date")
    pol = request.form.get("pol")
    pod = request.form.get("pod")
    eta_pod_date = request.form.get("eta_pod_date")
    vessel = request.form.get("vessel")
    vovage = request.form.get("vovage")
    transit_days = request.form.get("transit_days")

    client[DB_NAME].schedule.insert_one({
        "eta_pol_date": datetime.datetime.strptime(eta_pol_date, "%Y-%m-%d"),
        "pol": pol,
        "pod": pod,
        "eta_pod_date": datetime.datetime.strptime(eta_pod_date, "%Y-%m-%d"),
        "vessel": vessel,
        "vovage": vovage,
        "transit_days": transit_days
    })

    return "Schedule created successful!!"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)