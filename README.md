# 📝 CLI To-Do List (Python)

A simple command-line To-Do List application written in Python.  
The project allows users to add, edit, complete, delete, and persist tasks using a local JSON-based storage system.

---

## 🚀 Features

- Add new tasks with description, priority, and deadline
- Edit existing tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using a local file (`advancedTasks.txt`)
- Simple CLI-based menu system

---

## 🧠 How It Works

The application stores tasks in a list of dictionaries and saves them into a JSON-formatted text file.  
Each task contains:

- description (string)
- completed (boolean)
- priority (low / medium / high)
- deadline (YYYY-MM-DD)

---

## ▶️ How to Run

This project is executed via Python script and can optionally be run on Google Colab using GitHub cloning.

### Local (Python)
```
bash
python AdvancedToDoList.py
```

### Online (Google Colab)

```
!git clone https://github.com/MichaelScarnnn/python-todolist.git
%cd python-todolist
!python AdvancedToDoList.py
```