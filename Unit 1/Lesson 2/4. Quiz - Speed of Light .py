# Write Python code that stores the distance
# in meters that light travels in one
# nanosecond in the variable, nano-distance.
# These variables are defined for you:
# After your code, running the following:
# print nanodistance
# should output: 0.2998
# Note that nanodistance must be a decimal number.
# ASSIGN nanodistance BELOW this line

speed_of_light = 299800000.     # meters per second
nano_per_sec = 1000000000.      # 1 billion

nanodistance = speed_of_light/nano_per_sec
print (nanodistance)