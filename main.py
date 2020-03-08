import pandas
from matplotlib import pyplot, ticker

COLORS = ['#FF6666', '#AAAAAA', '#000000']


# To draw graph

def draw_line(y, intervals):
    pyplot.hlines(y, 0, len(excel_data), colors=COLORS[0 if y == 1 else 1], lw=40)  # To draw background
    for i, j in intervals:
        pyplot.hlines(y, i, j + 1, colors=COLORS[2], lw=40)


# To get data.

def get_ai_intervals(ai_list):
    index = 0
    counter = 0
    intervals = list()

    for order, data in enumerate(ai_list):
        data = 1 if data >= 0.5 else 0

        if counter > 0 and index != data:
            intervals.append([order - counter, order - 1])
            counter = 0

        if data == 1:
            index = 1
            counter += 1

        if order == len(ai_list) - 1 and counter > 0 and index == 1:
            intervals.append([order - counter + 1, order])
    return intervals


def get_test_intervals(test_list):
    index = 0
    counter = 0
    intervals = list()

    for order, data in enumerate(test_list):
        data = 1 if data == "'drone'" else 0

        if counter > 0 and index != data:
            intervals.append([order - counter, order - 1])
            counter = 0

        if data == 1:
            index = 1
            counter += 1

        if order == len(test_list) - 1 and counter > 0 and index == 1:
            intervals.append([order - counter + 1, order])
    return intervals


def get_comparision_intervals(ai_list, test_list):
    index = 0
    counter = 0
    intervals = list()

    for order, (ai_data, test_data) in enumerate(zip(ai_list, test_list)):
        x = 1 if ai_data >= 0.5 else 0
        y = 1 if test_data == "'drone'" else 0

        if counter > 0 and index != (1 if x == y else 0):
            intervals.append([order - counter, order - 1])
            counter = 0

        if x == y:
            index = 1
            counter += 1

        if order == len(test_list) - 1 and counter > 0 and index == 1:
            intervals.append([order - counter + 1, order])
    return intervals


# To show

def formatter(y, pos):
    if y == 3:
        return 'System Response'
    elif y == 2:
        return 'Test Data'
    elif y == 1:
        return 'Comparison'
    else:
        return ""


excel_data = pandas.read_excel('dataOne.xlsx')
ai = excel_data['AI'].tolist()
test = excel_data['TEST'].tolist()

draw_line(3, get_ai_intervals(ai))
draw_line(2, get_test_intervals(test))
draw_line(1, get_comparision_intervals(ai, test))

pyplot.plot(0, 0, COLORS[2], label='Drone', lw=5)
pyplot.plot(0, 0, COLORS[1], label='No Drone', lw=5)
pyplot.plot(0, 0, COLORS[0], label='Error', lw=5)

pyplot.legend(prop={'size': 20})
pyplot.yticks(fontsize=18)
pyplot.xticks(fontsize=18)

pyplot.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))
pyplot.ylim([0, 4])
pyplot.show()
