\clearpage

# Design & Implementation

The main deliverable from this project is the MultiMutiny application, which is composed of two components; the main application, which runs on the computer performing the mutation testing and a separate cloud-based reporting component. This chapter will describe both of these parts, and, briefly, the development process that created them, before describing the scoring parallelisation algorithm in greater detail.

Both sides to the program are written in Python, with the client-side component using Python 3 and the cloud-side application hosted on Google App Engine and therefore using that platform's integrated Python 2.7 runtime. The relevant code (and a commit history showing how development progressed) is contained within the GitHub repositories in the table below, and so only one small code extract will be quoted in this chapter.

------------------------- ------------------------------------------ -----------------
MultiMutiny               https://github.com/timw6n/multimutiny      468 lines of code
MultiMutiny Cloud Reports https://github.com/timw6n/mm-cloud-reports 222 lines of code
------------------------- ------------------------------------------ -----------------

The line counts above are intended to show the relative sizes of the two projects, and include Python files and HTML template files only. They were calculated using `git ls-files "*.py" "*.html" | xargs wc -l`.

## Development process and software lifecycle

As mentioned at the beginning of the previous chapter, I followed a highly iterative approach to developing the software for this project: Requirements were decided upon, and functionality added, mostly on the fly.

Dogmatically and completely applying a set Agile workflow, such as Scrum or Kanban[@scrumban], would be somewhat excessive for a project such as this, with only myself as both developer and project manager combined. I did however attempt to apply as many Agile principles as were relevant and sensible, given the circumstances. It has already been mentioned that the development process was highly iterative, with a working, but basic, version of MultiMutiny produced quite early on in the year and then refined. Also, one could liken the time between each supervision to a week-long sprint, with supervisor meetings functioning as a quasi-retrospective and planning session. That said, it would be fair to say that my plans for each week never reached the level of fine detail that would be required for, for instance, tickets in a real-world team's issue tracker.

Somewhat ironically, given this project's focus on building quality automated test suites, no automated tests were written for MultiMutiny. The application was, however, tested quite extensively against various sample programs (chiefly the Mutiny demo application described in Appendix 2), and, as will be shown in the Evaluation, doesn't seem to suffer from any major functional bugs. The main factor behind the lack of automated tests was the availability of time, as is often the case with academic software, coupled to the fact that features are much more noteworthy in reports like this one. Secondary to that was the fact that an automated test suite for MultiMutiny alone would not prove particularly useful: Most of the bugs encountered during development were in the mutation tool, rather than in the wrapper around it. Obviously, the absence of an automated test suite precludes the application of mutation testing to MultiMutiny itself.

## Application components and features

### The client-side application

The basic structure of, and tasks performed by, the main, client-side part of the MultiMutiny application is given in the diagram in Figure 4 overleaf. This section will give much more details regarding that structure, and the justifications behind it, starting with the relationships between the parts represented by the differently-coloured shapes.

Recall that, in order for the results of this project to be as widely applicable as possible, MultiMutiny was intended to be coupled as loosely as possible to Mutiny, the mutation tool for which it was initially implemented. All of the code that communicates, via shell commands, with Mutiny is confined to a single, unsurprisingly named, `Mutiny` class shown in Figure 5, which responds to a set interface that should be applicable to other mutation tools. Certainly, there is no code in the main application that requires a specific tool, and the architecture is there to enable wrapper classes for other tools to be dropped-in and selected via MultiMutiny's `-t` command-line flag. One point at which, however, there is something of a closer, but implicit, coupling is in the reading of mutants and their metadata from the relevant `.mutants` directory. While neither this directory's name, nor its contents, mention Mutiny by name, MultiMutiny does expect the relevant files to be in the format produced by Mutiny. I do not consider this to be a huge problem however, as a hypothetical wrapper class for another tool could always manipulate the filesystem itself if some light format-shifting were required.

A similar desire for extensibility led to the use of an almost identical plugin-type structure for what I've termed scorers and reporters, represented on the diagram by green pentagons and ClipArt-style icons respectively. There is only one scorer presented as part of this report; a `LocalScorer` class, each instance of which creates a temporary directory on the local filesystem, copies the project-under-test there, together with that scorer's subset of all the generated mutants, and then instructs the mutation tool to score those mutants. The assignment of mutants to scorers is controlled by the parallelisation algorithm defined below, with the parallel execution itself being by way of the mapping functionality provided by the `multiprocessing` package in Python's standard library. The concept of scorers was split-out from the main application code to provide a clear path towards the creation of a distributed scoring system, an idea explored further in the Conclusion chapter.

Reporters, for their part, receive the parsed mutation results, with mutant metadata already added, and are responsible for communicating those results, in one form or another, to the user. Three reporters are provided as part of this project; one which simply outputs to the command-line, one which generates a standalone HTML file, and one which communicates with MultiMutiny's cloud component and is ideally-suited to being used with cloud-based CI systems.

Screenshots of reports produced by the CLI and HTML reporters are given as Figures 6 and 7 respectively. The majority of the details given in these reports should be self-explanatory, but one term that needs defining is the "pessimistic mutation score". The word pessimistic has been prepended to emphasise that neither Mutiny nor MultiMutiny make any effort to identify equivalent mutants: The real mutation score, if one accepts that it should not take equivalent mutants into account, could be higher than the figure given. The HTML reports are similar in all but one aspect to those presented by the cloud component, and so will be covered, along with the cloud reporter, in more detail in the next subsection.

Finally, it is important to give a brief description of MultiMutiny's benchmark mode, which was utilised when producing the timings given in the Evaluation chapter. As we have seen, MultiMutiny has more features than, and therefore needs to do more work than, Mutiny on its own. The addition of the benchmark mode is an attempt to make timing measurements taken against MultiMutiny somewhat comparable with those taken against Mutiny, and thereby allow the efficacy of the parallelisation procedure to be judged. Enabling benchmark mode disables the potentially time-consuming loading of mutant metadata from disk, as well as the project compatibility check normally performed at the start of each run.

### The cloud reporting system

As mentioned at the head of this chapter, MultiMutiny's cloud component was built as a separate codebase to the main application and runs on Google's App Engine. App Engine was chosen because it abstracts away many sysadmin-type concerns, making the cloud reporting system highly-available, fast and scalable without me having to, for example, set-up and maintain any VPS instances. Using Python, the same language as for the client-side application, albeit an older version, meant that some code and templates, particularly those involved in actually rendering reports, could be re-used from the standalone HTML reporter.

Figure 8 is a screenshot of a report displayed by the cloud system. The report is, as one might expect given the above comment regarding shared code, pretty much identical to an equivalent HTML report. This report was generated in CI mode, hence the large green "CI BUILD PASSED" text. Each mutant's name is a hyperlink that, when clicked, opens up a modal window similar to that shown in Figure 9. As one can see from the figure, that box gives a standard-format diff between the relevant original and mutant files. Originally, the full contents of each file were displayed side-by-side in the dialogue, which was fine for the very small files in toy applications, but proved somewhat impractical for larger, actually useful, projects. The links at the bottom of the dialogue point to full versions of both of those files. These links are not present for the standalone HTML reports as, when using that reporter, it was considered safe to assume that the user has access to the raw files within the `.mutants` directory.

Reports are uploaded, by the cloud reporter, to the cloud system as the JSON-format payload of an HTTP PUT request. An example set of results, as translated into JSON, is given in Appendix 3. Once received by the server, each uploaded report is validated against the JSON schema given in Appendix 4. A URL pointing to that report is then returned to the client, which outputs it to the command-line. Using a schema is quite a heavyweight solution, in comparison to simply assuming the object received has the correct structure and relying on exceptions being thrown if it doesn't, but does have some significant advantages: It enables report-handling code protected by the schema check to be cavalier with regard to accessing keys and the like, in the knowledge that any report that code will touch must be of the expected format. Going forward, using a schema-based system could make it easier to maintain backwards compatibility with older clients, as, when new features are added, a new schema version could be created, with requests matched against the appropriate version. A well-defined schema also allows the possibility of additional clients being able to communicate with the cloud system.

## MultiMutiny's parallelisation algorithm

MultiMutiny's parallelisation algorithm is extremely simple, and reproduced in full below. It is the method responsible for allocating mutants to scoring instances.

```{.python}
def divide(sequence, numsegments):
    return [sequence[i::numsegments] for i in range(numsegments)]
```

As the above code is quite concise, its function is easiest to explain using an example: Let's say that we have a list of five mutants, represented by variable names `a` to `e`, and wish to divide them across three parallel scoring processes, numbered `1`, `2` and `3`. This would lead to a method call of `divide([a, b, c, d, e], 3)`, which gives the result `[[a, d], [b, e], [c]]`, where each of the nested lists represents the mutants assigned to a scorer. The allocation method is even clearer when expressed in the tabular form that will be re-used in the Evaluation chapter:

1\hspace{10mm} 2\hspace{10mm} 3
-------------- -------------- -
a              b              c
d              e

Clearly, this algorithm make no attempt to optimise the allocation with reference to any of the mutant's properties. Its performance was, however, deemed to be sufficient given the results of the experiment detailed in the Analysis chapter. Discussion of alternative, and potentially better, allocation methods will therefore be deferred until the Evaluation and Conclusion chapters.

![The basic structure of the MultiMutiny program. The blue rectangles represent steps carried out by the MultiMutiny core code, the green pentagons steps carried out by the scoring instances and the red circles those performed by the mutation tool. The three icons at the bottom represent the three reporting components.](images/mm-structure.png)

![The Mutiny class and those classes that instantiate it. Attributes and methods for other classes are given only where they have some connection to the Mutiny class. Blue lines show instance creation, black arrows method calls to a created instance.](images/uml.png)

![MultiMutiny CLI output for the Mutiny demo application.](images/cli-report.png)

![A local HTML version of the above report.](images/html-report.png)

![A MultiMutiny cloud report in CI mode. This build has passed as the pessimistic mutation score of 89% was above the 85% threshold set.](images/ci-report.png)

![The same cloud report as the above figure, showing more details for the first mutation.](images/ci-report-lightbox.png)
