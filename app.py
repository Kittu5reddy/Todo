from flask import Flask,render_template,url_for,request,redirect
from model import db,User
from utils import generate_password,verify_password
app=Flask(__name__)



@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/completed-todo')
def completePage():
    return render_template('complete.html')


@app.route('/signup',methods=['GET',"POST"])
def signupPage():
    if request.method=="POST":
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        if confirm_password!=password:
            return render_template('signup.html',message="Password not matching")
        if db.query(User).filter(User.email==email).first():
            return render_template('signup.html',message="email alreadt  exits")
        user=User(first_name=first_name,last_name=last_name,email=email,password=generate_password(password))
        db.add(user)
        db.commit()
        return redirect(url_for('loginPage'))
    return render_template('signup.html')


@app.route('/login',methods=['GET',"POST"])
def loginPage():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        if db.query(User).filter(User.email!=email).first():
            return render_template('loginPage.html',message="email not found")
        user=db.query(User).filter(User.email).first()
        if verify_password(password,user.password):
            return redirect(url_for("dashboard"))
    return render_template('login.html')



if __name__=="__main__":
   
    app.run(debug=True)