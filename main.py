from matplotlib import pyplot
from matplotlib import ticker


def formatter(y, pos):
    if y == 2:
        return 'AI Data'
    elif y == 1:
        return 'Test Data'
    elif y == 0:
        return 'Comparison Data'
    else:
        return ""


flag = None


def drawline(y, init_x, end_x, ok):
    global flag
    if flag is None:
        flag = ok

    color = 'g' if ok else 'r'
    pyplot.hlines(y, init_x, end_x, colors=color, linewidth=10)
    if flag != ok:
        pyplot.vlines(init_x, y + 0.2, y - 0.2, colors='b', linewidth=1)
        flag = ok


aiData = list()
testData = list()
comparisonData = list()

for i in range(100):
    aiData.append([2, i, i + 1, True if 10 < i < 40 or 60 < i < 80 else False])
for i in range(100):
    testData.append([1, i, i + 1, True if 15 < i < 25 or 30 < i < 65 else False])

for i in aiData:
    drawline(i[0], i[1], i[2], i[3])

flag = None
for i in testData:
    drawline(i[0], i[1], i[2], i[3])

flag = None
for i in range(len(aiData)):
    if aiData[i][3] is not testData[i][3]:
        drawline(0, aiData[i][1], aiData[i][2], False)
    else:
        drawline(0, aiData[i][1], aiData[i][2], True)

pyplot.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))
pyplot.show()
