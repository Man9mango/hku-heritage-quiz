from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-123' 

quiz_questions = [
    # MC: Identify buildings from pictures (7 questions)
    {"type": "mc", "question": "Which building is shown in the image?", "image": "university_hall.jpg",
     "options": ["University Hall", "Main Building", "May Hall"], "answer": "University Hall"},
    {"type": "mc", "question": "Identify this building from the picture.", "image": "main_building.jpg",
     "options": ["Hung Hing Ying Building", "Main Building", "Fung Ping Shan Building"], "answer": "Main Building"},
    {"type": "mc", "question": "Which building is this?", "image": "hung_hing_ying.jpg",
     "options": ["Eliot Hall", "Hung Hing Ying Building", "Tang Chi Ngong Building"], "answer": "Hung Hing Ying Building"},
    {"type": "mc", "question": "Identify the building in the image.", "image": "fung_ping_shan.jpg",
     "options": ["Fung Ping Shan Building", "May Hall", "University Hall"], "answer": "Fung Ping Shan Building"},
    {"type": "mc", "question": "Which building is shown?", "image": "tang_chi_ngong.jpg",
     "options": ["Tang Chi Ngong Building", "Main Building", "West Point Filters Bungalow"], "answer": "Tang Chi Ngong Building"},
    {"type": "mc", "question": "Identify this building.", "image": "west_point_filters_bungalow.jpg",
     "options": ["West Point Filters Bungalow", "Run Run Shaw Heritage House", "HKU Visitor Centre"], "answer": "West Point Filters Bungalow"},
    {"type": "mc", "question": "Which building is this?", "image": "run_run_shaw.jpg",
     "options": ["Run Run Shaw Heritage House", "West Point Filters Workmen's Quarters", "Eliot Pumping Station and Filters, Treatment Works building"], "answer": "Run Run Shaw Heritage House"},

    # True/False: Building facts (3 questions)
    {"type": "true_false", "question": "Lugard Hall was demolished in 1992. True or False?", "answer": "True"},
    {"type": "true_false", "question": "May Hall is one of the historical buildings. True or False?", "answer": "False"},
    {"type": "true_false", "question": "West Point Filters Workmen's Quarters is a Grade 1 historical building. True or False?", "answer": "False"},

    # Fill-in-the-blank: Establishment years and grades (3 questions)
    {"type": "fill_in_blank", "question": "Eliot Hall was established in ____.", "answer": "1914"},
    {"type": "fill_in_blank", "question": "HKU Visitor Centre is a Grade __ historical building.", "answer": "3"},
    {"type": "fill_in_blank", "question": "Eliot Pumping Station and Filters, Treatment Works building is a Grade __ historical building.", "answer": "3"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        results = []
        for i, q in enumerate(quiz_questions):
            user_answer = request.form.get(f'q{i}', '').strip()  # Handle missing answers
            is_correct = user_answer == q['answer']
            if is_correct:
                score += 1
            results.append({
                'question': q['question'],
                'user_answer': user_answer,
                'correct_answer': q['answer'],
                'is_correct': is_correct
            })
        return render_template('results.html', score=score, total=len(quiz_questions), results=results)
    return render_template('quiz.html', questions=quiz_questions)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)