from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)



def grammar_bot(text):
    url = "https://grammarbot-neural.p.rapidapi.com/v1/check"
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Host": "grammarbot-neural.p.rapidapi.com",
        "X-RapidAPI-Key": os.environ["X-RapidAPI-Key"]
    }
    dummy_text = "This are somme well-writen text. bu how bad tecxt u cn fix."
    data = {
        "text": text,
        "lang": "en"
    }

    response = requests.post(url, headers=headers, json=data)
    return response


@app.route("/")
def main():
    with app.app_context():
        all_tasks = [1, 2, 3]
        all_ready_tasks = ["a", "b", "c"]
        # result = db.session.execute(db.select(Task).order_by(Task.task_name))
        # all_tasks = [task.task_name for task in result.scalars()]
        #
        # ready_result = db.session.execute(db.select(ReadyTask).order_by(ReadyTask.task_name))
        # all_ready_tasks = [task.task_name for task in ready_result.scalars()]
    return render_template("index.html", tasks=all_tasks, ready_tasks=all_ready_tasks)

@app.route("/add-task", methods=["POST"])
def add_task():
    text_to_check = request.form["text_to_correct"]
    response = grammar_bot(text_to_check).json()
    corrected_text = response["correction"]
    print(corrected_text)


    return render_template("index.html", corrected_text=corrected_text)




# @app.route("/check-ready-task", methods=["POST"])
# def check_ready_task():
#     selected_task_name = request.form.get("task")
#     task_to_move = Task.query.filter_by(task_name=selected_task_name).first()
#
#     if task_to_move:
#         # Create a new ReadyTask instance with the task name
#         ready_task = ReadyTask(task_name=task_to_move.task_name)
#
#         # Add the ReadyTask instance to the session
#         db.session.add(ready_task)
#
#         # Commit the changes to the ReadyTask table
#         db.session.commit()
#
#         # Remove the task from the Task table
#         db.session.delete(task_to_move)
#         db.session.commit()
#
#     return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(debug=True, port=5008)