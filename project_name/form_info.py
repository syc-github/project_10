from flask import Blueprint,render_template
forms=Blueprint('forms',__name__,url_defaults='')


@forms.route('/register')
def register():

    pass


@forms.route('/login')
def login():
    pass


@forms.route('/error')
def error():
    return render_template('error.html')