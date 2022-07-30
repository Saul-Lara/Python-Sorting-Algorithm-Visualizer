class SortingAlgorithms:
    def bubble_sort(draw_info, draw_list, ascending=True):
        elements = draw_info.lst

        for i in range(len(elements) - 1):
            for j in range(len(elements) - 1 - i):
                num_1 = elements[j]
                num_2 = elements[j + 1]

                if (num_1 > num_2 and ascending) or (num_1 < num_2 and not ascending):
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]
                    draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                    yield True
        return elements
