## Deployment 

### b) PRODUCTION

#### Launch a workspace container at Gitpod

### 1. Create file --> requirements.txt  

```
click==7.1.2
dnspython==1.16.0
Flask==1.1.2
itsdangerous==1.1.0
pymongo==3.10.1
python-dotenv==0.13.0
Werkzeug==1.0.1
```

The requirements we are installing are:

* `pip3 install flask`
* `pip3 install pymongo` -- to use Mongo DB
* `pip3 install dnspython` -- is to allow us to connect to Mongo with just the URL
* `pip3 install python-dotenv` -- allows the use of `.env` files for environment variables

### 2. How to use requirements.txt
```
pip3 install -r requirements.txt
```
### 3. Create `.env` file to store the passwords and security-sensitive information.
### 4. Create `.gitignore` file to git ignore the environment variables file, which are never committed to the repository.
```
.env
```
### 5. Create file `app.py` and insert flask template

### 6. Connect mongodb 

### 7. Open Browser
To run a backend Python file, type `python3 app.py`, if Python file is named `app.py` of course.
A blue button should appear to click: *Make Public*,
Another blue button should appear to click: *Open Browser*.

### 8. Start create `@app.route("/")` & template.html for "C" Creation

### 9. import dateime, Python strptime()
```datetime.datetime.strptime(date, "%Y-%m-%d")```

### 10. create `@app.route("/")` & template.html for "R" Reading
Using <a href="https://getbootstrap.com/docs/4.4/content/tables/">Bootstrap Table</a> to show the schedule list, added Create button at the home page to bring external user to the create form page. Also, use of Flask `redirect` to bring external user back to the home page. 


