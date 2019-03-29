# Exercise I
Add your answers to the Algorithms exercises here...

* a) O(n)
    * only 1 loop of iterations, even though multiple math calculations are done per iteration making it still (n)

* b) O(n^3 (?) * (10 * (0.97xxxxxx)))
    * because if (n = 100)...
        * O(n^2) -> 4951
        * O(n^3) -> 157047
        * O(n^3 (?) * (10 * (0.97xxxxxx))) ---> <1525911>
        * O(n^4) -> 3621887
    * and if (n = 1000)...
        * O(n^2) -> 499501
        * O(n^3) -> 165670497
        * O(n^3 (?) * (10 * (0.97xxxxxx))) -> 1652209461

* c)
* input of 0 bunnies = O(1)
* input bunnies greater than 0 = O(n)
    * function is being called recursively n times before reaching base case so its O(n), often called linear. The `2 +` will not be added until the recursion loops back through the call stack, which will then give the total sum at the end.

# Exercise II
## Problem:
* give a solution that uses the least possible eggs to find the final safe floor

## constraints:
* assume plenty of eggs for testing drops per floor
* n floors (sorted array between 1 and n)
* there are no 0 floors, floor starts at 1,
    * return error message if n is <= 0
    * if egg breaks at floor 1, return message saying "there are no safe floors"
* safe floors (eggs dropped but not broken)
* not safe floors (eggs dropped and broken)
* Find the last floor where it is safe to drop eggs without getting broken

## unanswered questions:
1. How do I tell if dropping an egg from 1 floor will break or not break. Will this function be given to me?
    * Assume function will be given to change egg is_broken status
2. Is the result of dropping the egg from the same floor consistent or random with higher % chances based on the floor level?
    * Assume the result is constant

## solution: simular to binary search O(log n)
* Psudo code
* egg is an object:
    * initialize with boolean status is_broken = False
    * egg method is_broken() returns status boolean
* assuming question 2 is constant
* because the array floors is sorted, we can
    * loop starting in middle of each half of
    * the floors array
```


drop_egg(f):
    # Assuming from question 1 - unknown function body
    # after running this function, I can check egg status
    #    and see if the status is_broken == True

is_egg_dropped_broken(f):
    # returns true or false
    drop_egg(f)
    return egg.is_broken()

get_final_safe_floor(floors):
    # Edge case length of floors <= 0
    if len(floors) <= 0:
        return "invalid input of number of floors"

    f_i = len(floors) // 2
    f_not_broken = 0
    if is_egg_dropped_broken(floors[f_i]):
        half_floors = floors[:f_i]
        f_i = len(floors) // 2
    else:
        f_not_broken = floors[f_i]
        half_floors = floors[f_i:]
        f_i = len(floors) // 2

    while len(half_floors) > 1:
        if is_egg_dropped_broken(floors[f_i]):
            half_floors = floors[:f_i]
            f_i = len(floors) // 2
        else:
            f_not_broken = floors[f_i]
            half_floors = floors[f_i:]
            f_i = len(floors) // 2

    if f_not_broken == 0:
        if not is_egg_dropped_broken(floors[f_i]):
            return floors[f_i]
        else:
            return "there are no safe floors"
    return floors[f_i]


```

## Use Cases
* `[1,2,3,4,5,6,7,8,9,10]`, break = 8, f_in_check = 6
    * `[6,7,8,9,10]`, f_in_check = 8
    * `[6,7]`, f_in_check = 7, f_not_broken = 7
    * `[7]`, return `[7]`
* `[1,2,3,4,5,6,7,8,9,10]`, break = 9, f_in_check = 6
    * `[6,7,8,9,10]`, f_in_check = 8, f_not_broken = 8
    * `[8,9,10]`, f_in_check = 9, f_broken = 9
    * `[8]`, return `[8]`
* `[1,2,3,4,5,6,7,8,9,10]`, break = 2, f_in_check = 6
    * `[1,2,3,4,5]`, f_in_check = 3, f_broken = 3
    * `[1,2]`, f_in_check = 2, f_broken = 2
    * `[1]`,
        ```
        if f_not_broken == 0:
            if [1] is not safe:
                return "no safe floors"
            else:
                return [1] # <-----------
        else:
            return [1]
        ```
* `[1,2,3,4,5,6,7,8,9,10]`, break = 3, f_in_check = 6
    * `[1,2,3,4,5]`, f_in_check = 3, f_broken = 3
    * `[1,2]`, f_in_check = 2, f_not_broken = 2
    * `[2]`,
        ```
        if f_not_broken == 0:
            if [2] is not safe:
                return "no safe floors"
            else:
                return [2]
        else:
            return [2] # <----------
        ```