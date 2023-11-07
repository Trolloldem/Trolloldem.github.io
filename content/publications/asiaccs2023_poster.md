+++
title = " Leveraging eBPF to enhance sandboxing of WebAssembly runtimes"
date = "2023-05-03"
aliases = ["AsiaCCS","ACM","WebAssembly","WASI",
"eBPF", "sandboxing", "GLACIATION"]
[ author ]
  name = "Gianluca Oldani"
+++
In this work we propose a solution aimed at enhancing the security of the sandbox provided by WebAssembly runtimes when file system resources are accessed through the WebAssembly System Interface(WASI). Currenlty, runtimes implementing WASI, must prevent hostcalls to access arbitrary locations, thus they introduce security checks to only permit access to a predefined list of directories. This approach not only suffers from poor granularity: previous works have also investigated that it is also error-prone and has led to several security issues. In this preliminar investigation, we have replaced the security checks in hostcall wrappers with eBPF programs, enabling the introduction of fine-grained per-module policies. The experiments illustrated in the paper confirm that our approach introduces limited overhead when applied to existing runtimes.
##### Authors:
Marco Abbadini, Michele Beretta, Dario Facchinetti, Gianluca Oldani, Matthew Rossi, Stefano Paraboschi

##### The Paper has been presented at:&nbsp;<a href="https://asiaccs2023.org/" target="_blank">AsiaCCS 2023</a>

##### <a href="https://cs.unibg.it/seclab-papers/2023/ASIACCS/poster/enhance-wasm-sandbox.pdf" target="_blank">Link to PDF</a>
