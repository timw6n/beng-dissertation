\clearpage

# Introduction

Maintaining a high level of software quality is, or at least should be, of paramount importance for most development teams. One way in which quality is ensured is through automated test suites. In order to be useful, these test suites must be as comprehensive as possible.

Mutation testing is a measure of test suite effectiveness, and involves making small changes to a program's source code, with the aim of determining whether or not the relevant test suite can detect that each altered version, or mutant, differs from the original. A mutation score, representing the percentage of mutants thus detected, quantifies the test suite's effectiveness.

Continuous integration (or CI) systems are usually integrated with a software project's version-control system and start a build after each commit or check-in. After the build completes, a report is generated and, if the build is deemed to have failed, the responsible developers can be alerted by email or other means. These systems provide the advantage of making it easy to see exactly when, where and by whom low-quality code is introduced into a system, making it possible to quickly improve or remove such code.

If run regularly, as part of each CI build, mutation testing has the potential to improve software reliability. As will be described in the Literature Review, it has, however, failed to achieve widespread industrial adoption, primarily because it is slow. Also, the percentage score produced from mutation testing does not obviously match-up with the binary pass or fail statuses of CI builds. This project's goal is to make a small contribution to addressing these two deficiencies, and thereby to provide software (which I've called MultiMutiny) that will enable mutation testing to be easily included as part of CI builds and to give it sufficient performance to be somewhat useful.

The Literature Review goes over the above definitions and areas of work in much greater detail, encompassing basic manual and automated testing techniques, before moving on to code coverage metrics. Mutation testing is introduced as a stronger version of code coverage. CI systems and their benefits are explained, after which there is discussion of some issues inherent in mutation testing and how those may hinder operation in a CI context.

The main purpose of the Analysis section is to give the rationale behind three key decisions relating to the design of this project's software; the decision to build a wrapper around existing mutation testing tooling, the choice of which tool to use for the initial implementation, and the decision (and its subsequent experimental validation) to exploit the fact that many test suites and mutation testing tools are single-threaded and use a parallelisation-based approach to speed-up the mutation scoring process. This section also provides justification for the creation of a cloud-based reporting component and for the decision to use a static, user-determined threshold to determine build success.

The Design & Implementation section describes the final structure and implementation of the client-side MultiMutiny application and its cloud reporting component, as well as the relationship between the two. This section also explores the way in which the main, client-side program is designed to be as extensible as possible. There are also some brief comments relating to the software development process followed while undertaking this project and a description of MultiMutiny's parallelisation algorithm.

The Evaluation section attempts to determine the extent to which the software produced as this project's main deliverable meets its goals and requirements. This is done by running MultiMutiny against several real codebases, showing that it works and that a significant speed increase is achieved through parallelisation. There is still room for improvement with regard to the latter point however.

Finally, the Conclusion provides a brief recap of the project and gives a few suggestions for further work.
