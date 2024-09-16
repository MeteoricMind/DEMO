from flask import Flask, render_template
import speed_typing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/typing-speed-test')
def typing_speed_test_route():
    return speed_typing.run_typing_speed_test()

if __name__ == '__main__':
    app.run()