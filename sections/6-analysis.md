\clearpage

# Analysis

Recall that the aim of this project is to provide a means by which mutation testing can be included as part of CI builds. To achieve that objective, the software produced needs to include a mechanism for speeding up the mutation testing process, as well as providing a binary pass/fail output, not to mention the tooling necessary to actually perform the mutation testing process and to create and view reports from a CI context.

This chapter describes broad goals and requirements for the work carried out as part of this project, as well as the justifications behind them, and the methods by which those requirements were arrived at. The Design & Implementation section immediately following goes into the detail of how the software was implemented in order to meet the specified requirements. In terms of the actual sequence in which work was carried out, the activities described in the aforementioned two sections were intermeshed: As will become particularly clear as some of the experimentation done to justify the speed-up approach chosen is explained, the design described in the following section was arrived at iteratively and alongside some of the more detailed analysis work below.

## Constraints imposed by the CI environment

First, it was necessary to consider some of the technical constraints associated with running within a CI environment. For the sake of brevity and because cloud-based CI systems tend to be the most restrictive, the Travis CI documentation will be cited below for elements common to most similar systems. Competitor products will be mentioned only when they differ in functionality. It is also important to note here that, even if only for testing while under development, the software produced as part of this project will also need to be able to function outside of a CI environment.

A CI build consists of a setup phase, used to install dependencies and set up the environment, and which it is unnecessary to consider further, and a build phase, which runs the actual build and tests[@tcustom]. That phase consists of a number of commands, executed in sequence. If every command returns an exit code of 0 then the build will be marked as having succeeded. If any command returns a non-zero exit code then the build will continue but, at the end, will be marked as failed[@tcustom]. Travis builds take place on virtual machines under that company's control, which are instantiated anew prior to each build and then torn down (and the resources used by a different customer) afterwards[@tenv]. This means that one cannot simply rely on a user being able to browse the machine's file system or run additional commands to find out the precise details of the mutants created. It would be possible to output the mutant's source code to the command-line, which is persisted as the build log, but for a large number of mutants that would create a ridiculously unwieldy amount of text. The solution therefore is to transmit the mutant data to a separate system for safe-keeping and eventual viewing, leading to the requirement that the software created as part of this project have a cloud-based component with that functionality. Builds using Jenkins and Bamboo can suffer from similar constraints, although for those systems the testing VMs involved would at least be under the direct control of the organisation running the tests. Many such organisations would be reluctant however to keep machines running just in case a developer needed more details about a single build.

## Decision on whether or not to extend an existing tool

A key decision that needed to be taken was whether to improve an existing mutation testing tool to give it the features required or whether to build something at a higher level of abstraction, in other words a wrapper around a mutation testing tool. The main reason behind my choice for the latter approach was that the work needed to integrate with CI systems is quite generally applicable: Most mutation testing tools, regardless of which language they target, still produce mutants, score them and produce a percentage score at the end of the day. Choosing to extend a single tool would limit the potential impact of this project unnecessarily. Choosing to build a wrapper also means that, as will become relevant in the next chapter, the choice of implementation language for the wrapper is de-coupled from that used for the tool.

## Decision on speed-up approach

The other main aim of the software produced as part of this project was of course to speed-up the mutation testing process somewhat. The decision to pursue a relatively tool-independent approach ruled out many of the possibilities identified in the Literature Review: Selective mutation and weak mutation would require too much co-operation from, and development of, the mutation tool to be appropriate. Mutant sampling techniques wouldn't necessarily require such deep integration, but the random nature of most such approaches would jeopardise the repeatability of and consistency between runs necessary for trustworthy CI builds. "Do faster" approaches involving tweaked mutant compilation would be too language-specific, and are  inapplicable to dynamic languages such as Ruby (chosen as the initial target language, as described below) anyway.

That leaves parallelisation, a "do smarter" approach, as the main contender. Unlike some of the aforementioned approaches, this method would not only not require deep co-operation from the mutation tool, it would also mean that the exact same mutants would be end up being executed against the same tests: The results should, in an ideal world, be indistinguishable from those arising from the (single-threaded) tool directly. The fact that, as discussed previously, there are papers in the literature reporting quite dramatic (i.e. up to linear as more parallel processes are added) speed increases from this method was also a factor in its favour.

## Choice of mutation tool to wrap

Having decided to go with a wrapper approach, the decision then arose as to which mutation testing tool to actually wrap. While the eventual goal would be support multiple tools, the choice of initial tool would have an impact on the wrapper-to-tool interface, and, given the time constraints on the project, I'd need to be able to get to a working implementation sooner rather than later in order to validate other aspects of the design.

In collaboration with my supervisor, it was decided to choose a tool targeting Ruby-language projects as my supervisor was familiar with the area and I was reasonably familiar with the language at least. Only two truly viable options therefore emerged, namely Mutant[@mutant] and Mutiny[@mutiny]. To assist in choosing between them, and to govern some aspects of the wider design, I devised the following set of requirements as a kind of contract that the chosen tool must meet, or at least be modified to meet:

**1. The frontend and backend of the tool (i.e. mutation creation and scoring respectively) need to be callable separately.**

This requirement is crucial, in that, in order for the wrapper to distribute the scoring work between processes, it needs to be able to sit between the mutant generation and mutant scoring parts of the tool (as shown in the diagram in the next chapter). Mutiny already met this requirement through its `mutate` and `score` subcommands. Mutant had no such ability.

**2. The tool needs to be able to provide the set of generated mutants.**

As alluded to above, Mutiny was able to meet this requirement as its `mutate` subcommand saves all generated mutants to a `.mutants` directory under the current path. Mutant only provides its mutants at the end of the complete testing process.

**3. The tool would ideally provide metadata relating to mutant generation.**

This metadata could include the mutation operator used and the line and column to which it was applied. As shown by the word "ideally" this requirement was not as important as the others. Mutant provides this information in its command-line output only for surviving mutants. Mutiny did not initially have this feature, but it was added during the course of this project.

**4. The tool needs to be able to receive a subset of mutants and then score only those mutants.**

This is the major piece both tools lacked initially. I implemented this myself in a forked version of Mutiny, which was then superseded by a subsequent release in the upstream repository.

**5. The tool needs to output mutation scoring results somehow, ideally in an easily parseable format.**

Both tools meet this requirement by printing their results to the command-line in a manner that can be parsed with a regex. Obviously, support for an actual data interchange would be even better.

**6. It needs to be possible to run multiple instances of the tool in parallel on the same machine.**

Both tools would seem to be able to meet this requirement. Mutant already supports parallelisation through its `-j` option, which may actually be something of a negative: Difficulties could arise if attempting to override its in-built behaviour, particularly if there was time to implement multiple-machine parallelisation.

**7. Ideally, the tool would be able to do a basic sanity check to determine whether or not it supports mutating a given project.**

Mutiny supports this explicitly via the `check` subcommand. Mutant, on the other hand, does not have such an option but will quickly exit if it cannot find anything to do.

The notes above should give a clear indication that using Mutiny was already emerging as the preferred option. The pragmatic factor that sealed the deal was that Mutiny's sole developer was my supervisor for this project, meaning that help with understanding its workings would be easily accessible. There was also a realistic prospect of shaping future work so as to implement the missing components for points 3 and 4 above, or at least receiving guidance in how to address those deficiencies.

## Experimental validation of parallelisation approach

With both the mutation tool and the means to accelerate its operation chosen, it seemed a good idea to validate the latter decision. Having implemented an early version of the wrapper script, hereafter known as MultiMutiny, it was possible to put its parallelisation algorithm to the test with a small experiment. I created a second script known as `mm-benchmark` (and available at https://github.com/timw6n/mm-benchmark) which would create multiple copies of the program code and associated specs for the Mutiny demo application described in Appendix 2. Each newly inflated program, comprising between 1 and 50 such copies, would then be tested three times with MultiMutiny to produce an average execution time. This is perhaps not enough data, or a sufficiently realistic methodology, for a truly rigorous experiment, but it was only really intended to confirm that the approach was feasible.

![A graph showing the time required to mutation test different numbers of program copies. Times are given for Mutiny and for MultiMutiny using 1–4 processes. Results for 5–8 processes are not shown, but would closely follow the four-process line.](images/analysis-graph.png)

The key results arising from this experiment, as run on my quad-core desktop computer, were as follows, in roughly decreasing order of significance:

* Parallelisation via MultiMutiny does provide quite a significant speed increase, versus running Mutiny on its own. This is especially true as the size of the program-under-test increases: As the graph in Figure 3 shows, at 50 copies of the `Palindrome` class and related tests and using four processes, the testing process took just under 40% of the usual time.
* Even with quite trivial programs, parallelisation still provides a speed increase: For the unmodified example program (i.e. the point relating to one copy on the graph) the four-core parallelised implementation took, on average, only 74% of Mutiny's normal runtime. With two scoring processes in use, there was still a time-saving of around 10% shown in the same circumstances.
* There was a certain amount of overhead associated with wrapping Mutiny in this way: Running MultiMutiny in single-process mode caused the testing process to be around 40% slower. This is a legitimate use-case, given that MultiMutiny's CI and reporting features are likely to be useful (and hopefully considered worth the time penalty) even if either the program-under-test or the system hardware cannot support parallel operation.
* There was no appreciable speed increase beyond four simultaneous processes. This was as expected for a system with a quad-core CPU, as such a processor can only execute a maximum of four instructions at once.

I considered these findings sufficiently promising as to justify carrying on with the parallelisation approach.

## Decision on how to set the mutation threshold

The final point to consider is how to set the mutation score threshold beyond which a given test is deemed to have passed. Using a simple, user-supplied threshold was the easiest possibility to implement and was the method eventually chosen. In the absence of any clear literature giving a clue as to an appropriate threshold level, I felt it wise not to make an editorial decision on this point, and to let MultiMutiny's eventual users make their own decision with their own codebases in mind.

An interesting alternative would have been to implement a "not decreasing" threshold, whereby each build for a project must match or exceed the previous build's score. The problem with implementing this came from the fact that, as described above, MultiMutiny must not rely on persisting any state on the machine running it. It would be necessary therefore for the cloud component to have a concept of a project, and of a sequence of builds within a project, something which, though by no means impossible, would mean that it would end up taking over some of the responsibilities of the CI systems triggering it. This would violate the engineering principle of doing "one thing well". Besides, it would be by no means impossible for an end-user to build such a system on top of MultiMutiny, if running it on machine with non-temporary storage available.
