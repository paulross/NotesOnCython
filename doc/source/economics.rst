.. toctree::
    :maxdepth: 3

==============================================================
Economics and Software Engineering
==============================================================

Software, good software at least, evolves all the time to suit the immediate needs. That is where economics can come in. Economics seeks to explain, among other things, the consequences of allocating scarce resources to a number of demands where not all demands can be completely satisfied. Sound familiar? 

You want your software fast? Of course. You want your software now? Of course. Fortunately there are ways of doing both, just not at the same time.

Performance Measurement
---------------------------------------------

Before doing any performance tuning it is important to do some performance *measurement* first. Use every resource available to you, profilers, timing long running tasks, measuring resource usage and so on. There are a lot of tools out there but the field is incomplete so feel free to invent your own tools.

Above all treat performance measurement as a scientific experiment, one that takes great care if its conclusions are to be believed. The inverse is true too; sloppy measurement, poor test cases, poor analysis and so will doom your performance efforts.

It is a scientific experiment so budget time accordingly, more than you think and as with any scientific experiment, be open to surprises.


Example: Processing Large Binary Files.
---------------------------------------------
Here we have some Python code that is doing reasonably complex processing of binary files. The current (Python) code takes about 50 seconds to process a 1GB file. 

Python processing of a 1GB binary file: 50 seconds.

========    ==================  ===========================
Language    Est. time (s/GB)    Est. Developer time (hours)
========    ==================  ===========================
Python      50                  0
Cython      10                  4
C           2                   50
========    ==================  ===========================

We estimate that the C code will be x25 as fast: 2 seconds but th

Based on previous experience the C code will take a developer 1 week to write - say 50 hours. So how many GB of data does the software need to process for the user before it makes sense to write it in C? i.e. when does the user's benefit exceed the cost of development?



Cost/Benefit for Cython
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cost: 4 hours
The benefit must bette

4 * 3600 / (50 - 10) = 360 GB

10 users processing 

50 * 3600 / (50 - 2) = 3750 GB

100 users processing 1GB a day this pays back over about a month.





Cost: 50 hours now plus about the same in future maintenance. Say 100 hours total.
Benefit: 50 - 2 = 48 (seconds saved) x N (GB to be processed)

(100) * 3600 / (50 - 2) = 7500 GB

We have about 100 users processing about 1GB a day with this software so 7500 GB would be surpassed in around two to three months. This looks like it is worthwhile.

However if you only had one user processing 100MB/day the crossover point would be about 200 years. You are not going to see the benefit within your lifetime let alone the software's lifetime!


Python, Cython, C.

Code complexity.

Where is the cost? Now? Later?

Most "technical debt" is bullshit. Banks, ATC have soldiered on with really old software.


