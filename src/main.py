import argparse
from scene_loader import Scene
from explorer import ExplorationAgent
import json
import os

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def run_scene_understanding(args):
    scene = Scene(args.scene)
    print("Loaded scene info:", scene.info())

    agent = ExplorationAgent(scene, resolution=4)
    vps = agent.generate_viewpoints()
    print(f"Generated {len(vps)} exploration viewpoints.")

    os.makedirs(args.output, exist_ok=True)
    save_json(f"{args.output}/viewpoints.json", vps)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", type=str)
    parser.add_argument("--phase", type=str, default="scene")
    parser.add_argument("--output", type=str, default="outputs")

    args = parser.parse_args()

    if args.phase == "scene":
        run_scene_understanding(args)

if __name__ == "__main__":
    main()
