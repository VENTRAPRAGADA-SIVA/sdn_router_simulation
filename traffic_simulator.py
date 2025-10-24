import json, time, random
from controller import controller_tick, load_topology

print('Starting traffic simulator...')
# initial topology printed
topo = load_topology()
print('Initial topology:')
print(json.dumps(topo, indent=2))
# run simulation steps modifying available_bw randomly to simulate traffic
for step in range(5):
    print(f"\n--- Step {step+1} ---")
    topo = load_topology()
    # randomly reduce some link available_bw to simulate load
    for link in topo['links']:
        change = random.randint(-30, 10)
        link['available_bw'] = max(5, min(link['capacity'], link.get('available_bw', link['capacity']) + change))
    # write modified
    with open('topology.json','w') as f:
        json.dump(topo, f, indent=2)
    # run one controller tick
    controller_tick()
    time.sleep(1)
print('\nSimulation complete.')
