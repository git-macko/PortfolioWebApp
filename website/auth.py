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
            flash('Email must contain an' + ' @ ' + 'and atleast 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be more than 1 character', category='error')
        elif password1 != cpassword:
            flash('Password must match its confirmation', category='error')
        elif len(password1) < 6:
            flash('Password must be more than 6 characters', category='error')
        else:
            flash('Account Created', category='success')
            
        
    return render_template("sign_up.html")

