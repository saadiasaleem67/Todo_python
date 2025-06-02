from flask import Flask, render_template,url_for,request,redirect
import random
app = Flask(__name__)
todos=[{
    "id":1,
    "name":"write pyhton",
   "checked":False
},
{
    "id":1,
    "name":"Code Checking",
   "checked":True
},
    
]

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    if (request.method == "POST"):
        todo_name=request.form["todo_name"]
        car_id=random.randint(1, 1000)
        todos.append({
            "id":car_id,
            "name":todo_name,
           
   })
    return render_template("game.html",items=todos)

@app.route("/delete/<int:todo_id>",methods=["POST"])
def delete_todo(todo_id):
    global todos 
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)