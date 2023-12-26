from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage using a dictionary
users_data = {}
user_id_counter = 1

@app.route('/')
def index():
    users = list(users_data.values())
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    global user_id_counter

    if request.method == 'POST':
        new_user = {'id': user_id_counter, 'name': request.form['name']}
        users_data[user_id_counter] = new_user
        user_id_counter += 1

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    if id in users_data:
        del users_data[id]

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
