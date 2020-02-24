from vpython import *

scene.userzoom = False
scene.camera.forward = vector(1, 0, 0)
scene.camera.up = vector(0, 0, 1)
scene.camera.pos = vector(10, 10, 10)
scene.camera.axis = vector(-10, -10, -10)

spin_length = 5

B0_field = arrow(pos=vector(-5, 5, -5), axis=vector(0, 0, 15), shaftwidth=1, color=color.cyan)
spin1 = arrow(pos=vector(0, 0, 0), axis=spin_length*vector(0, 0, 1), shaftwidth=0.4, color=color.red)
spin2 = arrow(pos=vector(0, 0, 0), axis=spin_length*vector(0, 0, 1), shaftwidth=0.4, color=color.green)
spin3 = arrow(pos=vector(0, 0, 0), axis=spin_length*vector(0, 0, 1), shaftwidth=0.4, color=color.blue)

# apply a pulse along +x
x_pulse_vector = arrow(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), shaftwidth=0.4, color=color.yellow)

spin1.axis = spin_length*vector(0, -1, 0)
spin2.axis = spin_length*vector(0, -1, 0)
spin3.axis = spin_length*vector(0, -1, 0)

# precession
spin1.axis = spin_length*vector(-sqrt(2)/2, -sqrt(2)/2, 0)
spin2.axis = spin_length*vector(0, -1, 0)
spin3.axis = spin_length*vector(sqrt(2)/2, -sqrt(2)/2, 0)

