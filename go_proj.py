from flask import Flask, json, jsonify, redirect, url_for, request, flash, session, Response, render_template

# configuration
#DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

application = Flask(__name__)
application.config.from_object(__name__)

player_queue = []

@application.route('/')
def main_view():
    return render_template('game_view.html')  # Temporarily just redirect to the game

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Try login details later
        #if request.form['username'] != app.config['USERNAME']:
        #    error = 'Invalid username'
        #elif request.form['password'] != app.config['PASSWORD']:
        #    error = 'Invalid password'
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('main_view'))
    else:
        return render_template('login.html')


@application.route('/logout')
def logout():
    return Response('Logout', mimetype='text/plain')

@application.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        id = request.form.get('id')
        if len(player_queue) == 0:
            player_queue.append(id)
            return json.dumps({'status': 'OK'})
        else:
            p2 = player_queue.pop()
            return jsonify(id=p2)
    else:
        return render_template('test_conn.html')

@application.route('/test')
def css_test():
    return render_template('csstest.html')

@application.route('/go')
def go_view():
    return render_template('game_view.html')

@application.route('/disconnect_user', methods=['POST'])
def disconnect_user():
    id = request.form.get('id')
    print(player_queue)
    player_queue.remove(id)
    print(player_queue)
    return json.dumps({'status': 'OK'})


if __name__ == '__main__':
    application.run()
