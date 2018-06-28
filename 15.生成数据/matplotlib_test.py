import matplotlib.pyplot as plt
from randomwalk import RandomWalk
from die import Die
import pygal
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)

# plt.title("Square Number", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis="both", labelsize=14)


# x_value = list(range(1, 1001))
# y_value = [x**2 for x in x_value]
# plt.scatter(x_value, y_value, c=y_value,
#             cmap=plt.cm.Blues, edgecolor="none", s=40)

# plt.axis([0, 1100, 0, 1100000])
# plt.show()
# plt.savefig("squares_plot.png", bbox_inches="tight")

# x_value = list(range(1, 6))
# y_value = [x**3 for x in x_value]
# plt.plot(x_value, y_value)

# x_value = list(range(1, 5001))
# y_value = [x**3 for x in x_value]
# plt.scatter(x_value, y_value, c=y_value,
#             cmap=plt.cm.Blues, edgecolor="none", s=40)

# plt.axis([0, 5100, 0, 130000000000])

# plt.show()

# rw = RandomWalk()
# rw.fill_walk()

# plt.figure(figsize=(10, 6))

# plt.scatter(rw.x_values, rw.y_values, s=1)
# plt.scatter(rw.x_values[0], rw.y_values[0],
#             c="green", edgecolors="none", s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1],
#             c="red", edgecolors="none", s=100)
# # plt.plot(rw.x_values, rw.y_values, linewidth=1)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

# plt.show()


# die = Die(8)
# die2 = Die(8)
# results = [die.roll() + die2.roll() for x in range(1000)]
# # print(results)
# max_result = die.num_sides + die2.num_sides
# min_result = 2
# frequencies = [results.count(x) for x in range(min_result, max_result + 1)]
# print(frequencies)

# hist = pygal.Bar()
# hist.title = "掷骰子结果分析"
# hist.x_labels = [str(x) for x in range(min_result, max_result + 1)]
# hist.x_title = "结果"
# hist.y_title = "分析结果"

hist = pygal.XY(stroke=False)
rw = RandomWalk()
rw.fill_walk()
frequencies = []
for (x, y) in zip(rw.x_values, rw.y_values):
    frequencies.append((x, y))
hist.add("data", frequencies)
hist.render_to_file("die_visual.svg")


#plt.figure(figsize=(10, 6))

# plt.scatter(list(range(min_result, max_result + 1)), frequencies, s=50)
# plt.plot(list(range(min_result, max_result + 1)), frequencies, linewidth=5)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

plt.show()
