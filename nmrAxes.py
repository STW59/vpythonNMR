from vpython import *

scene.userzoom = False
scene.camera.forward = vector(1, 0, 0)
scene.camera.up = vector(0, 0, 1)
scene.camera.pos = vector(10, 10, 10)
scene.camera.axis = vector(-10, -10, -10)

spin_length = 5
comp_rate = 100

x_pulse_vector = arrow(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), shaftwidth=0.4, color=color.yellow, visible=False)
y_pulse_vector = arrow(pos=vector(0, -10, 0), axis=vector(0, 20, 0), shaftwidth=0.4, color=color.yellow, visible=False)
b0_field = arrow(pos=vector(-5, 5, -5), axis=vector(0, 0, 15), shaftwidth=1, color=color.cyan)

scene.waitfor('click')
spin1 = arrow(pos=vector(0, 0, 0), axis=spin_length * vector(0, 0, 1), shaftwidth=0.4, color=color.red)
spin2 = arrow(pos=vector(0, 0, 0), axis=spin_length * vector(0, 0, 1), shaftwidth=0.4, color=color.green)
spin3 = arrow(pos=vector(0, 0, 0), axis=spin_length * vector(0, 0, 1), shaftwidth=0.4, color=color.blue)
spin_net = arrow(pos=vector(0, 0, 0), axis=spin1.axis + spin2.axis + spin3.axis, shaftwidth=0.4, color=color.purple)

# apply a pi/2 pulse along +x
scene.waitfor('click')
x_pulse_vector.visible = True

scene.waitfor('click')
t = 0
delta_t = 0.1
while t < 14-delta_t:
    rate(comp_rate)
    spin1.rotate(angle=radians(90/140), axis=vector(1, 0, 0), origin=vector(0, 0, 0))
    spin2.rotate(angle=radians(90/140), axis=vector(1, 0, 0), origin=vector(0, 0, 0))
    spin3.rotate(angle=radians(90/140), axis=vector(1, 0, 0), origin=vector(0, 0, 0))
    spin_net.axis = spin1.axis + spin2.axis + spin3.axis
    t += delta_t

x_pulse_vector.visible = False

# precess
scene.waitfor('click')
t = 0
delta_t = 0.1

spin1_x_fid = []
spin1_y_fid = []
spin2_x_fid = []
spin2_y_fid = []
spin3_x_fid = []
spin3_y_fid = []
spin_net_x_fid = []
spin_net_y_fid = []

while t < 2048-delta_t:
    t += delta_t
    rate(comp_rate * 50)
    spin1.rotate(angle=radians(90/180), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
    spin2.rotate(angle=radians(90/140), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
    spin3.rotate(angle=radians(90/100), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
    spin_net.axis = spin1.axis + spin2.axis + spin3.axis

    spin1_x_fid.append([t, spin1.axis.x])
    spin1_y_fid.append([t, spin1.axis.y])
    spin2_x_fid.append([t, spin2.axis.x])
    spin2_y_fid.append([t, spin2.axis.y])
    spin3_x_fid.append([t, spin3.axis.x])
    spin3_y_fid.append([t, spin3.axis.y])
    spin_net_x_fid.append([t, spin_net.axis.x])
    spin_net_y_fid.append([t, spin_net.axis.y])

plot = graph(width=640, height=400, title='Precession Beat Frequency',
             xtitle='Time', ytitle='Signal')
# f1 = gcurve(color=color.cyan, data=spin1_x_fid)
# f2 = gcurve(color=color.red, data=spin2_x_fid)
# f3 = gcurve(color=color.green, data=spin3_x_fid)
f4 = gcurve(color=color.purple, data=spin_net_x_fid)

# apply a pi pulse along +y
# scene.waitfor('click')
# y_pulse_vector.visible = True

# scene.waitfor('click')
# t = 0
# delta_t = 0.1
# while t < 28:
#     t += delta_t
#     rate(comp_rate)
#     spin1.rotate(angle=radians(90 / 140), axis=vector(0, 1, 0), origin=vector(0, 0, 0))
#     spin2.rotate(angle=radians(90 / 140), axis=vector(0, 1, 0), origin=vector(0, 0, 0))
#     spin3.rotate(angle=radians(90 / 140), axis=vector(0, 1, 0), origin=vector(0, 0, 0))
#
# y_pulse_vector.visible = False
#
# # precess
# scene.waitfor('click')
# t = 0
# delta_t = 0.1
# while t < 14-delta_t:
#     rate(comp_rate)
#     spin1.rotate(angle=radians(90 / 180), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
#     spin2.rotate(angle=radians(90 / 140), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
#     spin3.rotate(angle=radians(90 / 100), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
#     t += delta_t
