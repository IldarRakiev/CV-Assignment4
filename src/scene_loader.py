# src/scene_loader.py
import gsplat
import numpy as np

class Scene:
    def __init__(self, path):
        self.scene_path = path
        self.data = gsplat.load(path)
        self.positions = np.array(self.data['positions'])

        if self.positions.shape[0] == 0:
            raise ValueError(f"PLY file {path} is empty!")

        self.bmin = self.positions.min(axis=0)
        self.bmax = self.positions.max(axis=0)
        self.center = (self.bmin + self.bmax) / 2
        self.diag = np.linalg.norm(self.bmax - self.bmin)

    def info(self):
        return {
            "num_points": int(self.positions.shape[0]),
            "bbox_min": self.bmin.tolist(),
            "bbox_max": self.bmax.tolist(),
            "center": self.center.tolist(),
            "diag": float(self.diag)
        }
