from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import engine, SessionLocal, Base, Task
from sqlalchemy.exc import OperationalError
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env', override=True)

app = Flask(__name__, static_url_path="", static_folder="static")
CORS(app) 

def create_task(db, task_name: str):
    new_task = Task(name=task_name)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)  
    return new_task

@app.route('/', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task_name = data.get('task')  
    if new_task_name:
        db = SessionLocal() 
        try:
            new_task = create_task(db, new_task_name)  
            return jsonify({
                "message": "Task added successfully!",
                "task": {
                    "id": new_task.id,
                    "name": new_task.name
                }
            }), 201 
        except OperationalError as e:
            return jsonify({
                "error": f"Database error: {str(e)}"
            }), 500 
        finally:
            db.close()  
    return jsonify({
        "error": "Task is empty!"
    }), 400  


@app.route('/tasks', methods=['GET'])
def get_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(Task).all()
        tasks_list = [{"id": task.id, "name": task.name} for task in tasks]
        return jsonify({"tasks": tasks_list}), 200
    except OperationalError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        db.close()
        
@app.route('/')
def send_page():
    app_host = os.getenv('APP_HOST', 'localhost')  
    app_port = os.getenv('APP_PORT', '5000')      
    return render_template('index.html', app_host=app_host, app_port=app_port)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)  
    app.run(host=os.getenv('APP_HOST', '0.0.0.0'), port=int(os.getenv('APP_PORT', 5000)), debug=True)
