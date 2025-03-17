from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page (Landing Page)
@app.route('/')
def home():
    return render_template('index.html')

# Questions Page
@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        answers = request.form.to_dict()  # Get answers from form
        feedback = analyze_thoughts(answers)  # Process answers
        return render_template('result.html', feedback=feedback)
    return render_template('questions.html')

# Function to analyze responses
def analyze_thoughts(answers):
    # Basic logic (replace this with AI/ML if needed)
    if 'yes' in answers.values():
        return "You are an optimistic thinker!"
    else:
        return "You tend to be a bit cautious in your thoughts."

if __name__ == '__main__':
    app.run(debug=True)
