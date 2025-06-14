from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated DB (in-memory)
policies = [
    {"id": 1, "name": "Life Cover", "premium": 1000},
    {"id": 2, "name": "Car Insurance", "premium": 1500},
]

@app.route('/')
def index():
    return render_template('index.html', policies=policies)

@app.route('/policy/<int:policy_id>')
def policy(policy_id):
    policy = next((p for p in policies if p['id'] == policy_id), None)
    return render_template('policy.html', policy=policy)

@app.route('/add', methods=['POST'])
def add_policy():
    name = request.form['name']
    premium = int(request.form['premium'])
    new_id = policies[-1]['id'] + 1
    policies.append({"id": new_id, "name": name, "premium": premium})
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Triggering Jenkins
