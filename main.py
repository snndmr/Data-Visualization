import pandas
from matplotlib import pyplot as plt, ticker

COLORS = ['white', 'gray', 'black']


def draw_line(y, intervals):
    plt.hlines(y, 0, len(excel_data), colors=COLORS[0 if y == 1 else 1], lw=40)  # To draw the background.
    for i, j in intervals:
        plt.hlines(y, i, j + 1, colors=COLORS[2], lw=40)


def get_intervals(data_list):  # To get data from columns.
    index = 0
    counter = 0
    intervals = list()

    for order, data in enumerate(data_list):
        data = 1 if type(data) == str and data == "'drone'" or type(data) == float and data >= 0.5 else 0

        if counter > 0 and index != data:
            intervals.append([order - counter, order - 1])
            counter = 0

        if data == 1:
            index = 1
            counter += 1

        if order == len(data_list) - 1 and counter > 0 and index == 1:
            intervals.append([order - counter + 1, order])
    return intervals


def get_comparision_intervals(ai_intervals, test_intervals):  # To compare data in AI and TEST columns.
    index = 0
    counter = 0
    intervals = list()

    for order, (ai_data, test_data) in enumerate(zip(ai_intervals, test_intervals)):
        x = 1 if ai_data >= 0.5 else 0
        y = 1 if test_data == "'drone'" else 0

        if counter > 0 and index != (1 if x == y else 0):
            intervals.append([order - counter, order - 1])
            counter = 0

        if x == y:
            index = 1
            counter += 1

        if order == len(excel_data) - 1 and counter > 0 and index == 1:
            intervals.append([order - counter + 1, order])
    return intervals


def formatter(y, pos):
    if y == 3:
        return 'System Response'
    elif y == 2:
        return 'Test Data'
    elif y == 1:
        return 'Comparison'
    else:
        return ''


excel_data = pandas.read_excel('dataOne.xlsx')
ai = excel_data['AI'].tolist()
test = excel_data['TEST'].tolist()

draw_line(3, get_intervals(ai))
draw_line(2, get_intervals(test))
draw_line(1, get_comparision_intervals(ai, test))

plt.ylim([0, 4])
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))

plt.plot(0, 0, COLORS[2], label='Drone', lw=5)
plt.plot(0, 0, COLORS[1], label='No Drone', lw=5)
plt.legend(prop={'size': 20}), plt.yticks(fontsize=18), plt.xticks(fontsize=18)

plt.show()
