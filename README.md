# GraphFly focus on dependency-flow exploiting. 

GraphFly generates the D-trees of initial graph. And the initial graph is divided into many dependency-flows.

   $ python main.py

GraphFly can be easily integrated in existing streaming graph systems. Following commands is we use GraphBolt systems (https://github.com/pdclab/graphbolt) to execute graph algorithms based on dependency-flows processing: 
   
   $ ./BFS -source 1 -numberOfUpdateBatches 1 -nEdges 100000
-streamPath ../inputs/live-journal/[edge streams file] 
-outputFile /tmp/output/bfs_log ../inputs/livejournal/
[dependency flows file]

   $ ./SSSP -source 1 -numberOfUpdateBatches 1 -nEdges 100000 
-streamPath ../inputs/livejournal/[edge streams file] 
-outputFile /tmp/output/sssp_log ../inputs/livejournal/
[dependency flows file]

   $ ./SSWP -source 1 -numberOfUpdateBatches 1 -nEdges 100000 
-streamPath ../inputs/livejournal/[edge streams file] 
-outputFile /tmp/output/sswp_log ../inputs/livejournal/
[dependency flows file]

   $ ./CC -source 1 -numberOfUpdateBatches 1 -nEdges 100000 
-streamPath ../inputs/livejournal/[edge streams file] 
-outputFile /tmp/output/cc_log ../inputs/livejournal/
[dependency flows file]

   $ ./PageRank -numberOfUpdateBatches 1 -nEdges 100000 
-streamPath ../inputs/livejournal/[edge streams file] 
-outputFile /tmp/output/pr_log ../inputs/livejournal/
[dependency flows file]

   $ ./LabelPropagation -numberOfUpdateBatches 1 -nEdges 
100000 -streamPath ../inputs/livejournal/[edge streams 
file] -seedsFile ../inputs/livejournal/lj-seeds-file 
-outputFile /tmp/output/lp_log ../inputs/livejournal/
[dependency flows file]

