from collections import namedtuple, defaultdict, Counter, deque, OrderedDict
Employee = namedtuple('Employee', ['emp_id', 'name', 'department', 'salary'])
employee_records = OrderedDict()
dept_groups = defaultdict(list)
dept_counts = Counter()
task_queue = deque()
def add_employee(emp_id, name, department, salary):
    """Adds a new employee record and updates grouping and counts."""
    if emp_id in employee_records:
        print(f"Error: Employee ID {emp_id} already exists.")
        return
    new_emp = Employee(emp_id, name, department, salary)
    employee_records[emp_id] = new_emp
    dept_groups[department].append(new_emp)
    dept_counts[department] += 1
    print(f"Employee {name} (ID: {emp_id}) added successfully.")
def assign_task(emp_id, task_description):
    """Assigns a task to an existing employee and adds it to the queue."""
    if emp_id not in employee_records:
        print(f"Error: Cannot assign task. Employee ID {emp_id} not found.")
        return
    
    employee = employee_records[emp_id]
    task = {"emp_id": emp_id, "name": employee.name, "task": task_description}
    task_queue.append(task)
    print(f"Task '{task_description}' assigned to {employee.name}.")

def complete_task():
    """Removes and completes the oldest task from the queue."""
    if not task_queue:
        print("No tasks in the queue to complete.")
        return
    
    completed = task_queue.popleft()
    print(f"Completed Task: '{completed['task']}' by {completed['name']} (ID: {completed['emp_id']})")

def display_by_department(department):
    """Displays all employees in a specific department using defaultdict."""
    employees = dept_groups.get(department)
    if not employees:
        print(f"No employees found in the '{department}' department.")
        return
    
    print(f"\n--- Employees in {department} ---")
    for emp in employees:
        print(f"ID: {emp.emp_id} | Name: {emp.name} | Salary: ${emp.salary}")

def show_task_queue():
    """Displays current pending tasks in the deque."""
    print(f"\n--- Current Task Queue (Pending: {len(task_queue)}) ---")
    if not task_queue:
        print("Queue is empty.")
    for i, task in enumerate(task_queue, 1):
        print(f"{i}. {task['task']} (Assigned to: {task['name']})")

def display_department_summary():
    """Displays employee counts per department using Counter."""
    print("\n--- Department Employee Summary ---")
    if not dept_counts:
        print("No records available.")
    for dept, count in dept_counts.items():
        print(f"Department: {dept:15} | Employee Count: {count}")


if __name__ == "__main__":

    add_employee(101, "Alice Johnson", "Engineering", 95000)
    add_employee(102, "Bob Smith", "Sales", 60000)
    add_employee(103, "Charlie Davis", "Engineering", 98000)
    add_employee(104, "Diana Prince", "HR", 70000)
    
    
    add_employee(101, "Duplicate Alice", "Engineering", 95000)

    display_department_summary()

  
    display_by_department("Engineering")

    
    print("\n--- Assigning Tasks ---")
    assign_task(101, "Fix server bug")
    assign_task(102, "Client follow-up call")
    assign_task(103, "Update API docs")
    assign_task(999, "Secret mission")  

    show_task_queue()

    
    print("\n--- Processing Tasks ---")
    complete_task()  
    show_task_queue()
