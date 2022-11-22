import numpy
import matplotlib.pyplot

back_leg_sensor_values = numpy.load("data/backLegSensorValues.npy")
front_leg_sensor_values = numpy.load("data/frontLegSensorValues.npy")
print(back_leg_sensor_values)

matplotlib.pyplot.plot(back_leg_sensor_values, label="Back Leg", linewidth=2)
matplotlib.pyplot.plot(front_leg_sensor_values, label="Front leg", linewidth=0.8)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
