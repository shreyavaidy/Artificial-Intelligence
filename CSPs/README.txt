*******************************************************************************
*******************************************************************************
ARTIFICIAL INTELLIGENCE Spring 2018
Homework4: CSPs
*******************************************************************************
Author: SHREYA VAIDYANATHAN
UNI: sv2525
*******************************************************************************
*******************************************************************************


RESULTS:
************
Example of the results for the the first 60 boards when I run "python3 driver_3.py" is as follows where the number denotes line number and the time is displayed in seconds-

"
Running all from sudokus_start
1 Running_time: 0.00000000
2 Running_time: 0.00000000
3 Running_time: 23.22563505
4 Running_time: 24.91526937
5 Running_time: 64.88114834
6 Running_time: 34.78776455
7 Running_time: 1.55010152
8 Running_time: 94.50922966
9 Running_time: 38.38330436
9 Running_time: 38.38330436
10 Running_time: 85.9483015
11 Running_time: 3.90377665
12 Running_time: 6.67874861
13 Running_time: 13.97894454
14 Running_time: 41.12824893
15 Running_time: 3.06718326
16 Running_time: 14.95463896
17 Running_time: 26.91616201
18 Running_time: 0.67247176
19 Running_time: 23.81796432
20 Running_time: 5.68904686
21 Running_time: 3.01813698
22 Running_time: 3.88878226
23 Running_time: 9.71390939
24 Running_time: 3.20328450
25 Running_time: 1.00471377
26 Running_time: 7.51832676
27 Running_time: 23.05539322
28 Running_time: 3.52951121
29 Running_time: 19.04254580
30 Running_time: 10.5477986
31 Running_time: 37.89793611
32 Running_time: 1.36799240
33 Running_time: 31.63050485
34 Running_time: 40.44176459
35 Running_time: 3.18126345
36 Running_time: 3.28734899
37 Running_time: 53.76724720
38 Running_time: 4.31906390
39 Running_time: 8.64715219
40 Running_time: 0.53838253
41 Running_time: 0.74652863
42 Running_time: 19.11259341
43 Running_time: 3.83772278
44 Running_time: 0.40528917
45 Running_time: 1.30891395
46 Running_time: 20.41252017
47 Running_time: 5.00155258
48 Running_time: 3.13323116
49 Running_time: 9.15751219
50 Running_time: 2.07647634
51 Running_time: 7.17212057
52 Running_time: 22.36791372
53 Running_time: 1.21684504
54 Running_time: 9.37969017
55 Running_time: 13.71375418
56 Running_time: 23.18749571
57 Running_time: 9.18452978
58 Running_time: 7.43528676
59 Running_time: 1.75024223
60 Running_time: 1.54011297
"


OBSERVATIONS:
*************
- Number of boards that I could solve from sudokus_start.txt - All

- Running Time: Varies from 0.00seconds to 50 seconds or so
- Some boards in line 5,8,9,10 etc. took slightly more than 60 seconds on running to finish. I am not sure how it sometimes runs a few seconds faster perhaps because of the heuristic I am using to tune the unassigned values.

- The hardest board '800000000003600000070090200050007000000045700000100030001000068008500010090000400' (also solved) took "Running_time: 404.95847678" to solve!

- So I was able to observe that the algorithm eliminates minimum remaining values more slowly and then tries to do forward feed in order to get the domains that are not assigned for the remaining values and so on.

