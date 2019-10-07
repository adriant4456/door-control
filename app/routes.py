from flask import render_template, redirect
import json
from app import app
from app.servo_control import servo_lock, servo_unlock, lock_status

lock_status()
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/locked', methods=['GET', 'POST'])
def lock():
    if not lock_status():
        servo_lock()
    print('locked')
    return render_template('locked.html')

@app.route('/unlocked', methods=['GET', 'POST'])
def unlock():
    if lock_status():
        servo_unlock()
    return render_template('unlocked.html')


    
