from flask import Flask, render_template, request, redirect, url_for, flash
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo
import datetime

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
CLOUD_NAME = os.environ.get("CLOUD_NAME")
UPLOAD_PRESET = os.environ.get("UPLOAD_PRESET")

client = pymongo.MongoClient(MONGO_URI)
DB_NAME = "pro3"

SESSION_KEY = os.environ.get("SESSION_KEY")
app.secret_key = SESSION_KEY


@app.route("/")
def home():
    search_pol = request.args.get("search_pol")
    search_pod = request.args.get("search_pod")

    criteria = {}

    if search_pol != "" and search_pol is not None:
        criteria["pol"] = {
            "$regex": search_pol,
            "$options": "i"
        }

    if search_pod != "" and search_pod is not None:
        criteria["pod"] = {
            "$regex": search_pod,
            "$options": "i"
        }

    schedules = client[DB_NAME].schedule.find(criteria)
    images = client[DB_NAME].profile.find()
    return render_template("home.template.html",
                           schedules=schedules,
                           images=images)


# Schedule Session
@app.route("/schedule/create")
def schedule_create_form():
    return render_template("schedule_create.template.html")


@app.route("/schedule/create", methods=["POST"])
def schedule_create_process():
    eta_pol = request.form.get("eta_pol")
    pol = request.form.get("pol")
    pod = request.form.get("pod")
    eta_pod = request.form.get("eta_pod")
    vessel = request.form.get("vessel")
    vovage = request.form.get("vovage")
    transit_days = request.form.get("transit_days")
    company_name = request.form.get("company_name")
    website = request.form.get("website")

    client[DB_NAME].schedule.insert_one({
        "eta_pol": datetime.datetime.strptime(eta_pol, "%Y-%m-%d"),
        "pol": pol,
        "pod": pod,
        "eta_pod": datetime.datetime.strptime(eta_pod, "%Y-%m-%d"),
        "vessel": vessel,
        "vovage": vovage,
        "transit_days": transit_days,
        "company_name": company_name,
        "website": website
    })
    flash(f"New schedule '{vessel} V.{vovage}' has been created")
    return redirect(url_for("home"))


@app.route("/schedule/update/<id>")
def schedule_update_form(id):    
    schedule = client[DB_NAME].schedule.find_one({
        "_id": ObjectId(id)
    })
    return render_template("schedule_update.template.html", schedule=schedule)


@app.route("/schedule/update/<id>", methods=["POST"])
def schedule_update_process(id):
    eta_pol = request.form.get("eta_pol")
    pol = request.form.get("pol")
    pod = request.form.get("pod")
    eta_pod = request.form.get("eta_pod")
    vessel = request.form.get("vessel")
    vovage = request.form.get("vovage")
    transit_days = request.form.get("transit_days")
    company_name = request.form.get("company_name")
    website = request.form.get("website")

    eta_pol = datetime.datetime.strptime(eta_pol, "%Y-%m-%d")
    eta_pod = datetime.datetime.strptime(eta_pod, "%Y-%m-%d")

    client[DB_NAME].schedule.update_one({
        "_id": ObjectId(id)
    }, {
        "$set": {
            "eta_pol": eta_pol,
            "pol": pol,
            "pod": pod,
            "eta_pod": eta_pod,
            "vessel": vessel,
            "vovage": vovage,
            "transit_days": transit_days,
            "company_name": company_name,
            "website": website
        }
    })
    flash(f"'{vessel} V.{vovage}' has been updated")
    return redirect(url_for("home"))


@app.route("/schedule/delete/<id>")
def schedule_delete_form(id):
    schedule = client[DB_NAME].schedule.find_one({
        "_id": ObjectId(id)
    })
    return render_template("schedule_delete_form.template.html",
                           schedule=schedule)


@app.route("/schedule/delete/<id>", methods=["POST"])
def schedule_delete_process(id):
    client[DB_NAME].schedule.remove({
        "_id": ObjectId(id)
    })
    flash("One schedule has been deleted")
    return redirect(url_for("home"))


# Profile Ads Session
@app.route("/profile/upload")
def profile_upload():
    return render_template("profile_upload.template.html",
                           cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)


@app.route("/profile/upload", methods=["POST"])
def profile_upload_process():
    uploaded_image_url = request.form.get("uploaded_image_url")
    description = request.form.get("description")
    company_name = request.form.get("company_name")
    website = request.form.get("website")
    client[DB_NAME].profile.insert_one({
        "uploaded_image_url": uploaded_image_url,
        "description": description,
        "company_name": company_name,
        "website": website
    })
    flash("profile created!!")
    return redirect(url_for("home"))


@app.route("/profile/update/<id>")
def profile_update_form(id):
    profile = client[DB_NAME].profile.find_one({
        "_id": ObjectId(id)
    })
    return render_template("profile_update.template.html",
                           profile=profile,
                           cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)


@app.route("/profile/update/<id>", methods=["POST"])
def profile_update_process(id):
    uploaded_image_url = request.form.get("uploaded_image_url")
    description = request.form.get("description")
    company_name = request.form.get("company_name")
    website = request.form.get("website")
    client[DB_NAME].profile.update_one({
        "_id": ObjectId(id)
    }, {
        "$set": {
            "uploaded_image_url": uploaded_image_url,
            "description": description,
            "company_name": company_name,
            "website": website
        }
    })
    flash(f"Your profile '{company_name}' has been updated")
    return redirect(url_for("home"))


@app.route("/profile/delete/<id>")
def profile_delete_form(id):
    profile = client[DB_NAME].profile.find_one({
        "_id": ObjectId(id)
    })
    return render_template("profile_delete.template.html", profile=profile)


@app.route("/profile/delete/<id>", methods=["POST"])
def profile_delete_process(id):
    company_name = request.form.get("company_name")
    client[DB_NAME].profile.remove({
        "_id": ObjectId(id)
    })
    flash("Profile has been deleted")
    return redirect(url_for("home"))

   # "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
