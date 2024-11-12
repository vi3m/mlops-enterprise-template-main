Let's dive deeper into how Airflow works with Docker containers and how environment variables can drive the execution.
## Airflow and Docker Integration
Airflow provides a DockerOperator that allows you to run tasks within Docker containers. Here's a simplified overview of the process:
- Airflow creates a Docker container from a specified image.
- Airflow sets environment variables within the container.
- Airflow runs the container, executing the command specified in the DockerOperator.
- The container executes the task, and Airflow monitors its progress.
- Upon completion, Airflow retrieves the container's logs and updates the task's status.
## Using Environment Variables to Drive Execution
Environment variables can be used to:
Pass parameters to the container.
Configure the container's behavior.
Determine which code function to run.
Here are some examples:
### Example 1: Passing Parameters
dag.py:
Python
```python
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator

default_args = {
    'environment_variables': [
        {"name": "NAME", "value": "John"},
        {"name": "AGE", "value": "30"},
    ]
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval=None,
)

task = DockerOperator(
    task_id='print_name',
    image='python:3.9-slim',
    command='python -c "import os; print(f\'Hello, {os.environ[\'NAME\']}! You are {os.environ[\'AGE\']} years old.\')"',
    dag=dag,
)
```

In this example, the NAME and AGE environment variables are passed to the container and used in the Python script.
### Example 2: Configuring Behavior
dag.py:
Python
```python
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator

default_args = {
    'environment_variables': [
        {"name": "LOG_LEVEL", "value": "DEBUG"},
    ]
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval=None,
)

task = DockerOperator(
    task_id='run_app',
    image='my-app:latest',
    command='python app.py',
    dag=dag,
)
```
In this example, the LOG_LEVEL environment variable configures the logging level for the app.py script.
### Example 3: Driving Code Execution
dag.py:
Python
```python
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator

default_args = {
    'environment_variables': [
        {"name": "FUNCTION_TO_RUN", "value": "process_data"},
    ]
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval=None,
)

task = DockerOperator(
    task_id='run_function',
    image='my-app:latest',
    command='python runner.py',
    dag=dag,
)
```
runner.py:
Python
```python
import os

def process_data():
    # Process data logic
    print("Processing data...")

def send_notification():
    # Send notification logic
    print("Sending notification...")

if __name__ == "__main__":
    function_to_run = os.environ["FUNCTION_TO_RUN"]
    globals()[function_to_run]()
```
In this example, the FUNCTION_TO_RUN environment variable determines which function to execute in the runner.py script.

### Using dummy_key to Drive Execution
Based on your original code snippet, you can modify the runner.py script to use the dummy_key environment variable:
runner.py:
Python
```python
import os

def function1():
    # Function 1 logic
    print("Running function 1...")

def function2():
    # Function 2 logic
    print("Running function 2...")

if __name__ == "__main__":
    dummy_key = os.environ["dummy_key"]
    if dummy_key == "value1":
        function1()
    elif dummy_key == "value2":
        function2()
```
dag.py:
Python
```python
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator

default_args = {
    'environment_variables': [
        {"name": "dummy_key", "value": "value1"},
    ]
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval=None,
)

task = DockerOperator(
    task_id='run_function',
    image='my-app:latest',
    command='python runner.py',
    dag=dag,
)
```
In this example, the dummy_key environment variable determines which function to execute in the runner.py script.
I hope these examples help you understand how Airflow works with Docker containers and how environment variables can drive the execution!


# More Details

Certainly! Let’s explore how Apache Airflow works with Docker containers and how environment variables can influence the execution of tasks within a DAG.

### Overview of Airflow with Docker

1. **Airflow DAGs**: Airflow uses Directed Acyclic Graphs (DAGs) to represent workflows. Each task in a DAG can be a Python function, an external script, or a command that runs in a container.

2. **Docker Operator**: Airflow provides the `DockerOperator`, which allows you to run tasks in Docker containers. This means that each task can have its own environment and dependencies.

### Using Environment Variables

Environment variables can determine which function or logic to execute in a container. Here’s a simple example to illustrate this.

### Example DAG

```python
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

def determine_function(dummy_key):
    if dummy_key == "function_a":
        return "Running Function A"
    elif dummy_key == "function_b":
        return "Running Function B"
    else:
        return "Unknown function"

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(dag_id='example_dag', default_args=default_args, schedule_interval='@daily') as dag:
    
    run_function = DockerOperator(
        task_id='run_function',
        image='my_docker_image:latest',
        command='python -c "from my_module import determine_function; print(determine_function(\'{{ dag_run.conf.get(\'dummy_key\', \'default\') }}\'))"',
        environment_variables=[
            {"name": "DUMMY_KEY", "value": "{{ dag_run.conf.get('dummy_key', 'default') }}"}
        ],
        auto_remove=True,
        dag=dag,
    )
```

### Explanation

1. **DAG Definition**: The DAG is defined with a daily schedule.

2. **DockerOperator**:
   - **Image**: Specifies the Docker image to use.
   - **Command**: This runs a Python command within the container. It imports a function and calls it based on the value of an environment variable (`DUMMY_KEY`).

3. **Environment Variables**:
   - The `DUMMY_KEY` variable is set using a Jinja template that allows you to pass in a value when triggering the DAG. The default value is `'default'`.

### Triggering the DAG

You can trigger this DAG manually (e.g., via the Airflow UI or CLI) and provide a configuration:

```bash
airflow dags trigger -c '{"dummy_key": "function_a"}' example_dag
```

### Output

- If `dummy_key` is set to `"function_a"`, the container will execute `determine_function` and print `"Running Function A"`.
- If set to `"function_b"`, it will print `"Running Function B"`.
- If the key is unknown or not provided, it defaults to `"Unknown function"`.

### Conclusion

In this example, the use of environment variables within a Docker container allows dynamic control over the task’s execution. You can easily adapt your workflow based on input parameters, making it flexible and powerful for various use cases.