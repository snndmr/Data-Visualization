import pandas
from matplotlib import pyplot, ticker

excel_data_df = pandas.read_excel('dataTwo.xlsx')


# To draw graph

def formatter(y, pos):
    if y == 2:
        return 'System Response'
    elif y == 1:
        return 'Test Data'
    elif y == 0:
        return 'Comparison'
    else:
        return ""


def draw_background(y, init, end):
    pyplot.hlines(y, init, end, colors='gray', lw=40)


def draw_detected(y, init, end):
    pyplot.hlines(y, init, end, colors='black', lw=40)


# To assign data.

flag = False
temp = 0

AI = list()
TEST = list()
COMP = list()

for order, i in enumerate(excel_data_df['AI'].tolist()):
    if i >= 0.5 and flag is False:
        temp = order
        flag = True
    elif i < 0.5 and flag is True:
        AI.append([temp, order])
        flag = False

for order, i in enumerate(excel_data_df['TEST'].tolist()):
    if i == "'drone'" and flag is False:
        temp = order
        flag = True
    elif i != "'drone'" and flag is True:
        TEST.append([temp, order])
        flag = False

draw_background(2, 0, len(excel_data_df['AI'].tolist()))
for i, j in AI:
    draw_detected(2, i, j)

draw_background(1, 0, len(excel_data_df['TEST'].tolist()))
for i, j in TEST:
    draw_detected(1, i, j)

for order, (i, j) in enumerate(zip(excel_data_df['AI'].tolist(), excel_data_df['TEST'].tolist())):
    x = 0
    y = 0
    x = 1 if i >= 0.5 else 0
    y = 1 if j == "'drone'" else 0

    if x == y and flag is False:
        temp = order
        flag = True
    elif x != y and flag is True:
        COMP.append([temp, order])
        flag = False
COMP.append([temp, len(excel_data_df['TEST'].tolist())])

for i, j in COMP:
    draw_detected(0, i, j)

pyplot.plot(0, 0, 'black', label='Drone', lw=5)
pyplot.plot(0, 0, 'gray', label='No Drone', lw=5)

pyplot.legend(prop={'size': 20})
pyplot.yticks(fontsize=18)
pyplot.xticks(fontsize=18)
pyplot.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))
pyplot.ylim([-1, 3])
pyplot.show()