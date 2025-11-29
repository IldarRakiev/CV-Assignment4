import numpy as np
import open3d as o3d

class Scene:
    def __init__(self, path):
        self.path = path
        self.pcd = o3d.io.read_point_cloud(path)
        self.points = np.asarray(self.pcd.points)

        self.bmin = self.points.min(axis=0)
        self.bmax = self.points.max(axis=0)
        self.center = (self.bmin + self.bmax) / 2
        self.diag = np.linalg.norm(self.bmax - self.bmin)

    def info(self):
        return {
            "num_points": len(self.points),
            "bbox_min": self.bmin.tolist(),
            "bbox_max": self.bmax.tolist(),
            "center": self.center.tolist(),
            "diag": float(self.diag)
        }
