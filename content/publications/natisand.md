+++
title = "NatiSand: Native Code Sandboxing for JavaScript Runtimes"
date = "2023-10-16"
aliases = ["RAID","ACM","WebAssembly","Landlock LSM",
"eBPF", "sandboxing", "Deno", "Cage4Deno", "GLACIATION", "JavaScript"]
[ author ]
  name = "Gianluca Oldani"
+++
This work takes into consideration modern runtimes that render JavaScript code 
in a secure and isolated environment, 
but when they execute binary programs and shared libraries, no isolation 
guarantees are provided. This is an important limitation, and it affects many 
popular runtimes including Node.js, Deno, and Bun.

In this paper we propose NatiSand, a component for JavaScript runtimes that 
leverages Landlock, eBPF, and Seccomp to control the filesystem, Inter-Process 
Communication (IPC), and network resources available to binary programs and 
shared libraries. NatiSand does not require changes to the application code and 
offers to the user an easy interface. To demonstrate the effectiveness and 
efficiency of our approach we implemented NatiSand and integrated it into Deno, 
a modern, security-oriented JavaScript runtime. We reproduced a number of 
vulnerabilities affecting third-party code, showing how they are mitigated by 
NatiSand. We also conducted an extensive experimental evaluation to assess the 
performance, proving that our approach is competitive with state of the art code 
sandboxing solutions. The implementation is available open source.

##### Authors:
Marco Abbadini, Dario Facchinetti, Gianluca Oldani, Matthew Rossi, Stefano Paraboschi

##### The Paper has been presented at:&nbsp;<a href="https://raid2023.org/welcome.html" target="_blank">RAID 2023</a>

##### <a href="https://dl.acm.org/doi/10.1145/3607199.3607233" target="_blank">Link to paper</a>
