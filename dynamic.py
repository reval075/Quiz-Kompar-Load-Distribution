import heapq
import random

def dynamic_distribution(num_nodes=4, num_tasks=20):
    # priority queue (min heap)
    nodes = [(0, i) for i in range(num_nodes)]  # (current load, node_id)
    heapq.heapify(nodes)

    task_times = [random.randint(1, 10) for _ in range(num_tasks)]
    print("Tasks:", task_times)

    for t in task_times:
        load, node_id = heapq.heappop(nodes)
        
        # assign task ke node dengan beban terkecil
        new_load = load + t
        
        heapq.heappush(nodes, (new_load, node_id))
        
        print(f"Assign task {t} to node {node_id}, new load={new_load}")

    final_times = [load for load, _ in nodes]
    optimal_time = max(final_times)

    print("Final loads:", final_times)
    print("Expected optimal time:", optimal_time)

dynamic_distribution()