import numpy
import matplotlib.pyplot

# back_leg_sensor_values = numpy.load("data/sinValues.npy")
# front_leg_sensor_values = numpy.load("data/cosValues.npy")
# print(back_leg_sensor_values)
#
#
# matplotlib.pyplot.plot(back_leg_sensor_values, label="Back Leg", linewidth=2)
# matplotlib.pyplot.plot(front_leg_sensor_values, label="Front leg", linewidth=0.8)
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

backLeg = numpy.load("data/backLeg.npy")
frontLeg = numpy.load("data/frontLeg.npy")
matplotlib.pyplot.plot(backLeg)
matplotlib.pyplot.plot(frontLeg)

matplotlib.pyplot.show()