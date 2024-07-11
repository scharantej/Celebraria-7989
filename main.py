
# Flask imports
from flask import Flask, render_template, request, redirect

# Create the Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Handle the message sending logic here
    # ...
    
    return redirect('/contact')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
