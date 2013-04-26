% Introduction to MapReduce with Hadoop on Linux
% Adam Monsen
% April 28, 2013

# Welcome!

<!--
Conference: LinuxFest Northwest 2013
Target audience experience level: intermediate
-->

- this is the Hadoop talk
- see my article in the [April 2013 issue of Linux Journal](http://www.linuxjournal.com/content/april-2013-issue-linux-journal-high-performance-computing)
- thank you BLUG and LFNW
- please donate to support this conference

# How do you scale when you must?

# Bigger hardware

> In pioneer days they used oxen for heavy pulling, and when one ox couldn't
> budge a log, they didn't try to grow a larger ox. We shouldn't be trying for
> bigger computers, but for more systems of computers. --Grace Hopper

# Try "smarter"

- say we're at the limits of our hardware
- how do we "throw more hardware" at our problem?

# Scale out

- scaling _out_ is hard
    - partitioning
    - communication
    - synchronization
    - hardware failure
    - different paradigms ("process" vs. "job")
    - hardest part is making the above easy

# Hadoop and MapReduce

- MapReduce provides a pattern to scale **big**
- Hadoop provides an implementation of MapReduce

# Diagram: MapReduce overview

![MapReduce diagram](Mapreduce_Overview.svg)\ 

<div class="handout">
The above diagram is a [work of Wikipedia user Poposhka](http://en.wikipedia.org/wiki/File:Mapreduce_Overview.svg), used here in accordance with the [Creative Commons](http://en.wikipedia.org/wiki/Creative_Commons) [Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/).
</div>

# Example: Log crunching

- shell version, small input file
    - map only, add sort, add reduce
- streaming: local (single-node) hadoop
- Dumbo local
- Dumbo hadoop

# Log crunching, more data

- shell version with a 1.4G input file took 44sec
    - 8-way Intel i7, 8GB RAM, SSD
- streaming with 667M input file on Elastic MapReduce took 7 min
    - 1x m1.small master, 2x m1.small core
- much more data needed before the cluster pays off

<hr />

> In a one-meter race between a rocket and a scooter, the scooter is gone
> before the rocket's engines are started.

<div class="handout">
Generated larger (667M) log file like so:
<pre>
for i in {1..100}; do cat log.txt &gt;&gt; /tmp/data23k; done
for i in {1..100}; do cat /tmp/data23k &gt;&gt; /tmp/data2.3M; done
for i in {1..30}; do cat /tmp/data2.3M &gt;&gt; /tmp/data67M; done
for i in {1..10}; do cat /tmp/data67M &gt;&gt; /tmp/data667M; done
for i in {1..20}; do cat /tmp/data67M &gt;&gt; /tmp/data1.4G; done
</pre>
</div>

# Example: Create a book index

- book text
- partially reduced key,value pairs
- final output
- walk through dumbo `mapper()` and `reducer()`

# The End

* <http://adammonsen.com/talks>
* <https://github.com/meonkeys/hadoop-talk>

<!--
vim: ft=markdown
-->