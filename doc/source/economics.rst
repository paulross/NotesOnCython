.. toctree::
    :maxdepth: 3

==============================================================
Software Engineering and Economics
==============================================================

It is misleading to look at a software project at a particular point in time, good software at least evolves to suit the needs of the time and that is where Economics can come in. Economics seeks to explain, among other things, the consequences of allocating scarce resources to a number of demands where not all demands can be satisfied. Sound familiar? 

You want your software fast? Of course. You want your software now? Of course. Fortunately there are ways of doing both, just not at the same time.

Before doing any performance tuning it is important to do some performance *measurement* otherwise 

Example 1 - Optimising an XML Writer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A large amount of data is sent through a set of Python classes that write XML. These classes ensure that the XML is well formed and handle all the encoding of the content.

Profiling reveals that these output classes are the the bottleneck. Can Cython help?

We estimate that Cython can gives about x5 speedup  

Developer cost of Cython'sing the code: 1 day
Benefit: 

Example 2 - Processing Large Binary Files.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we have some Python code that is doing reasonably complex processing of binday files.

Python processing of a 1GB binary file: 50 seconds.

We estimate that the C code will be x25 as fast: 2 seconds.

Based on previous experience the C code will take a developer 1 week to write - say 50 hours. So how many GB of data does the software need to process for the user before it makes sense to write it in C? i.e. when does the user's benefit exceed the cost of development?

Cost: 50 hours now plus about the same in future maintenance. Say 100 hours total.
Benefit: 50 - 2 = 48 (seconds saved) x N (GB to be processed)

(100) * 3600 / (50 - 2) = 7500 GB

We have about 100 users processing about 1GB a day with this software so 7500 GB would be surpassed in around two to three months. This looks like it is worthwhile.

However if you only had one user processing 100MB/day the crossover point would be about 200 years. You are not going to see the benefit within your lifetime let alone the software's lifetime!


Python, Cython, C.

Code complexity.

Where is the cost? Now? Later?

Most "technical debt" is bullshit. Banks, ATC have soldiered on with really old software.


