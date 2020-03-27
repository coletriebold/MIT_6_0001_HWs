###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import csv
import numpy as np

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def dict_builder(file_line):
    key_list = []
    j = 0
    
    key_list = file_line.split(",")
    key = key_list[0]
    value = int(key_list[1])
    return (key, value)


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #file = 'ps1.cow_data.txt'
    file = filename
    cow_dict = {}
    with open(file) as fh:
        #rd = csv.DictReader(fh, delimiter=',')
        for i in fh:
            rd = fh.readline()
            [key, value] = dict_builder(rd)
            cow_dict[key] = value
    return cow_dict

# Problem 2
def dict_sort(dict_in):
    val_list = []
    key_list = []
    val_sorted = []
    key_sorted = []
    sorted_list = []
    sorted_list
    for key in dict_in:
        key_list.append(key)
        val_list.append(dict_in[key])
    while len(key_list)>0:
        max_val = max(val_list)
        max_index = val_list.index(max_val)
        val_sorted.append(max_val)
        key_sorted.append(key_list[max_index])
        val_list.pop(max_index)
        key_list.pop(max_index)
    return(key_sorted, val_sorted)

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trip_list = []
    trip_list_big = []
    cow_dict = cows.copy()
    (key_sorted, val_sorted) = dict_sort(cow_dict)
    for i in range(0,len(val_sorted)):
        if val_sorted[i] <= limit:
            limit -= cow_dict[key_sorted[i]]
            trip_list.append(key_sorted[i])
            cow_dict.pop(key_sorted[i])
    trip_list_big.append(trip_list)
    if len(cow_dict) > 0:
        trip_list_big.extend(greedy_cow_transport(cow_dict, limit=10))
    return trip_list_big
    
# Problem 3

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_list  = []
    cow_dict = cows.copy()
    partition_dict = {}
    best_cow_points = len(cow_dict)
    flag = 0
    for cow in cows:
        cow_list.append(cow)
    cow_parts = get_partitions(cow_list)
    for cow_partition in cow_parts:
        cow_len = len(cow_partition)
        partition_dict[cow_len] = cow_partition
        for cow_set in cow_partition:
            new_dict = {}
            for cows in cow_set:
                
                cow_val = cow_dict[cows]
                new_dict[cows] = cow_val
            transport_list =  greedy_cow_transport(new_dict,limit)
            if len(transport_list) > 1:
                flag = 1
        if flag == 0:
            cow_points = cow_len
        else:
            flag = 0
            cow_points = len(cow_dict)
        if cow_points < best_cow_points:
            best_cow_points = cow_points
            best_cow_list = cow_partition
    return best_cow_list
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    optimal_trip = brute_force_cow_transport(load_cows('ps1_cow_data.txt'),limit=10)
    end = time.time()
    print('Brute force took {} to finish'.format(end-start))
    print('There were {} trips'.format(len(optimal_trip)))
    
    start = time.time()
    optimal_trip2 = greedy_cow_transport(load_cows('ps1_cow_data.txt'),limit=10)
    end = time.time()
    print('Greedy cow transport took {} to finish'.format(end-start))
    print('There were {} trips'.format(len(optimal_trip2)))
    pass
