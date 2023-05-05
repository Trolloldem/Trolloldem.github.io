+++
title = "Cage4Deno: A Fine-Grained Sandbox for Deno Subprocesses"
date = "2023-05-05"
aliases = ["AsiaCCS","ACM","WebAssembly","Landlock LSM",
"eBPF", "sandboxing", "Deno", "Cage4Deno", "GLACIATION", "JavaScript"]
[ author ]
  name = "Gianluca Oldani"
+++
This work illustrates a mechanism to enhance the security 
properties of Deno. Deno is a runtime for JavaScript and TypeScript 
that is receiving great interest by developers, and is increasingly used 
for the construction of back-ends of web applications. A primary goal of Deno
is to provide a secure and isolated environment for the execution of
JavaScript programs. It also supports the execution of subprocesses,
unfortunately without providing security guarantees.
The proposal exposed in this paper consists in a set of modifications to
Deno enabling the creation of fine-grained sandboxes for the execution of 
subprocesses. The design of Cage4Deno satisfies the
compatibility, transparency, flexibility, usability, security, and performance 
needs of a modern sandbox. The realization of these
requirements partially stems from the use of Landlock and eBPF,
two robust and efficient security technologies. Significant attention
has been paid to the design of a flexible and compact policy model
consisting of RWX permissions, which can be automatically created,
and deny rules to declare exceptions. The sandbox effectiveness
is demonstrated by successfully blocking a number of exploits for
recent CVEs, while runtime experiments prove its efficiency.
##### Authors:
Marco Abbadini, Michele Beretta, Dario Facchinetti, Gianluca Oldani, Matthew Rossi, Stefano Paraboschi

##### The Paper will be presented at:&nbsp;<a href="https://asiaccs2023.org/" target="_blank">AsiaCCS 2023</a>

##### <a href="https://cs.unibg.it/seclab-papers/2023/ASIACCS/paper/cage4deno.pdf" target="_blank">Link to PDF</a>
