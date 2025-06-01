# 🧠 TaskMate – AI Task Manager

TaskMate is a smart, OOP-based task management system built entirely in **Python** with a frontend powered by **Streamlit**. It allows users to add, list, and manage tasks through an interactive web interface.

---

## ✨ Features

- ✅ Add tasks with title, description, and priority
- 📋 View all tasks with status indicators
- 🔄 Mark tasks as completed
- ❌ Delete individual tasks
- 🔁 Reset entire task list
- 🧠 Built using clean Object-Oriented Programming principles

---

## 🏗️ Project Structure

taskmate/
├── app.py                  ← Main Streamlit app
├── models/
│   ├── __init__.py
│   ├── task.py             ← Task class
│   ├── user.py             ← User class
│   └── task_manager.py     ← Manages users & tasks
├── utils/
│   └── session_state.py 

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/taskmate.git
cd taskmate

🐍 Python Environment Setup
2. Create & Activate Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # or `venv\\Scripts\\activate` on Windows

3. Install Dependencies

pip install -r requirements.txt

▶️ Run the App

streamlit run app.py

Then visit: http://localhost:8501


🧠 OOP Components Explained
Task class: represents a single task with attributes like title, description, priority, and status.

TaskManager class: handles operations like add, list, delete, and complete tasks.

app.py: Streamlit UI connecting user inputs with the TaskManager logic.

📌 Future Improvements
🗃️ Persistent storage (e.g., JSON or SQLite)

📅 Due date and scheduling features

🧠 AI-based prioritization

🧑‍💼 Multi-user login (using streamlit-auth or Firebase)


👨‍💻 Author
Made with 💻 by [Anus Butt]
📬 Reach me at: buttanus3@gmail.com
