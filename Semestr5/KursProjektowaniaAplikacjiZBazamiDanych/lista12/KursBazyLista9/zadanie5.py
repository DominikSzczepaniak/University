from inigo_py.flask import Middleware
import requests

graphql_url = "http://localhost:4000"

app = Flask(__name__)

config = {
    'INIGO': {  
        'TOKEN': os.environ.get('eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOm51bGwsInRva2VuVHlwZSI6InNlcnZpY2VfdG9rZW4iLCJ1c2VyX3Byb2ZpbGUiOiJzaWRlY2FyIiwidXNlcl9yb2xlcyI6WyJzaWRlY2FyIl0sInVzZXJfaWQiOjM3NjEsInVzZXJfbmFtZSI6IkRvbWluaWtTemN6ZXBhbmlhay90ZXN0L3Byb2QiLCJvcmdfaWQiOjI0NDQsIm9yZ19kZXNjIjoiMjQ0NF9Eb21pbmlrU3pjemVwYW5pYWsiLCJ0b2tlbiI6IjFkOWYzZTRjLTgyMzYtNDdmZS1hMjk5LWQ0OWVhM2JjYWJmYSIsImVuY3J5cHRpb25fa2V5IjoiWmJHU0tnTXZtVzM1ZTlHWFo3T0E5b3hWbWo2UVpHT2RYdm9uUGVrbWsrND0iLCJpYXQiOjE3MzczMDgyNTMsInN1YiI6InRlc3Q6cHJvZCJ9.dmYSxIs--3_blg_iJYroyrQas6PNuQxX7HNFXPdFskMegasrvbXu7pNwlJMzurDqqK4TOk5_zC7Nn5l_X_jlWg', ''),
        'PATH': '/query',
        'GRAPHENE_SCHEMA': 'app.schema.schema',
    },
}

app.config.update(config)
app.wsgi_app = Middleware(app)


def create_task(title, description):
  mutation = """
  mutation CreateTask($title: String!, $description: String) {
    createTask(title: $title, description: $description) {
      id
    }
  }
  """

  data = {
      "title": title,
      "description": description
  }

  response = requests.post(graphql_url, json={"query": mutation, "variables": data})

  if response.status_code == 200:
      data = response.json()
      return data["data"]["createTask"]["id"]
  else:
      print(f"Error creating task: {response.text}")
      return None


def get_tasks():
  query = """
  query GetTasks {
    tasks {
      id
      title
      description
    }
  }
  """

  response = requests.post(graphql_url, json={"query": query})

  if response.status_code == 200:
      data = response.json()
      return data["data"]["tasks"]
  else:
      print(f"Error retrieving tasks: {response.text}")
      return None


title = input("Enter task title: ")
description = input("Enter task description (optional): ")

task_id = create_task(title, description)

if task_id:
  print(f"Task created with ID: {task_id}")
  tasks = get_tasks()
  if tasks:
    print("All tasks:")
    for task in tasks:
      print(f"- ID: {task['id']}, Title: {task['title']}, Description: {task.get('description', '')}")
  else:
    print("No tasks found.")
else:
  print("Error creating task.")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, use_reloader=False)