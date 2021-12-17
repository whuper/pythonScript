import numpy as np

Total = 250
Number_of_users = 10
Average_score = 25
Upper_boundary = 100

probs = np.full(10, 1.0/np.float64(Number_of_users), dtype=np.float64) # probabilities

# samples to test
N = 100
k = 0
while k < N:
    q = np.random.multinomial(Total, probs)
    t = np.where(q > Upper_boundary) # check for out-of boundaries
    if np.any(t):
        print("Rejected, out of boundaries") # reject, do another sample
        continue
    # accepted
    # do something with q, print((sum(q), len(q), np.mean(q)))
    print((sum(q), len(q), np.mean(q)))

    k += 1
