#!/bin/python3

import itertools


def flatlandSpaceStations(n, c):
    # Rename variables for clarity
    n_cities = n
    space_stations = c
    # Sort space stations
    space_stations.sort()
    # Find maximum distance from a city to nearest space station distances for first & last cases
    first_city_to_Station_distance = space_stations[0]
    last_station_to_city_distance = n_cities - 1 - space_stations[-1]
    # Create pairs of consecutive space stations & calculate distances between them
    if len(space_stations) == 1:
        max_city_to_station_distance = max(first_city_to_Station_distance, last_station_to_city_distance)
    else:
        station_to_station_distances = [j - i for i, j in itertools.pairwise(space_stations)]
        # Convert station-to-station distances to distances from middle cities to nearest station
        middle_cities_to_station_distances = [distance // 2 for distance in station_to_station_distances]
        # Find & return maximum distance of any city from its nearest station
        max_middle_city_to_station_distance = max(middle_cities_to_station_distances)
        max_city_to_station_distance = max(first_city_to_Station_distance, last_station_to_city_distance, max_middle_city_to_station_distance)
    return max_city_to_station_distance


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    print()
    print('OUTPUT')
    print(result)


# https://www.hackerrank.com/challenges/flatland-space-stations/problem