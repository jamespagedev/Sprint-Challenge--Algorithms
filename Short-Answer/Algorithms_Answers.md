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
