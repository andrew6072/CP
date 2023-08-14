'''
2 10 10
1st: 0 left: time 0 there's 1st car at left bank, then PICKS right: +10, NOW 10 right (1st: 10)
2nd: 10 left: time 10 there's 2nd car at left bank, then MOVES left: +10, NOW 20 left
3rd: 20 left: time 20 on left bank there are 2 cars 2nd, 3rd, then PICKS right: +10, NOW 30 right (2nd, 3rd: 30)
4th: 30 left: time 30 on left bank there's 4th car, then MOVES left:+10, NOW 40 left
5th: 40 left: time 40 PICKS 4th, 5th right:+10, NOW 50 right (4th,5th:50), there's 6th at left, then MOVES left:+10, NOW 60 left
6th: 50 left:
7th: 60 left: time 60 PICKS 6th, 7th right:+10, NOW 70 right (6th,7th:70), there's 8th at left, then MOVES left:+10, NOW 80 left
8th: 70 left:
9th: 80 left: time 80 PICKS 8th, 9th right:+10, NOW 90 right (8th,9th:90), there's 10th at left, then MOVES left:+10, NOW 100 left
10th: 90 left: time 100 PICKS 10th right:+10, NOW 110 right (10th:110)

Expected output:
10
30
30
50
50
70
70
90
90
110


2 10 3
1st: 10 right
2nd: 25 left
3rd: 40 left

time 0 no cars
time 10 3rd at right, MOVES right:+10, NOW 20 right
time 20 PICKS 1st left:+10, NOW 30 left (1st:30left), 30>25 then PICKS 2nd right:+10, NOW 40 right (2nd:40right)
time 40>=40 then MOVES left:+10, NOW 50>=40 left, then PICKS 3rd right:+10, NOW 60 right (3rd:60right)

Expected output:
30
40
60

'''
import queue

class FerryStatus(object):
    def __init__(self, time, where):
        self.time = time
        self.where = where
    def __repr__(self):
        return f'({self.time}, {self.where})'


class MyQueue(queue.Queue):
    def __repr__(self):
        items = list(self.queue)
        return f'{items}'


def move(t, ferry, where):
    ferry.time += t
    ferry.where = where


def oppositeBank(which_bank):
    if which_bank == 'left':
        return 'right'
    elif which_bank == 'right':
        return 'left'
    else:
        print('Input must be "left" or "right"')
        return which_bank


def operate(ans, n, t, ferry, bank, where, opposite_bank):
    if not bank.empty() and bank.queue[0][1] <= ferry.time:
        count = 1
        while count <= n and not bank.empty() and bank.queue[0][1] <= ferry.time:
            car = bank.get()
            ans[car[0]] = ferry.time + t
            count += 1
        move(t, ferry, oppositeBank(where))

    elif not bank.empty() and bank.queue[0][1] > ferry.time:  # The time when there's no cars in both 2 banks, update time
        car_time_left = bank.queue[0][1]
        car_time_right = 10 ** 9
        if not opposite_bank.empty():
            car_time_right = opposite_bank.queue[0][1]

        if car_time_left < car_time_right:
            ferry.time = car_time_left
        else:
            move(t, ferry, oppositeBank(where))

    else:  # this bank is empty
        move(t, ferry, oppositeBank(where))


def printAns(ans):
    for a in ans:
        print(a)


def solve():
    n, t, m = map(int, input().split())

    left_bank = MyQueue()
    right_bank = MyQueue()

    ans = [0 for _ in range(m)]

    min_car_time_left = 10**9
    min_car_time_right = 10**9
    for i in range(m):
        car_time, which_bank = input().split()
        car_time = int(car_time)
        if which_bank == 'left':
            min_car_time_left = min(min_car_time_left, car_time)
            left_bank.put((i, car_time))
        else:
            min_car_time_right = min(min_car_time_right, car_time)
            right_bank.put((i, car_time))

    ferry = FerryStatus(min(min_car_time_left, min_car_time_right), 'left')

    while (not left_bank.empty()) or (not right_bank.empty()):
        if ferry.where == 'left':
            operate(ans, n, t, ferry, left_bank, 'left', right_bank)
        else:
            operate(ans, n, t, ferry, right_bank, 'right', left_bank)

    return ans


tc = int(input())
for i in range(tc):
    ans = solve()
    printAns(ans)
    if i != tc-1:
        print()
