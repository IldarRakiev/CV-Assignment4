import numpy as np

class ExplorationAgent:
    def __init__(self, scene, resolution=5):
        self.scene = scene
        self.resolution = resolution

    def generate_viewpoints(self):
        xmin, ymin, zmin = self.scene.bmin - self.scene.diag * 0.2
        xmax, ymax, zmax = self.scene.bmax + self.scene.diag * 0.2

        xs = np.linspace(xmin, xmax, self.resolution)
        ys = np.linspace(ymin, ymax, self.resolution)
        zs = np.linspace(zmin + self.scene.diag*0.3,
                         zmax + self.scene.diag*0.3,
                         self.resolution)

        viewpoints = []
        for x in xs:
            for y in ys:
                for z in zs:
                    viewpoints.append({
                        "pos": [float(x), float(y), float(z)],
                        "look_at": self.scene.center.tolist()
                    })

        return viewpoints
