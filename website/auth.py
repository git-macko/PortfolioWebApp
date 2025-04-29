from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        cpassword = request.form.get('cpassword')
        
        if len(email) < 4:
            flash('Email must contain an' + ' @ ' + 'and atleast 4 characters')
        elif len(firstName) < 2:
            pass
        elif password1 != cpassword:
            pass
        elif len(password1) < 6:
            pass
        else:
            # ADD DATABASE
            pass
            
        
    return render_template("sign_up.html")

