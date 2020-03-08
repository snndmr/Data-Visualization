import pandas
from matplotlib import pyplot, ticker

COLORS = ['#AAAAAA', '#979797', '#848484', '#717171', '#5E5E5E', '#4C4C4C', '#393939', '#262626', '#131313', '#000000']

ai = pandas.read_excel('one.xlsx')['AI'].tolist()
test = pandas.read_excel('test.xlsx')['TEST'].tolist()


def formatter(y, pos):
    if y == 4:
        return 'AI B2G'
    elif y == 3:
        return 'AI B&G'
    elif y == 2:
        return 'Test B&G'
    elif y == 1:
        return 'Comparision B&G'
    else:
        return ""


def get_intervals(ai_list):
    index = 0
    counter = 0
    intervals = list()

    for _ in range(10):
        intervals.append(list())

    for order, data in enumerate(ai_list):
        if counter > 0 and not (index <= data * 10 <= index + 1):
            intervals[index].append([order - counter, order - 1])
            counter = 0

        if 0.9 <= data <= 1:
            index = 9
            counter += 1
        elif 0.8 <= data < 0.9:
            index = 8
            counter += 1
        elif 0.7 <= data < 0.8:
            index = 7
            counter += 1
        elif 0.6 <= data < 0.7:
            index = 6
            counter += 1
        elif 0.5 <= data < 0.6:
            index = 5
            counter += 1
        elif 0.4 <= data < 0.5:
            index = 4
            counter += 1
        elif 0.3 <= data < 0.4:
            index = 3
            counter += 1
        elif 0.2 <= data < 0.3:
            index = 2
            counter += 1
        elif 0.1 <= data < 0.2:
            index = 1
            counter += 1
        elif 0 <= data < 0.1:
            index = 0
            counter += 1

        if order == len(ai_list) - 1 and counter > 0:
            intervals[index].append([order - counter, order - 1])
    return intervals


def get_test_intervals(test_list):
    index = 0
    counter = 0
    intervals = list()

    for _ in range(2):
        intervals.append(list())

    for order, data in enumerate(test_list):
        data = 1 if data == "'drone'" else 0

        if counter > 0 and index != data:
            intervals[index].append([order - counter, order - 1])
            counter = 0

        if data == 1:
            index = 1
            counter += 1
        else:
            index = 0
            counter += 1

        if order == len(test_list) - 1 and counter > 0:
            intervals[index].append([order - counter, order - 1])
    return intervals


def get_comparision_intervals(ai_list, test_list):
    index = 0
    counter = 0
    intervals = list()

    for _ in range(2):
        intervals.append(list())

    for order, (ai_data, test_data) in enumerate(zip(ai_list, test_list)):
        x = 1 if ai_data >= 0.5 else 0
        y = 1 if test_data == "'drone'" else 0

        if counter > 0 and x == y and index != 1:
            intervals[index].append([order - counter, order - 1])
            counter = 0
        elif counter > 0 and x != y and index != 0:
            intervals[index].append([order - counter, order - 1])
            counter = 0

        if x != y:
            index = 1
            counter += 1
        else:
            index = 0
            counter += 1

        if order == len(test_list) - 1 and counter > 0:
            intervals[index].append([order - counter, order - 1])
    return intervals


def display_ai_intervals(ai_list):
    for order, data in enumerate(get_intervals(ai_list)):
        print("{:.1f} - {:.1f}  |  Size : {:3}  |  {}".format(order / 10, (order + 1) / 10, len(data), data))


def draw_intervals_black2gray(y, intervals):
    for index in range(len(intervals)):
        for j in intervals[index]:
            pyplot.hlines(y, j[0], j[1] + 1, colors=COLORS[index], lw=50)


def draw_intervals_black_gray(y, intervals):
    for index in range(len(intervals)):
        if index < len(intervals) / 2:
            for j in intervals[index]:
                pyplot.hlines(y, j[0], j[1] + 1, colors='gray', lw=50)
        else:
            for j in intervals[index]:
                pyplot.hlines(y, j[0], j[1] + 1, colors='black', lw=50)


# for i in range(len(COLORS)):
#     pyplot.plot(0, 0, color=COLORS[i], label=(i / 10, (i + 1) / 10), lw=5)
#
# pyplot.legend(prop={'size': 16})
# pyplot.yticks(fontsize=18)
# pyplot.xticks(fontsize=18)
# pyplot.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))
#
# for i in range(1, 5):
#     pyplot.hlines(i, 0, len(ai), colors=COLORS[5], lw=50)
#
# draw_intervals_black2gray(4, get_intervals(ai))
# draw_intervals_black_gray(3, get_intervals(ai))
# draw_intervals_black_gray(2, get_test_intervals(test))
# draw_intervals_black_gray(1, get_comparision_intervals(ai, test))
#
# pyplot.ylim([0, 5])
# pyplot.xlim([-1500, len(ai) + 1500])
# pyplot.show()
display_ai_intervals(ai)
