# 🤖 Cyber Reminder Bot

A fully automated Telegram bot that sends daily penetration testing tasks, built to help cybersecurity learners stay consistent and reach expert-level skill in 12 weeks.

> 💡 Built with ❤️ by [@Kindosticx](https://github.com/Kindosticx) — powered by GitHub Actions, Python, and the Telegram Bot API.

---

## 📌 Features

- ⏰ **Daily automated tasks** delivered at 9:00 AM WAT
- 🛡️ Covers **advanced penetration testing topics** (SQLi, XSS, phishing, API hacking, etc.)
- ⚙️ **Hosted serverlessly** via GitHub Actions — no Render, no cron jobs!
- 🧠 Designed for **solo learners and cybersecurity communities**
- 💬 Command support coming soon: `/today`, `/next`, `/resources`, `/reset`

---

## 🧰 Technologies Used

- Python
- Telegram Bot API
- GitHub Actions (CI Scheduler)
- JSON (for roadmap data)

---

## 🚀 Getting Started

### 1. Fork & Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/cyber-reminder-bot.git
cd cyber-reminder-bot

2. Set Your Bot Token & Chat ID
Update send_task.py with your:

BOT_TOKEN (from BotFather)

CHAT_ID (your Telegram user ID)

3. Add Your GitHub Secrets (Optional for security)
Instead of hardcoding, store:

BOT_TOKEN → in GitHub Secrets

CHAT_ID → in GitHub Secrets

4. Enable GitHub Actions
Your bot will run daily using .github/workflows/reminder.yml

To test it immediately:

Go to your repo > Actions tab > Run workflow manually.

🛠️ Roadmap (12 Weeks)
✅ Beginner → Advanced Penetration Tester
📚 Topics include:

Kali Linux setup

SQL Injection

XSS & CSRF

Phishing Simulations

API testing

Buffer overflows

Post-exploitation

and more...

(See roadmap.json for full list)

👨‍💻 Creator
Kindness Chimeremeze
Cybersecurity Analyst | Educator | Dev-In-Progress
🔗 https://www.linkedin.com/in/kindness-chimeremeze-907b57210/
📫 kindnesschimeremeze@gmail.com
