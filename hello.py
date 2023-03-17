from prefect import flow, task

@task
def create_message():
    msg = 'Hello from task'
    return msg

# Sub-flow (child)
@flow
def something_else():
    result = 10 
    return result

@flow
def hello_world():
    subflow_message = something_else() 
    task_message = create_message() 
    new_message = task_message + str(subflow_message)
    print(new_message)


if __name__ == "main":
    hello_world()