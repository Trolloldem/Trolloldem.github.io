+++
title = "Multi-dimensional indexes for point and range queries on outsourced encrypted data"
date = "2021-10-25"
aliases = ["Databases","Mehrotra","Searchable encryption","Privacy",
"PostgreSQL", "Globecom", "Indexes", "Mosaicrown"]
[ author ]
  name = "Gianluca Oldani"
+++
In this work we present an approach for indexing encrypted data
stored at external providers to enable provider-side evaluation of
queries. The presented approach supports the evaluation of point and range
conditions on multiple attributes. Protection against inferences
from indexes is guaranteed by clustering tuples in boxes that are
then mapped to the same index values, so to ensure collisions for
individual attributes as well as their combinations. 
Our algorithm partitions tuples to produce such a clustering
in a way to ensure efficient query execution. Query translation
and processing require the client to store a compact map. The
experiments, evaluating query performance and client-storage
requirements, confirm the efficiency enjoyed by our solution.
##### Authors:
Sabrina De Capitani di Vimercati, Dario Facchinetti, Sara Foresti, Gianluca Oldani, Stefano Paraboschi, Matthew Rossi, Pierangela Samarati

##### Paper presented at:&nbsp;<a href="https://globecom2021.ieee-globecom.org/" target="_blank">Globecom 2021</a>

##### <a href="https://cs.unibg.it/seclab-papers/2021/GLOBECOM/multi-dimensional-indexes.pdf" target="_blank">Link to PDF</a>
