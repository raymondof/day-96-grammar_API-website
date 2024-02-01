from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import csv

app = Flask(__name__)


# Define the CSV file name and path
csv_file_name = "./static/assets/data/data.csv"

# Check if the CSV file exists
if not os.path.exists(csv_file_name):
    # Create the CSV file with header
    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Original Text', 'Corrected Text'])
else:
    # CSV file already exists, no need to create it again
    print(f"{csv_file_name} already exists.")

# Open the CSV file and print its contents to the console
with open(csv_file_name, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    print("\nCSV File Contents:")
    for row in reader:
        print(row[0], "|", row[1])


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
    # Open the CSV file and read its contents
    with open(csv_file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        rows = [row for row in reader]

    # Reverse the rows to display in opposite order
    reversed_rows = rows[::-1]

    return render_template("index.html", header=header, rows=reversed_rows)


@app.route("/correct-text", methods=["POST"])
def correct_text():
    original_text = request.form["text_to_correct"]
    response = grammar_bot(original_text).json()
    corrected_text = response["correction"]

    # Add the new data to the CSV file
    with open(csv_file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([original_text, corrected_text])

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5008)
