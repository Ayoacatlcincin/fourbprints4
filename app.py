from fourbp import app, mail
from fourbp.forms import ContactUsForm
from flask import render_template, session, request, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from flask_mail import Message
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    form = ContactUsForm()
    
    if form.validate_on_submit():
        session['first'] = form.first.data
        session['last'] = form.last.data
        session['email'] = form.email.data
        session['quantity'] = form.quantity.data
        session['dateby'] = form.dateby.data
        session['message'] = form.message.data
        msg = Message('New FourBPrints email', recipients=['fourbprints@gmail.com'], reply_to=session['email'])
        msg.body = session['message']
        if form.file.data != None:
            file = form.file.data
            filename = secure_filename(form.file.data.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with app.open_resource(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as fp:
              msg.attach(filename, "image/png", fp.read())
        mail.send(msg)
        
        flash('Thanks for the Message! We will get back to you soon!')
        return redirect(url_for('thankyou'))
    
    return render_template('contact.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')



if __name__ == '__main__':
    app.run(debug=True)
