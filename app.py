from flask import Flask, render_template, request

app = Flask(__name__)

# Define unique questions and their options
QUESTIONS = [
    "Do you often feel anxious or worried about everyday situations?",
    "Have you lost interest in activities you once enjoyed?",
    "Do you experience sudden mood swings without clear reasons?",
    "Do you find it difficult to concentrate or make decisions?",
    "Have you been feeling unusually tired or lacking energy lately?",
    "Do you often feel hopeless about the future?",
    "Do you have trouble sleeping or sleep too much?",
    "Do you frequently experience feelings of guilt or worthlessness?",
    "Have you had thoughts of hurting yourself or giving up?",
    "Do you avoid social gatherings or feel isolated from others?"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        answers = []
        for i in range(len(QUESTIONS)):
            ans = request.form.get(f'q{i}')
            answers.append(ans)

        # Simple psychologist-style logic:
        score = 0
        for ans in answers:
            if ans == 'yes':
                score += 2
            elif ans == 'sometimes':
                score += 1

        # Interpret score
        if score >= 15:
            result = (
                "Your responses indicate signs of moderate to severe psychological distress. "
                "It may be helpful to seek professional support from a psychologist or counselor. "
                "Remember, you are not alone and help is available."
            )
        elif 7 <= score < 15:
            result = (
                "You may be experiencing mild symptoms of stress or depression. "
                "Try self-care techniques such as regular exercise, maintaining social connections, "
                "and relaxation practices. If symptoms persist, consider consulting a professional."
            )
        else:
            result = (
                "Your answers suggest that you are currently coping well psychologically. "
                "Keep taking care of your mental health and stay mindful of your emotional wellbeing."
            )

        return render_template('result.html', result=result)

    return render_template('questions.html', questions=QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True)
