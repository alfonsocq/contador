from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)

app.secret_key = 'el-viaje- de-Chihiro'

@app.route('/')                           
def principal():
    #contador=0
    if "contador" in session:
     session["contador"] =  session["contador"]+ 1
    else:
     session["contador"] = 0
    return render_template('index.html')

@app.route("/destroy_session")
def  delete():
   session.pop("contador", None)
   return redirect("/")

@app.route("/plusdos")
def suma():
   session["contador"] +=1
   return redirect("/")

if __name__=="__main__":
    app.run(debug=True) 

