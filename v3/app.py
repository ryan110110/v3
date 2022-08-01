from uuid import uuid4
import time,base64
from flask import Flask, render_template, url_for, redirect, request, abort
from database_client import engine
import requests

app = Flask(__name__)


@app.get("/demo/")
def index():
    return redirect(url_for('details'))

@app.get("/demo/details")
def details():
    return render_template("details.html")

@app.post("/demo/passive_liveness")
@app.get("/demo/passive_liveness")
def passive_liveness():
    if request.method == "GET":
        abort(403)
    
    data = request.form
    email = data.get("email")
    email2 = data.get("email2")
    if not email and not email2:
        abort(400)

    

    if "submit_register" in data.keys():
        db_data = list(engine.execute(f"SELECT * FROM Users WHERE email='{email}';"))

        if db_data:
            abort(400)
        else:
            name = data.get("name")
            company_name = data.get("company_name")
            phone = data.get("phone")
            api_key = str(uuid4().hex)
            engine.execute(f"INSERT INTO Users(name,email,company_name,phone_number,api_key) VALUES('{name}','{email}','{company_name}','{phone}','{api_key}');")
            return render_template("passive_liveness.html",api_key=email)

    elif "submit_login" in data.keys():
        db_data = list(engine.execute(f"SELECT * FROM Users WHERE email='{email2}';"))
        if not db_data:
            abort(400)
        else:
            return render_template("passive_liveness.html",api_key=email2)
    
    abort(403)
    

@app.post("/demo/test_passive_liveness")
def test_passive_liveness():
    data = request.get_json()

    img = data.get('b64_img')
    img = img[img.find(",")+1:]

    start = time.time()

    url = 'http://localhost:8080/check_liveness'
    files = {'Image': img}

    headers = {"x-api-key":"UHVsDmSRvmJShqy5z49QmDIZxPUsUb4iegpP9h00"}
    try:
        res =  requests.post(url,headers=headers,files=files)
        res = res.json()
    except:
        res = {}

    time_elapsed= time.time()-start

    return 1

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


'''
name email company_name phone_number api_key image

api_key result output exec_time
'''