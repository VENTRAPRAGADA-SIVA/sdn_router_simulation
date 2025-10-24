# SDN Router Simulation (Mock)

This is a simplified SDN controller and topology simulator that demonstrates dynamic path selection
based on available bandwidth. It is a mock replacement for running a full Mininet/POX testbed.

## Files
- `controller.py` : Simplified controller logic that selects paths with highest minimum available bandwidth.
- `topology.json` : Mock topology describing nodes, links, and candidate paths.
- `traffic_simulator.py` : Simulates traffic by randomly changing link available bandwidth and triggering controller decisions.
- `README.md` : This file.

## How to run locally
1. Ensure Python 3.8+ is installed.
2. Run: `python traffic_simulator.py`
3. Observe controller decisions in the console output.
