import gsplat
import numpy as np

class Scene:
    def __init__(self, path):
        self.gs = gsplat.Scene(path)
        self.positions = self.gs.positions
        self.num_points = self.positions.shape[0]

        self.bmin = self.positions.min(axis=0)
        self.bmax = self.positions.max(axis=0)
        self.center = (self.bmin + self.bmax) / 2
        self.diag = np.linalg.norm(self.bmax - self.bmin)

    def info(self):
        return {
            "num_points": int(self.num_points),
            "bbox_min": self.bmin.tolist(),
            "bbox_max": self.bmax.tolist(),
            "center": self.center.tolist(),
            "diag": float(self.diag)
        }
