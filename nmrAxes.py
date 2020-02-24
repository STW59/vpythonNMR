from vpython import *

scene.userzoom = False
scene.camera.forward = vector(1, 0, 0)
scene.camera.up = vector(0, 0, 1)
scene.camera.pos = vector(10, 10, 10)
scene.camera.axis = vector(-10, -10, -10)

B0_field = arrow(pos=vector(-5, 5, -5), axis=vector(0, 0, 15), shaftwidth=1, color=color.cyan)
spin1 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 5), shaftwidth=0.4, color=color.yellow)

x_pulse = arrow(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), shaftwidth=0.4, color=color.red)

spin2 = arrow(pos=vector(0, 0, 0), axis=vector(0, -5, 0), shaftwidth=0.4, color=color.green)
