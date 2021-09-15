"""
https://ja.wikipedia.org/wiki/%E9%81%B8%E6%8A%9E%E3%82%BD%E3%83%BC%E3%83%88

            0 1 2 3 4 5 6 7
初期データ: 8 4 3 7 6 5 2 1　
太字はソート完了した部分
 1 4 3 7 6 5 2 8 （1回目のループ終了時）
[1 4 3 7 6 5 2 8]

 1 2 3 7 6 5 4 8 （2回目のループ終了時）
[1 2 3 7 6 5 4 8]

 1 2 3 7 6 5 4 8 （3回目のループ終了時）
[1 2 3 7 6 5 4 8]

 1 2 3 4 6 5 7 8 （4回目のループ終了時）
[1 2 3 4 6 5 7 8]

 1 2 3 4 5 6 7 8 （5回目のループ終了時）
[1 2 3 4 5 6 7 8]

この例では、一見して、この時点で既にソート完了したとわかる。しかしデータが多数の場合はそうはいかないし、アルゴリズムで「一見して」ソート完了か否か判断できない。アルゴリズム通りに最後まで処理する必要がある。
 1 2 3 4 5 6 7 8 （6回目のループ終了時）
[1 2 3 4 5 6 7 8]

 1 2 3 4 5 6 7 8 （7回目のループ終了時）
[1 2 3 4 5 6 7 8]

[1 2 3 4 5 6 7 8]
[1 2 3 4 5 6 7 8]

for I := 1 to N
  min := I
  for J := I+1 to N
    if data[J] < data[min] then
      min := J
    end if
  end for
  swap(data[I], data[min])
end for

"""
data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
# data = [8, 4, 3, 7, 6, 5, 2, 1]
"""
for i in range(0,len(data)):
  min = i
  for j in range(i+1,len(data)):
    if data[j] < data[min]:
      min = j
  data[i], data[min] = data[min], data[i]
  print(data)
print(data)
"""


def selection_sort(data, idx):
    if idx >= len(data):
        print(f'1) {data=} {idx=}')
        return data

    print(f'2) {data=} {idx=}')

    min = idx
    for j in range(idx + 1, len(data)):
        if data[j] < data[min]:
            min = j
    data[idx], data[min] = data[min], data[idx]

    return selection_sort(data, idx + 1)


print(selection_sort(data, 0))
