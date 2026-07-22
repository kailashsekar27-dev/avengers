from flask import Flask, render_template, request, redirect, url_for
import os
import csv
from parser import extract_text, extract_skills


app = Flask(__name__)



# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Data files
DATA_FOLDER = "data"
USER_FILE = os.path.join(DATA_FOLDER, "users.csv")


# Create folders
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)



# Function to find matching opportunities with percentage
def find_matches(user_skills):

    matches = []

    file_path = os.path.join(
        DATA_FOLDER,
        "opportunities.csv"
    )


    with open(file_path, "r") as file:

        reader = csv.DictReader(file)


        for row in reader:

            required_skills = row["Skills"].split()


            matched_skills = []


            for skill in user_skills:

                if skill.lower() in [
                    x.lower() for x in required_skills
                ]:

                    matched_skills.append(skill)



            if len(matched_skills) > 0:

                percentage = int(
                    (len(matched_skills) / len(required_skills)) * 100
                )


                row["Match"] = percentage

                row["Matched Skills"] = ", ".join(matched_skills)


                matches.append(row)



    return matches






# Home page
@app.route("/")
def home():

    return render_template("index.html")




# Login page
@app.route("/login")
def login():

    return render_template("login.html")




# Save login details
@app.route("/user_login", methods=["POST"])
def user_login():

    name = request.form["name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    password = request.form["password"]

    

    with open(USER_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            email,
            mobile,
            password
        ])


    print("User Details Saved")


    return redirect(url_for("dashboard"))




# Dashboard page
@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")




# Resume upload
@app.route("/upload", methods=["POST"])
def upload():

    resume = request.files["resume"]


    if resume.filename == "":
        return "Please select a resume"



    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )


    resume.save(filepath)


    print("Resume Uploaded Successfully")
    print("File:", filepath)



    # Extract text from PDF
    text = extract_text(filepath)



    # Extract skills
    skills = extract_skills(text)



    print("Extracted Skills:")
    print(skills)



    # Find matching opportunities
    matches = find_matches(skills)
    



    return render_template(
        "recommendation.html",
        skills=skills,
        matches=matches
    )




# Recommendation page
@app.route("/recommendation")
def recommendation():

    return render_template(
        "recommendation.html"
    )




if __name__ == "__main__":
    app.run(debug=True)