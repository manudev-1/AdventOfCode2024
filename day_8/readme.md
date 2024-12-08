
# Day 8 AdventOfCode

## Introducion

The code in the `day_8` directoy in my repository is written by [hyperneutrino](https://github.com/hyperneutrino), I didn't get what I had to do in this challenge so I searched online. Basically in this excerpt I am trying to explaing what the code does.

## Code
### First Part
-   **At the start of the challenge**, we map the positions of all antennas grouped by their frequency.
-   We initialize a `set`, which ensures that all stored positions are unique.
-   For each list of coordinates in the values of the `antennas` dictionary:
    -   We use two nested loops to iterate over all possible pairs of antennas.
    -   For each pair, we calculate the positions of the antinodes and add them to the `set`.
### Second Part
Basically the request is the same but we have to add antinodes until it reach the board of the map.
-   **At the start of the challenge**, we map the positions of all antennas grouped by their frequency.
-   We initialize a `set`, which ensures that all stored positions are unique.
-   For each list of coordinates in the values of the `antennas` dictionary:
    -   We use two nested loops to iterate over all possible pairs of antennas.
        -   If the two antennas are the same (`i == j`), we skip the pair to avoid redundant calculations.
    -   For each valid pair of antennas:
        -   Calculate the difference in rows (`dr`) and columns (`dc`) between the two antennas to determine the direction of the line.
        -   Initialize the starting position at the first antenna (`r1, c1`).
        -   Follow the direction `(dr, dc)` along the grid, adding each position to the `set` until the coordinates go out of bounds.
-   The process is repeated for all antenna frequencies to calculate all unique antinode positions.