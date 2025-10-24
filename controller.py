import json, time, random, logging

logger = logging.getLogger('sdn-controller')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(handler)

TOPO_FILE = "topology.json"

def load_topology():
    with open(TOPO_FILE) as f:
        return json.load(f)

def choose_path(topology, src, dst):
    # Simplified path selection: choose path with highest min available bandwidth
    candidates = topology.get("paths", {}).get(f"{src}-{dst}", [])
    best = None
    best_bw = -1
    for p in candidates:
        bw = min(link["available_bw"] for link in p["links"])
        if bw > best_bw:
            best_bw = bw
            best = p
    return best

def apply_route(path):
    logger.info(f"Applying route via links: {[l['id'] for l in path['links']]} with min_bw={min(l['available_bw'] for l in path['links'])}")

def controller_tick():
    topo = load_topology()
    # For each source-destination pair, pick best path
    for sd in topo.get("flows", []):
        src = sd["src"]
        dst = sd["dst"]
        path = choose_path(topo, src, dst)
        if path:
            apply_route(path)

if __name__ == '__main__':
    logger.info("Starting SDN controller simulation...")
    while True:
        controller_tick()
        time.sleep(2)
