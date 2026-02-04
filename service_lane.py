#!/bin/python3

def serviceLane(n, cases):
    service_lane_widths = width
    narrowest_service_lanes = []
    for case in cases:
        entry_idx = case[0]
        exit_idx = case[1]
        service_lane_widths_for_case = service_lane_widths[entry_idx: (exit_idx + 1)]
        narrowest_service_lane = min(service_lane_widths_for_case)
        narrowest_service_lanes.append(narrowest_service_lane)
    return narrowest_service_lanes


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))

    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)
    print()
    print('OUTPUT')
    print(*result, sep='\n')


# https://www.hackerrank.com/challenges/service-lane/problem