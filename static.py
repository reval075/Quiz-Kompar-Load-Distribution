import random
import numpy as np

def static_uneven_distribution(num_nodes=5, threshold=0.1):
    # generate beban awal tidak merata
    loads = np.array([random.randint(10, 100) for _ in range(num_nodes)])
    print("Initial loads:", loads)

    step = 0

    while True:
        step += 1
        
        avg_load = np.mean(loads)
        
        # redistribusi sederhana
        for i in range(len(loads)):
            if loads[i] > avg_load:
                diff = (loads[i] - avg_load) * 0.5
                loads[i] -= diff
                # kirim ke node lain
                j = random.randint(0, num_nodes - 1)
                if j != i:
                    loads[j] += diff
        
        max_diff = max(loads) - min(loads)
        
        print(f"Step {step}: {loads}, diff={max_diff:.2f}")
        
        if max_diff < threshold:
            print("Ideal distribution reached")
            break

static_uneven_distribution()