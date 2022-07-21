from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    total = 0
    time = 0
    while truck_weights:
      time += 1
      k = bridge.popleft()

      if k :
        total -= k

      if total + truck_weights[0] <= weight:
        bridge.append(truck_weights.popleft())
        total += bridge[-1]
      else:
        bridge.append(0)
    
    time += len(bridge)
    return time