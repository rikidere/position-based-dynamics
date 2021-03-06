import taichi as ti

from src.Simulation import Simulation
from src.objects.Box import Box
from src.objects.Sphere import Sphere
from src.objects.Plane import Plane
from src.clothes.GridCloth import GridCloth

sim = Simulation("test", res=(1600, 900), dt=0.005,MODE=ti.cpu, iterations=5, rotateCamera=50)
sim.set_camera((-1.6, 1.6, 0.5), (0, 0, 0))
sim.add_light((-0.1, -0.1, 1), (1, 1, 1))

c = GridCloth(N=(32, 32), W = 100, S=(0.5, 0.5), KS=0.95  , KB=0.05, KC=1, center=ti.Vector([0, 0, 0.01]))
sim.add_cloth(c)

b = Box(ti.Vector([0, 0, -0.2]), ti.Vector([0.4, 0.4, 0.4]), color=(0, 0, 0.7))
#sim.add_object(b)

s = Sphere(ti.Vector([0.1, 0.2, -0.11]), 0.1, color=(1, 0, 0))
sim.add_object(s)

s = Sphere(ti.Vector([0, -0.1, -0.11]), 0.1, color=(1, 0, 0))
sim.add_object(s)

p = Plane(center=ti.Vector([0, 0, -0.5]), color=(0.2, 0.2, 0.2))
sim.add_object(p)

sim.make_video("self_collision3")
sim.run()