from flask import Flask, render_template, request

app = Flask(__name__)

# Заглушка для списка дел
todo_list = ["Покупки", "Уборка", "Учеба"]

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    if todo:
        todo_list.append(todo)
    return render_template("index.html", todo_list=todo_list)


if __name__ == "__main__":
    app.run()