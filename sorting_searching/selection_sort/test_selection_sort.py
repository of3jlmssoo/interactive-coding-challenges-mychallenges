"""
[参照]
https://ja.wikipedia.org/wiki/%E9%81%B8%E6%8A%9E%E3%82%BD%E3%83%BC%E3%83%88

sor_iterative_altについてはdouble selection sortで代替

"""
import unittest


class SelectionSort(object):

    def sort(self, data):
        # TODO: Implement me (recursive)
        # pass
        if data is None:
            raise TypeError(f'SelectionSort.sort: arg error')

        # print(f'{data=} {len(data)=}')

        if len(data) <= 1:
            return data

        for i in range(0, len(data)):
            min = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min]:
                    min = j
            data[i], data[min] = data[min], data[i]

        return data

    def sor_iterative_alt(self, data):
        for i in range(0, len(data) // 2):
            min = i
            max = i
            l = len(data) - 1 - i
            for j in range(i + 1, len(data) - i):
                if data[j] < data[min]:
                    min = j
                if data[j] > data[max]:
                    max = j

            if i == max and l == min:
                data[i], data[l] = data[l], data[i]
            else:
                data[i], data[min] = data[min], data[i]
                data[l], data[max] = data[max], data[l]
        return data

    def sort_recursive(self, data):
        return self._sort_recursive(data, 0)

    def _sort_recursive(self, data, idx):
        if idx >= len(data):
            # print(f'1) {data=} {idx=}')
            return data

        # print(f'2) {data=} {idx=}')

        min = idx
        for j in range(idx + 1, len(data)):
            if data[j] < data[min]:
                min = j
        data[idx], data[min] = data[min], data[idx]

        return self._sort_recursive(data, idx + 1)


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self, func):
        print('None input')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_selection_sort\n')


def main():
    test = TestSelectionSort()
    selection_sort = SelectionSort()
    test.test_selection_sort(selection_sort.sort)
    try:
        test.test_selection_sort(selection_sort.sort_recursive)
        test.test_selection_sort(selection_sort.sor_iterative_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
