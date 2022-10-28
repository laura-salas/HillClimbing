import math, random, time
import matplotlib.pyplot as plt


def draw_graph(x, y, interval=None, focus_point = None):
    """
    Draw a graph that refreshes as often as the specified interval
    :param int x: x point
    :param int y: y point
    :param int interval: in seconds, of how long should the graph refresh on
    :param int focus_point: [optional] the index of the x,y coordinate that 
should be marked
    """
    plt.title("~Laura's hill climbing~ | f(x) = cos(0.25x^2) - cos(x)")
    if not interval:
        plt.plot(x, y, 'r')

        plt.draw()
        time.sleep(9999)
    else:
        time.sleep(interval)
        if focus_point:
            plt.plot(x[focus_point], y[focus_point], 'b*' , markersize=10, 
zorder=10)
            plt.plot(x, y, 'r', zorder=0)

        else:
            plt.plot(x, y, 'r')
        plt.draw()
        plt.pause(interval)

def climb_hill(x: [int], y: [int], epsilon=None, verbose=False):
    """
    Implement hill climbing algorithm. Stops once the local maxima is found
    :param [int] x: x values
    :param [y] y: y values, equivalent to f(x) 
    :param [int] epsilon: the neighbourhood size, for instance a neighbourhood 
of
    1 will look at just the element before and after the current index.
    :param verbose : if turned on, print some useful info
    """
    if epsilon <= 0:
        print("Invalid neighbourhood size %d!" % epsilon)
        return
    if not epsilon:
        epsilon = int(0.2 * len(hills[0]))

    if verbose:
        print("epsilon: %d" % epsilon)

    chosen_x = random.randint(min(x), max(x))
    plt.ion()

    def navigate(currIdx, epsilon):
        # show current step
        draw_graph(x, y, 0.3, currIdx)

        indexes = set()
        for i in range(1, epsilon + 1):
            newIdxPos, newIdxMinus = currIdx-i, currIdx+i
            if newIdxPos > len(x)-1 or newIdxPos < 0:
                newIdxPos = currIdx
            if newIdxMinus < 0 or newIdxMinus > len(x)-1:
                newIdxMinus = currIdx

            indexes.add(newIdxMinus)
            indexes.add(newIdxPos)


        local_max = y.index(max([y[idx] for idx in indexes] + [y[currIdx]]))

        if verbose:
            print("Current index: %f, for which value is %f" % (x[currIdx], 
y[currIdx]))
            print(indexes)
            print("local max chosen: %d" % x[local_max])

        if x[local_max] == x[currIdx]:
            return x[currIdx] # we've reached local maxima
        else:
            navigate(local_max, epsilon)

    navigate(chosen_x, epsilon)
    draw_graph(x, y)

# this sets the range for x, e.g. x = [0, NUMBER_OF_POINTS]
NUMBER_OF_POINTS = 100

#  feel free to modify this function to generate the hills
hill_function = lambda x: math.cos(0.25 * (x ** 2)) - math.cos(x)


hills = [[x * 0.5, hill_function(x * 0.5)] for x in range(0, 
NUMBER_OF_POINTS+1)]
x = [elem[0] for elem in hills]
y = [elem[1] for elem in hills]
climb_hill(x,y, epsilon=1, verbose=True)
