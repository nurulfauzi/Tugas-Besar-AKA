import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random
import time

def swap(Z, i, j):
    """Helper function to swap elements i and j of list X."""

    if i != j:
        Z[i], Z[j] = Z[j], Z[i]

def bubble_sort(Z):
    """In-place bubble sort."""
    if len(Z) == 1:
        return
    bertukar = True
    for i in range(len(Z) - 1):
        if not bertukar:
            break
        bertukar = False
        for j in range(len(Z) - 1 - i):
            if Z[j] > Z[j + 1]:
                swap(Z, j, j + 1)
                bertukar = True
            yield Z

def merge_sort(Z, awal, akhir):
    """Merge sort."""

    if akhir <= awal:
        return
    mid = awal + ((akhir - awal + 1) // 2) - 1
    yield from merge_sort(Z, awal, mid)
    yield from merge_sort(Z, mid + 1, akhir)
    yield from merge(Z, awal, mid, akhir)
    yield Z

def merge(Z, awal, mid, akhir):
    """Helper function for merge sort."""
    
    merged = []
    leftIdx = awal
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= akhir:
        if Z[leftIdx] < Z[rightIdx]:
            merged.append(Z[leftIdx])
            leftIdx += 1
        else:
            merged.append(Z[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(Z[leftIdx])
        leftIdx += 1

    while rightIdx <= akhir:
        merged.append(Z[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        Z[awal + i] = sorted_val
        yield Z

if __name__ == "__main__":
    N = int(input("Input Jumlah Array dalam bilangan Bulat: "))
    method_msg = "Pilih Sorting yang ingin digunakan :\n(b)ubble\n(m)erge\n"
    method = input(method_msg)

    Z = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(Z)

    if method == "b":
        title = "Bubble sort"
        generator = bubble_sort(Z)
    else:
        title = "Merge sort"
        generator = merge_sort(Z, 0, N - 1)

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(Z)), Z, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.0 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    
    def update_fig(Z, rects, iteration):
        for rect, val in zip(rects, Z):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("Iterasi: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()
