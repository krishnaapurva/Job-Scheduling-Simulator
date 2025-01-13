import heapq
import matplotlib.pyplot as plt
import random
import time

class Task:
    def __init__(self, task_id, arrival_time, burst_time, priority=None):
        self.task_id = task_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.start_time = None
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None

class JobScheduler:
    def __init__(self, scheduling_algorithm="FCFS"):
        self.tasks = []
        self.scheduling_algorithm = scheduling_algorithm
        self.current_time = 0
        self.gantt_chart = []

    def add_task(self, task):
        self.tasks.append(task)

    def fcfs(self):
        self.tasks.sort(key=lambda task: task.arrival_time)
        for task in self.tasks:
            if self.current_time < task.arrival_time:
                self.current_time = task.arrival_time
            task.start_time = self.current_time
            self.current_time += task.burst_time
            task.completion_time = self.current_time
            task.turnaround_time = task.completion_time - task.arrival_time
            task.waiting_time = task.turnaround_time - task.burst_time
            self.gantt_chart.append((task.task_id, task.start_time, task.completion_time))

    def sjf(self):
        ready_queue = []
        self.tasks.sort(key=lambda task: task.arrival_time)
        task_index = 0
        while task_index < len(self.tasks) or ready_queue:
            while task_index < len(self.tasks) and self.tasks[task_index].arrival_time <= self.current_time:
                heapq.heappush(ready_queue, (self.tasks[task_index].burst_time, self.tasks[task_index]))
                task_index += 1

            if not ready_queue:
                self.current_time = self.tasks[task_index].arrival_time
                continue

            _, task = heapq.heappop(ready_queue)
            task.start_time = self.current_time
            self.current_time += task.burst_time
            task.completion_time = self.current_time
            task.turnaround_time = task.completion_time - task.arrival_time
            task.waiting_time = task.turnaround_time - task.burst_time
            self.gantt_chart.append((task.task_id, task.start_time, task.completion_time))

    def round_robin(self, time_quantum):
        ready_queue = []
        self.tasks.sort(key=lambda task: task.arrival_time)
        task_index = 0
        while task_index < len(self.tasks) or ready_queue:
            while task_index < len(self.tasks) and self.tasks[task_index].arrival_time <= self.current_time:
                ready_queue.append(self.tasks[task_index])
                task_index += 1

            if not ready_queue:
                self.current_time = self.tasks[task_index].arrival_time
                continue

            task = ready_queue.pop(0)
            if task.start_time is None:
                task.start_time = self.current_time

            executed_time = min(task.remaining_time, time_quantum)
            self.current_time += executed_time
            task.remaining_time -= executed_time

            if task.remaining_time == 0:
                task.completion_time = self.current_time
                task.turnaround_time = task.completion_time - task.arrival_time
                task.waiting_time = task.turnaround_time - task.burst_time
            else:
                ready_queue.append(task)

            self.gantt_chart.append((task.task_id, self.current_time - executed_time, self.current_time))

    def schedule(self, time_quantum=None):
        if self.scheduling_algorithm == "FCFS":
            self.fcfs()
        elif self.scheduling_algorithm == "SJF":
            self.sjf()
        elif self.scheduling_algorithm == "RR":
            if time_quantum is None:
                raise ValueError("Time quantum must be provided for Round Robin scheduling.")
            self.round_robin(time_quantum)
        else:
            raise ValueError("Unsupported scheduling algorithm.")

    def display_results(self):
        print("\nTask Results:")
        print("Task ID | Arrival Time | Burst Time | Start Time | Completion Time | Turnaround Time | Waiting Time")
        for task in self.tasks:
            print(f"{task.task_id:<7} | {task.arrival_time:<12} | {task.burst_time:<10} | {task.start_time:<10} | {task.completion_time:<16} | {task.turnaround_time:<15} | {task.waiting_time:<12}")

    def display_gantt_chart(self):
        print("\nGantt Chart:")
        for task_id, start_time, end_time in self.gantt_chart:
            print(f"| Task {task_id} [{start_time} - {end_time}] ", end="")
        print("|")

    def visualize_gantt_chart(self):
        plt.figure(figsize=(10, 5))
        for task_id, start_time, end_time in self.gantt_chart:
            plt.barh(task_id, end_time - start_time, left=start_time, edgecolor='black')
        plt.xlabel("Time")
        plt.ylabel("Tasks")
        plt.title("Gantt Chart")
        plt.grid(axis='x', linestyle='--', linewidth=0.7)
        plt.show()

# Interactive Mode
if __name__ == "__main__":
    def get_valid_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    print("Welcome to the Job Scheduling Simulator!")
    print("Available Scheduling Algorithms:")
    print("1. First-Come-First-Serve (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin (RR)")

    choice = input("Choose a scheduling algorithm (1/2/3): ")
    if choice == "1":
        scheduler = JobScheduler(scheduling_algorithm="FCFS")
    elif choice == "2":
        scheduler = JobScheduler(scheduling_algorithm="SJF")
    elif choice == "3":
        scheduler = JobScheduler(scheduling_algorithm="RR")
        time_quantum = get_valid_integer("Enter the time quantum for Round Robin: ")
    else:
        print("Invalid choice. Exiting...")
        exit()

    num_tasks = get_valid_integer("Enter the number of tasks: ")
    for i in range(num_tasks):
        print(f"\nEnter details for Task {i + 1}:")
        arrival_time = get_valid_integer("Arrival Time: ")
        burst_time = get_valid_integer("Burst Time: ")
        scheduler.add_task(Task(task_id=i + 1, arrival_time=arrival_time, burst_time=burst_time))

    if choice == "3":
        scheduler.schedule(time_quantum=time_quantum)
    else:
        scheduler.schedule()

    scheduler.display_results()
    scheduler.display_gantt_chart()
    scheduler.visualize_gantt_chart()

    print("\nThank you for using the Job Scheduling Simulator!")

