\clearpage

\usection{Abstract}

Many software projects are now equipped with automated test suites of varying levels of comprehensiveness. Mutation testing has the potential to be a powerful measure of test suite effectiveness, but has failed to gain widespread adoption, primarily because it is very time-consuming.

Continuous integration systems have been deployed widely in industry and are used to, amongst other tasks, run test suites and thereby determine whether or not a given build is deemed acceptable.

This project provides software intended to enable mutation testing to be run with each CI build, and to be a determinant of build success. The produced application speeds-up Mutiny (a mutation tool for Ruby) through parallelisation, and analyses its results to give a binary pass or fail outcome. It also produces various types of report, including remotely-hosted HTML reports ideally suited to cloud-based CI systems such as Travis CI.

Evaluation reveals that this approach is practical and usable with several real Ruby projects. A speed-up of around 60% was recorded, with the potential for an even bigger improvement after further work on the parallelisation algorithm.
