#!/usr/bin/python3
"""
Renders home page
"""

from collections import defaultdict
from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, session, url_for)
import requests
from flask_login import current_user, login_required
from models import storage
from models.quiz import Quiz
from models.score import Score
from models.user import User

home = Blueprint('home', __name__)

categories = {
    'General Knowledge': '9',
    'Entertainment: Books': '10',
    'Entertainment: Film': '11',
    'Entertainment: Music': '12',
    'Entertainment: Musicals & Theatres': '13',
    'Entertainment: Television': '14',
    'Entertainment: Video Games': '15',
    'Entertainment: Board Games': '16',
    'Science & Nature': '17',
    'Science: Computers': '18',
    'Science: Mathematics': '19',
    'Mythology': '20',
    'Sports': '21',
    'Geography': '22',
    'History': '23',
    'Politics': '24',
    'Art': '25',
    'Celebrities': '26',
    'Animals': '27',
    'Vehicles': '28',
    'Entertainment: Comics': '29',
    'Science: Gadgets': '30',
    'Entertainment: Japanese Anime & Manga': '31',
    'Entertainment: Cartoon & Animations': '32',
}

colors = [
    "#1a1a2e", "#16213e", "#0f3460", "#53354a", "#2e294e",
    "#1f4068", "#2b2e4a", "#3a506b", "#1c2541", "#344955",
    "#212121", "#1e1e24", "#202040", "#323232", "#2c3e50",
    "#1b263b", "#2d4059", "#1c1c1c", "#283149", "#2d2d34",
    "#232931", "#293462", "#1d1e33", "#222831", "#232323"
]


@home.route('/', methods=['GET'])
def index():
    """Renders index page"""
    return render_template('/home_page.html', categories=categories,
                           colors=colors)


@home.route('/generate_quiz', methods=['POST'])
@login_required
def generate_quiz():
    """Generates quiz based on the category selected"""

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    category = request.form.get('category')
    difficulty = request.form.get('difficulty')
    quiz_type = request.form.get('quiz_type')

    session['category'] = category

    params = ""
    if difficulty != "Any":
        params = "&difficulty={}".format(difficulty.lower())

    if quiz_type != "Any":
        params = params + "&type={}".format(quiz_type)

    url = "https://opentdb.com/api.php?amount=10&category={}{}".format(
            categories.get(category), params)

    response = requests.get(url=url)

    if response.status_code == 200:
        questions = response.json()['results']
        session['questions'] = questions
        return render_template('quiz.html', questions=questions,
                               title=category)
    else:
        return jsonify({'error': 'Failed to fetch questions'}), 500


@home.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    """Handles quiz submission and calculates score"""
    questions = session['questions']
    score = 0
    for i, question in enumerate(questions):
        selected_answer = request.form.get(f'question{i+1}')
        correct_answer = question['correct_answer']
        if selected_answer == correct_answer:
            score += 1
    percentage = (score / 10) * 100

    # Create and save quiz to the database
    quiz_data = {'user_id': current_user.id, 'title': session['category'], 'questions': questions}
    quiz = Quiz(**quiz_data)
    quiz.save()

    # Create score and save to the database
    score_data = {'user_id': current_user.id, 'quiz_id': quiz.id, 'score': percentage}
    score = Score(**score_data)
    score.save()

    flash(f"You have scored: {percentage}%", "success")
    return render_template('corrections.html', questions=questions)


@home.route('/leader_board', methods=['GET'])
@login_required
def leader_board():
    """Returns to ten users with the highest score"""
    scores_list = [score.to_dict() for key, score in storage.all(Score).items()]
    
    users_list = [user.to_dict() for key, user in storage.all(User).items()]
    # Dictionary to hold the sum of scores and count of quizzes for each user
    user_data = defaultdict(lambda: {"total_score": 0.0, "quiz_count": 0})

    # Iterate over the list and sum the scores and count quizzes for each user
    for score_entry in scores_list:
        user_id = score_entry["user_id"]
        score = score_entry["score"]
        user_data[user_id]["total_score"] += score
        user_data[user_id]["quiz_count"] += 1

    # Create a dictionary to map user_id to full names
    user_names = {user["id"]: f"{user['first_name']} {user['last_name']}" for user in users_list}

    # Create a list of dictionaries with the user's name, total score, and quiz count
    top_scores = [
        {
            "name": user_names[user_id],
            "total_score": data["total_score"],
            "quiz_count": data["quiz_count"]
        }
        for user_id, data in user_data.items()
    ]

    # Sort the list by total scores in descending order
    top_scores = sorted(top_scores, key=lambda x: x["total_score"], reverse=True)
    return render_template('leader_board.html', top_scores=top_scores)


@home.route('/history', methods=['GET'])
@login_required
def history():
    """Returns users attempted quizzes"""
    quizzes = storage.all(Quiz)
    user_quizzes = [quiz.to_dict() for key, quiz in quizzes.items() if quiz.user_id == current_user.id]

    return render_template('history.html', quizzes=user_quizzes)
