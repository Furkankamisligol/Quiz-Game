import requests
question_raw_data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_raw_data.raise_for_status()
question_data = question_raw_data.json()["results"]

