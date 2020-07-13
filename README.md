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

### 8. Start create `@app.route("/schedule/create")` & template.html for "C" Creation

### 9. import dateime, Python strptime()
```datetime.datetime.strptime(date, "%Y-%m-%d")```

### 10. create home `@app.route("/")` & template.html for "R" Reading
Using <a href="https://getbootstrap.com/docs/4.4/content/tables/">Bootstrap Table</a> to show the schedule list, added Create button at the home page to bring external user to the create form page. Also, use of Flask `redirect` to bring external user back to the home page. 

## 11. Flash Messages 
11.a) import flash messages

11.b) Session Key generated from https://randomkeygen.com/

11.c) save the Session Key in the environment variables file 

11.d) save & restart server `python3 app.py`

11.e) read in the SESSION_KEY variable from the operating system environment ```SESSION_KEY = os.environ.get('SESSION_KEY')```

11.f) set the session Key ```app.secret_key = SESSION_KEY```

11.g) In the layout.template.html add in the code to display the flash messages:

    ```
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for m in messages %}
            <div class="alert alert-success">
                {{m}}
            </div>
            {% endfor %}
        {%endif%}
    {%endwith%}
    ```






