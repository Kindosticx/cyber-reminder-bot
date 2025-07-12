import os
import json
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
USER_INPUT = os.environ.get("USER_INPUT", "").strip().lower()

with open("roadmap.json") as f:
    roadmap = json.load(f)
with open("progress.json") as f:
    progress = json.load(f)

def send(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    )

if USER_INPUT == "/today":
    day = progress["current_day"]
    task = roadmap.get(str(day), "🎉 All tasks done!")
    send(f"📅 *Day {day}*\n{task}")

elif USER_INPUT == "/next":
    day = progress["current_day"] + 1
    task = roadmap.get(str(day), "🎉 No more tasks ahead.")
    send(f"⏭️ *Next Task - Day {day}*\n{task}")

elif USER_INPUT == "done":
    if progress["current_day"] < len(roadmap):
        progress["current_day"] += 1
        with open("progress.json", "w") as f:
            json.dump(progress, f)
        send("✅ Great! Progress saved. Use /today to see your next task.")
    else:
        send("🎉 You’ve already completed all tasks!")
else:
    send("🤖 Unknown command. Use `/today`, `/next`, or type `done`.")

