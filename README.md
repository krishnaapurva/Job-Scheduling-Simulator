# Job Scheduling Simulator
This project is a Python-based Job Scheduling Simulator designed to demonstrate the workings of common CPU scheduling algorithms. It simulates First-Come-First-Serve (FCFS), Shortest Job First (SJF), and Round Robin (RR) algorithms, providing a clear understanding of their differences and behavior through numerical outputs and visualizations.

## Features
* #### Interactive Simulation:
  - Users can choose a scheduling algorithm and input task details interactively.
* #### Scheduling Algorithms:
  - First-Come-First-Serve (FCFS)
  - Shortest Job First (SJF)
  - Round Robin (RR) with customizable time quantum
* #### Detailed Task Statistics:
  - Arrival Time, Burst Time, Start Time, Completion Time, Turnaround Time, and Waiting Time for each task.
* #### Gantt Chart Visualization:
  - Visual representation of task scheduling for better understanding.
* #### Error Handling:
  - Ensures valid input for all numerical fields, preventing runtime errors.
 
## Installation
1. Clone the repository:
   ```
   git clone https://github.com/krishnaapurva/Job-Scheduling-Simulator.git
   cd Job-Scheduling-Simulator
   ```

2. Install dependencies:
   ```
   pip install matplotlib
   ```

## Usage
1. Run the script:
   ```python scheduling_simulator.py```
2. Follow the on-screen prompts:
  * Choose a scheduling algorithm.
  * Input the number of tasks.
  * Provide arrival time and burst time for each task.
  * For Round Robin, specify the time quantum.

## Example Workflow
#### Input:
```
Welcome to the Job Scheduling Simulator!
Available Scheduling Algorithms:
1. First-Come-First-Serve (FCFS)
2. Shortest Job First (SJF)
3. Round Robin (RR)
Choose a scheduling algorithm (1/2/3): 3
Enter the time quantum for Round Robin: 2
Enter the number of tasks: 3

Enter details for Task 1:
Arrival Time: 0
Burst Time: 5

Enter details for Task 2:
Arrival Time: 1
Burst Time: 3

Enter details for Task 3:
Arrival Time: 2
Burst Time: 8
```
![](https://github.com/krishnaapurva/Job-Scheduling-Simulator/blob/411412d67517098fd20479f2625d0338de5f482a/Input.png)
#### Output:
![Gantt Chart](https://github.com/krishnaapurva/Job-Scheduling-Simulator/blob/2aa077d871b4851ae21bbe44a78dfe9d4e6d657d/Gantt%20Chart.png)
## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.
