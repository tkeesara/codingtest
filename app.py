from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
questions = [
    "What is the capital of Cuba?",
    "What is the capital of France?",
    "What is the capital of Poland?",
    "What is the capital of Germany?"
]

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify({
        "questionnaireTitle": "Geography Questions",
        "questionsText": questions
    })

if __name__ == '__main__':
    app.run(debug=True)
