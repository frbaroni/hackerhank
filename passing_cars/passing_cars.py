def solution(A):
    cars = 0
    passed = 0
    for car in reversed(A):
        cars += car
        if car == 0:
            passed += cars
            if passed > 1000000000:
                return -1
    return passed
