from flask import render_template, redirect
import json
from app import app
from app.servo_control import servo_lock, servo_unlock, lock_status

@app.route('/')
@app.route('/index')
def index():
    if lock_status == "locked":
        return render_template('locked.html')
    elif lock_status == "unlocked":
        return render_template('unlocked.html')

@app.route('/locked', methods=['GET', 'POST'])
def lock():
    if lock_status not "locked":
        servo_lock()
    return render_template('locked.html')

@app.route('/unlocked', methods=['GET', 'POST'])
def lock():
    if lock_status not "unlocked":
        servo_unlock()
    return render_template('unlocked.html')


    
