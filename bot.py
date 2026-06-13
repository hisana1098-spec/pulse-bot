import requests
from datetime import datetime


def get_weather(city="Kochi"):
    try:
        url = f"https://wttr.in/{city}?format=3"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.text.strip()

    except Exception:
        return "Weather unavailable"


def get_quote():
    try:
        response = requests.get(
            "https://zenquotes.io/api/random",
            timeout=10
        )

        response.raise_for_status()

        data = response.json()[0]

        quote = data["q"]
        author = data["a"]

        return f'"{quote}" — {author}'

    except Exception:
        return "Quote unavailable"


def build_summary():

    today = datetime.now().strftime("%d-%m-%Y")

    weather = get_weather()

    quote = get_quote()

    summary = f"""
==============================
      PULSE DAILY SUMMARY
==============================

Date: {today}

Weather:
{weather}

Quote:
{quote}

==============================
"""

    return summary


def run():

    summary = build_summary()

    print(summary)

    with open(
        "daily_summary.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(summary)


if __name__ == "__main__":
    run()
