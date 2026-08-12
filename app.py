from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print("Name:", name)
        print("Email:", email)
        print("Feedback:", message)

        return render_template('thankyou.html')

    return render_template('feedback.html')


@app.route('/profile.png')
def profile_image():
    return send_from_directory('.', 'profile.png')


if __name__ == '__main__':
    app.run(debug=True)
