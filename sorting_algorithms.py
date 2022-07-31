class SortingAlgorithms:
    """This class contains the different sorting algorithms

    @author Saúl Hdz Lara
    @version 1.0
    """

    def bubble_sort(draw_info, draw_list, ascending=True):
        """Implementation of the bubble sort algorithm

        Parameters
        ----------
        draw_info : DrawInformation class
            An instance of the class with information to draw
        draw_list : function
            A function used to draw in the window
        ascending : bool, optional
            A flag used to know how to order the numbers, by default True

        Yields
        ------
        bool
            A flag used to know if the sorting process is finished
        """
        elements = draw_info.lst

        for i in range(len(elements) - 1):
            for j in range(len(elements) - 1 - i):
                num_1 = elements[j]
                num_2 = elements[j + 1]

                if (num_1 > num_2 and ascending) or (num_1 < num_2 and not ascending):
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]
                    draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                    yield True
