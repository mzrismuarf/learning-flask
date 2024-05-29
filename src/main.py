import os

# from flask import Flask, send_file, render_template
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# @app.route("/")
# def index():
#     return send_file('index.html')

@app.route("/")
def index():
    return render_template('home.html', name='hohn')    

@app.route('/conditional')
def conditional():
    user = {
        'name': 'Jhonx',
        'age': 2
    }
    return render_template('conditional.html', user=user)

# looping
@app.get('/loop')
def loop():
    users = ['xabi', 'wirtz', 'rudiger']
    return render_template('loops.html', users=users)

@app.get('/inherit')
def inherit():
    return render_template('child.html')

# macro
@app.get('/macro')
def macro():
    return render_template('macro.html')

# import
@app.get('/import')
def import_macro():
    return render_template('import.html')

# context_processor
@app.context_processor
def inject_user():
    return {
        'user': {
            'name': 'Jhonx',
            'age': 2
        }
    }

@app.context_processor
def utility_processor():
    def format_age(age):
        return f"{round(age)} years"
    return dict(format_age=format_age)   



@app.get('/context_processor')
def context_processor():
    return render_template('context_processor.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
