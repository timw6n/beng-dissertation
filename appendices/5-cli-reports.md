\pagebreak

# Appendix 5: MultiMutiny reports for real codebases {-}

This appendix gives complete reports for the real projects referred to in the Evaluation section, as produced by MultiMutiny's CLI reporter.

The first report in this section was produced in "normal" mode, i.e. without activating CI mode and setting a threshold, while the latter two reports show a passing and failing CI-mode build respectively.

The first line of each report (starting with `$`) gives the command run.

Links to uploaded copies of the equivalent HTML reports, and to reports live on the cloud reporting system follow in Appendix 6.

\usubsection{event\_bus}

\footnotesize

```
$ multimutiny

-------------------------------------------------------------------------------------------------------------
                                              MultiMutiny Report
-------------------------------------------------------------------------------------------------------------

+----------------------------+-----+
| # Mutants Created          | 57  |
| # Mutants Killed           | 51  |
| Pessimistic Mutation Score | 89% |
+----------------------------+-----+

+-------------------------------+-------------------------+------------+-----------+------------+-----------+
| Mutant                        | Target                  | Operator   | Status    | # Tests    | Time      |
|-------------------------------+-------------------------+------------+-----------+------------+-----------|
| event_bus/registrations.0.rb  | EventBus::Registrations | COI        | survived  | 31 (of 31) | 0.017789s |
| event_bus/registrations.1.rb  | EventBus::Registrations | COI        | killed    | 1 (of 31)  | 0.026732s |
| event_bus/registrations.2.rb  | EventBus::Registrations | COI        | killed    | 10 (of 31) | 0.041409s |
| event_bus/registrations.3.rb  | EventBus::Registrations | COI        | survived  | 31 (of 31) | 0.016192s |
| event_bus/registrations.4.rb  | EventBus::Registrations | COI        | killed    | 2 (of 31)  | 0.027454s |
| event_bus/registrations.5.rb  | EventBus::Registrations | COI        | survived  | 31 (of 31) | 0.017427s |
| event_bus/registrations.6.rb  | EventBus::Registrations | COI        | killed    | 9 (of 31)  | 0.066081s |
| event_bus/registrations.7.rb  | EventBus::Registrations | COI        | killed    | 10 (of 31) | 0.068974s |
| event_bus/registrations.8.rb  | EventBus::Registrations | COI        | killed    | 8 (of 31)  | 0.036505s |
| event_bus/registrations.9.rb  | EventBus::Registrations | COI        | survived  | 31 (of 31) | 0.016032s |
| event_bus/registrations.10.rb | EventBus::Registrations | COI        | killed    | 1 (of 31)  | 0.038801s |
| event_bus/registrations.11.rb | EventBus::Registrations | COI        | survived  | 31 (of 31) | 0.016618s |
| event_bus/registrations.12.rb | EventBus::Registrations | COI        | killed    | 1 (of 31)  | 0.047177s |
| event_bus/registrations.13.rb | EventBus::Registrations | COI        | killed    | 10 (of 31) | 0.043221s |
| event_bus/registrations.14.rb | EventBus::Registrations | COI        | survived  | 31 (of 31) | 0.015683s |
| event_bus/registrations.15.rb | EventBus::Registrations | LOI        | killed    | 1 (of 31)  | 0.027413s |
| event_bus/registrations.16.rb | EventBus::Registrations | LOI        | killed    | 1 (of 31)  | 0.035772s |
| event_bus/registrations.17.rb | EventBus::Registrations | LOI        | killed    | 10 (of 31) | 0.031001s |
| event_bus/registrations.18.rb | EventBus::Registrations | LOI        | stillborn | n/a        | n/a       |
| event_bus/registrations.19.rb | EventBus::Registrations | LOI        | killed    | 1 (of 31)  | 0.03648s  |
| event_bus/registrations.20.rb | EventBus::Registrations | LOI        | killed    | 1 (of 31)  | 0.027083s |
| event_bus/registrations.21.rb | EventBus::Registrations | LOI        | killed    | 9 (of 31)  | 0.030682s |
| event_bus/registrations.22.rb | EventBus::Registrations | LOI        | killed    | 10 (of 31) | 0.039402s |
| event_bus/registrations.23.rb | EventBus::Registrations | LOI        | killed    | 8 (of 31)  | 0.038908s |
| event_bus/registrations.24.rb | EventBus::Registrations | LOI        | killed    | 9 (of 31)  | 0.030461s |
| event_bus/registrations.25.rb | EventBus::Registrations | LOI        | killed    | 1 (of 31)  | 0.039189s |
| event_bus/registrations.26.rb | EventBus::Registrations | LOI        | killed    | 13 (of 31) | 0.051285s |
| event_bus/registrations.27.rb | EventBus::Registrations | LOI        | killed    | 1 (of 31)  | 0.05042s  |
| event_bus/registrations.28.rb | EventBus::Registrations | LOI        | killed    | 10 (of 31) | 0.07343s  |
| event_bus/registrations.29.rb | EventBus::Registrations | LOI        | killed    | 19 (of 31) | 0.045765s |
| event_bus/registrations.30.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.028747s |
| event_bus/registrations.31.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.021559s |
| event_bus/registrations.32.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.022631s |
| event_bus/registrations.33.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.028901s |
| event_bus/registrations.34.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.031961s |
| event_bus/registrations.35.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.020941s |
| event_bus/registrations.36.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.020681s |
| event_bus/registrations.37.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.027151s |
| event_bus/registrations.38.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.028807s |
| event_bus/registrations.39.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.020968s |
| event_bus/registrations.40.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.028554s |
| event_bus/registrations.41.rb | EventBus::Registrations | SAOR       | killed    | 1 (of 31)  | 0.03014s  |
| event_bus/registrations.42.rb | EventBus::Registrations | UAOI       | killed    | 1 (of 31)  | 0.020533s |
| event_bus/registrations.43.rb | EventBus::Registrations | UAOI       | killed    | 1 (of 31)  | 0.026158s |
| event_bus/registrations.44.rb | EventBus::Registrations | UAOI       | killed    | 10 (of 31) | 0.038609s |
| event_bus/registrations.45.rb | EventBus::Registrations | UAOI       | stillborn | n/a        | n/a       |
| event_bus/registrations.46.rb | EventBus::Registrations | UAOI       | killed    | 1 (of 31)  | 0.026709s |
| event_bus/registrations.47.rb | EventBus::Registrations | UAOI       | killed    | 1 (of 31)  | 0.026476s |
| event_bus/registrations.48.rb | EventBus::Registrations | UAOI       | killed    | 9 (of 31)  | 0.032533s |
| event_bus/registrations.49.rb | EventBus::Registrations | UAOI       | killed    | 10 (of 31) | 0.040806s |
| event_bus/registrations.50.rb | EventBus::Registrations | UAOI       | killed    | 8 (of 31)  | 0.029494s |
| event_bus/registrations.51.rb | EventBus::Registrations | UAOI       | killed    | 9 (of 31)  | 0.040073s |
| event_bus/registrations.52.rb | EventBus::Registrations | UAOI       | killed    | 1 (of 31)  | 0.04766s  |
| event_bus/registrations.53.rb | EventBus::Registrations | UAOI       | killed    | 13 (of 31) | 0.045031s |
| event_bus/registrations.54.rb | EventBus::Registrations | UAOI       | killed    | 1 (of 31)  | 0.038901s |
| event_bus/registrations.55.rb | EventBus::Registrations | UAOI       | killed    | 10 (of 31) | 0.063441s |
| event_bus/registrations.56.rb | EventBus::Registrations | UAOI       | killed    | 19 (of 31) | 0.056299s |
+-------------------------------+-------------------------+------------+-----------+------------+-----------+
```

\normalsize

\usubsection{full\_name}

\footnotesize

```
$ multimutiny -ci -cit 90

-------------------------------------------------------------------------------
                               MultiMutiny Report
-------------------------------------------------------------------------------

                                CI BUILD PASSED

+----------------------------+------+
| # Mutants Created          | 51   |
| # Mutants Killed           | 51   |
| Pessimistic Mutation Score | 100% |
| CI Threshold               | 90%  |
+----------------------------+------+

+-----------------+----------+------------+----------+------------+-----------+
| Mutant          | Target   | Operator   | Status   | # Tests    | Time      |
|-----------------+----------+------------+----------+------------+-----------|
| full_name.0.rb  | FullName | COI        | killed   | 3 (of 15)  | 0.04193s  |
| full_name.1.rb  | FullName | COI        | killed   | 15 (of 15) | 0.042936s |
| full_name.2.rb  | FullName | COI        | killed   | 3 (of 15)  | 0.044003s |
| full_name.3.rb  | FullName | COI        | killed   | 6 (of 15)  | 0.039877s |
| full_name.4.rb  | FullName | COI        | killed   | 10 (of 15) | 0.040465s |
| full_name.5.rb  | FullName | COI        | killed   | 1 (of 15)  | 0.041161s |
| full_name.6.rb  | FullName | COI        | killed   | 1 (of 15)  | 0.038068s |
| full_name.7.rb  | FullName | COI        | killed   | 6 (of 15)  | 0.036082s |
| full_name.8.rb  | FullName | COI        | killed   | 6 (of 15)  | 0.03985s  |
| full_name.9.rb  | FullName | COI        | killed   | 1 (of 15)  | 0.035455s |
| full_name.10.rb | FullName | COI        | killed   | 1 (of 15)  | 0.038636s |
| full_name.11.rb | FullName | COI        | killed   | 1 (of 15)  | 0.038325s |
| full_name.12.rb | FullName | COI        | killed   | 1 (of 15)  | 0.039776s |
| full_name.13.rb | FullName | COI        | killed   | 11 (of 15) | 0.046286s |
| full_name.14.rb | FullName | COI        | killed   | 11 (of 15) | 0.039437s |
| full_name.15.rb | FullName | COR        | killed   | 8 (of 15)  | 0.027894s |
| full_name.16.rb | FullName | COR        | killed   | 6 (of 15)  | 0.040467s |
| full_name.17.rb | FullName | COR        | killed   | 9 (of 15)  | 0.032095s |
| full_name.18.rb | FullName | COR        | killed   | 9 (of 15)  | 0.027813s |
| full_name.19.rb | FullName | COR        | killed   | 5 (of 15)  | 0.027666s |
| full_name.20.rb | FullName | COR        | killed   | 3 (of 15)  | 0.042332s |
| full_name.21.rb | FullName | LOI        | killed   | 3 (of 15)  | 0.027737s |
| full_name.22.rb | FullName | LOI        | killed   | 15 (of 15) | 0.028771s |
| full_name.23.rb | FullName | LOI        | killed   | 3 (of 15)  | 0.028366s |
| full_name.24.rb | FullName | LOI        | killed   | 6 (of 15)  | 0.029405s |
| full_name.25.rb | FullName | LOI        | killed   | 10 (of 15) | 0.029342s |
| full_name.26.rb | FullName | LOI        | killed   | 1 (of 15)  | 0.026229s |
| full_name.27.rb | FullName | LOI        | killed   | 1 (of 15)  | 0.028093s |
| full_name.28.rb | FullName | LOI        | killed   | 6 (of 15)  | 0.030884s |
| full_name.29.rb | FullName | LOI        | killed   | 6 (of 15)  | 0.027865s |
| full_name.30.rb | FullName | LOI        | killed   | 1 (of 15)  | 0.026223s |
| full_name.31.rb | FullName | LOI        | killed   | 1 (of 15)  | 0.027676s |
| full_name.32.rb | FullName | LOI        | killed   | 1 (of 15)  | 0.026059s |
| full_name.33.rb | FullName | LOI        | killed   | 1 (of 15)  | 0.026222s |
| full_name.34.rb | FullName | LOI        | killed   | 11 (of 15) | 0.029065s |
| full_name.35.rb | FullName | LOI        | killed   | 11 (of 15) | 0.032234s |
| full_name.36.rb | FullName | UAOI       | killed   | 3 (of 15)  | 0.027367s |
| full_name.37.rb | FullName | UAOI       | killed   | 15 (of 15) | 0.028659s |
| full_name.38.rb | FullName | UAOI       | killed   | 3 (of 15)  | 0.026948s |
| full_name.39.rb | FullName | UAOI       | killed   | 6 (of 15)  | 0.028032s |
| full_name.40.rb | FullName | UAOI       | killed   | 10 (of 15) | 0.027033s |
| full_name.41.rb | FullName | UAOI       | killed   | 1 (of 15)  | 0.028182s |
| full_name.42.rb | FullName | UAOI       | killed   | 1 (of 15)  | 0.028905s |
| full_name.43.rb | FullName | UAOI       | killed   | 6 (of 15)  | 0.028302s |
| full_name.44.rb | FullName | UAOI       | killed   | 6 (of 15)  | 0.027506s |
| full_name.45.rb | FullName | UAOI       | killed   | 1 (of 15)  | 0.027445s |
| full_name.46.rb | FullName | UAOI       | killed   | 1 (of 15)  | 0.026962s |
| full_name.47.rb | FullName | UAOI       | killed   | 1 (of 15)  | 0.026493s |
| full_name.48.rb | FullName | UAOI       | killed   | 1 (of 15)  | 0.02702s  |
| full_name.49.rb | FullName | UAOI       | killed   | 11 (of 15) | 0.029148s |
| full_name.50.rb | FullName | UAOI       | killed   | 11 (of 15) | 0.02864s  |
+-----------------+----------+------------+----------+------------+-----------+
```

\normalsize

\usubsection{lumberjack}

The column giving target classes has been omitted from this report in order to enable it to fit on the page. The target class for a mutant can be inferred from the mutant's filename quite easily though: For the first mutant, for example, the filename of `lumberjack/device/date_rolling_log_file.0.rb` translates to a target class of `Lumberjack::Device::DateRollingLogFile`.

\footnotesize

```
$ multimutiny -ci -cit 90

------------------------------------------------------------------------------------------------------
                                          MultiMutiny Report
------------------------------------------------------------------------------------------------------

                                           CI BUILD FAILED

+----------------------------+-----+
| # Mutants Created          | 565 |
| # Mutants Killed           | 480 |
| Pessimistic Mutation Score | 85% |
| CI Threshold               | 90% |
+----------------------------+-----+

+--------------------------------------------------+------------+-----------+------------+-----------+
| Mutant                                           | Operator   | Status    | # Tests    | Time      |
|--------------------------------------------------+------------+-----------+------------+-----------|
| lumberjack/device/date_rolling_log_file.0.rb     | COI        | survived  | 8 (of 8)   | 0.011754s |
| lumberjack/device/date_rolling_log_file.1.rb     | COI        | survived  | 8 (of 8)   | 0.012023s |
| lumberjack/device/date_rolling_log_file.2.rb     | COI        | killed    | 1 (of 8)   | 0.030989s |
| lumberjack/device/date_rolling_log_file.3.rb     | COI        | killed    | 2 (of 8)   | 0.033941s |
| lumberjack/device/date_rolling_log_file.4.rb     | COI        | killed    | 3 (of 8)   | 0.03235s  |
| lumberjack/device/date_rolling_log_file.5.rb     | COI        | survived  | 8 (of 8)   | 0.011397s |
| lumberjack/device/date_rolling_log_file.6.rb     | COR        | killed    | 1 (of 8)   | 0.031201s |
| lumberjack/device/date_rolling_log_file.7.rb     | COR        | killed    | 1 (of 8)   | 0.029981s |
| lumberjack/device/date_rolling_log_file.8.rb     | COR        | survived  | 8 (of 8)   | 0.010744s |
| lumberjack/device/date_rolling_log_file.9.rb     | COR        | survived  | 8 (of 8)   | 0.013716s |
| lumberjack/device/date_rolling_log_file.10.rb    | COR        | survived  | 8 (of 8)   | 0.012176s |
| lumberjack/device/date_rolling_log_file.11.rb    | COR        | survived  | 8 (of 8)   | 0.011449s |
| lumberjack/device/date_rolling_log_file.12.rb    | COR        | survived  | 8 (of 8)   | 0.01272s  |
| lumberjack/device/date_rolling_log_file.13.rb    | COR        | survived  | 8 (of 8)   | 0.012283s |
| lumberjack/device/date_rolling_log_file.14.rb    | RER        | survived  | 8 (of 8)   | 0.012564s |
| lumberjack/device/date_rolling_log_file.15.rb    | RER        | survived  | 8 (of 8)   | 0.012903s |
| lumberjack/device/date_rolling_log_file.16.rb    | RER        | survived  | 8 (of 8)   | 0.012393s |
| lumberjack/device/date_rolling_log_file.17.rb    | RER        | killed    | 1 (of 8)   | 0.029008s |
| lumberjack/device/date_rolling_log_file.18.rb    | RER        | survived  | 8 (of 8)   | 0.011037s |
| lumberjack/device/date_rolling_log_file.19.rb    | RER        | killed    | 1 (of 8)   | 0.030551s |
| lumberjack/device/date_rolling_log_file.20.rb    | RER        | survived  | 8 (of 8)   | 0.012608s |
| lumberjack/device/date_rolling_log_file.21.rb    | RER        | killed    | 2 (of 8)   | 0.029524s |
| lumberjack/device/date_rolling_log_file.22.rb    | RER        | survived  | 8 (of 8)   | 0.011419s |
| lumberjack/device/date_rolling_log_file.23.rb    | RER        | killed    | 2 (of 8)   | 0.033524s |
| lumberjack/device/date_rolling_log_file.24.rb    | RER        | survived  | 8 (of 8)   | 0.012445s |
| lumberjack/device/date_rolling_log_file.25.rb    | RER        | killed    | 3 (of 8)   | 0.031929s |
| lumberjack/device/date_rolling_log_file.26.rb    | RER        | survived  | 8 (of 8)   | 0.011679s |
| lumberjack/device/date_rolling_log_file.27.rb    | RER        | killed    | 3 (of 8)   | 0.036239s |
| lumberjack/device/date_rolling_log_file.28.rb    | ROR        | survived  | 8 (of 8)   | 0.012178s |
| lumberjack/device/date_rolling_log_file.29.rb    | ROR        | survived  | 8 (of 8)   | 0.01206s  |
| lumberjack/device/date_rolling_log_file.30.rb    | ROR        | survived  | 8 (of 8)   | 0.014473s |
| lumberjack/device/date_rolling_log_file.31.rb    | ROR        | survived  | 8 (of 8)   | 0.011013s |
| lumberjack/device/date_rolling_log_file.32.rb    | ROR        | survived  | 8 (of 8)   | 0.011159s |
| lumberjack/device/date_rolling_log_file.33.rb    | ROR        | killed    | 1 (of 8)   | 0.028348s |
| lumberjack/device/date_rolling_log_file.34.rb    | ROR        | survived  | 8 (of 8)   | 0.012714s |
| lumberjack/device/date_rolling_log_file.35.rb    | ROR        | killed    | 1 (of 8)   | 0.028525s |
| lumberjack/device/date_rolling_log_file.36.rb    | ROR        | survived  | 8 (of 8)   | 0.010954s |
| lumberjack/device/date_rolling_log_file.37.rb    | ROR        | killed    | 1 (of 8)   | 0.028647s |
| lumberjack/device/date_rolling_log_file.38.rb    | ROR        | killed    | 1 (of 8)   | 0.028386s |
| lumberjack/device/date_rolling_log_file.39.rb    | ROR        | survived  | 8 (of 8)   | 0.01102s  |
| lumberjack/device/date_rolling_log_file.40.rb    | ROR        | survived  | 8 (of 8)   | 0.011178s |
| lumberjack/device/date_rolling_log_file.41.rb    | ROR        | survived  | 8 (of 8)   | 0.012048s |
| lumberjack/device/date_rolling_log_file.42.rb    | ROR        | survived  | 8 (of 8)   | 0.011108s |
| lumberjack/device/date_rolling_log_file.43.rb    | ROR        | killed    | 2 (of 8)   | 0.029771s |
| lumberjack/device/date_rolling_log_file.44.rb    | ROR        | survived  | 8 (of 8)   | 0.011918s |
| lumberjack/device/date_rolling_log_file.45.rb    | ROR        | killed    | 2 (of 8)   | 0.035335s |
| lumberjack/device/date_rolling_log_file.46.rb    | ROR        | survived  | 8 (of 8)   | 0.01142s  |
| lumberjack/device/date_rolling_log_file.47.rb    | ROR        | killed    | 2 (of 8)   | 0.032267s |
| lumberjack/device/date_rolling_log_file.48.rb    | ROR        | killed    | 2 (of 8)   | 0.031954s |
| lumberjack/device/date_rolling_log_file.49.rb    | ROR        | survived  | 8 (of 8)   | 0.012044s |
| lumberjack/device/date_rolling_log_file.50.rb    | ROR        | survived  | 8 (of 8)   | 0.011201s |
| lumberjack/device/date_rolling_log_file.51.rb    | ROR        | survived  | 8 (of 8)   | 0.014187s |
| lumberjack/device/date_rolling_log_file.52.rb    | ROR        | survived  | 8 (of 8)   | 0.011626s |
| lumberjack/device/date_rolling_log_file.53.rb    | ROR        | killed    | 3 (of 8)   | 0.033565s |
| lumberjack/device/date_rolling_log_file.54.rb    | ROR        | survived  | 8 (of 8)   | 0.012209s |
| lumberjack/device/date_rolling_log_file.55.rb    | ROR        | killed    | 3 (of 8)   | 0.034917s |
| lumberjack/device/date_rolling_log_file.56.rb    | ROR        | survived  | 8 (of 8)   | 0.011415s |
| lumberjack/device/date_rolling_log_file.57.rb    | ROR        | killed    | 3 (of 8)   | 0.034388s |
| lumberjack/device/date_rolling_log_file.58.rb    | ROR        | killed    | 3 (of 8)   | 0.03426s  |
| lumberjack/device/date_rolling_log_file.59.rb    | ROR        | survived  | 8 (of 8)   | 0.014418s |
| lumberjack/device/date_rolling_log_file.60.rb    | ROR        | survived  | 8 (of 8)   | 0.011477s |
| lumberjack/device/date_rolling_log_file.61.rb    | ROR        | survived  | 8 (of 8)   | 0.011368s |
| lumberjack/device/date_rolling_log_file.62.rb    | ROR        | survived  | 8 (of 8)   | 0.011526s |
| lumberjack/device/date_rolling_log_file.63.rb    | LOI        | killed    | 1 (of 8)   | 0.028929s |
| lumberjack/device/rolling_log_file.0.rb          | COD        | killed    | 1 (of 34)  | 0.028067s |
| lumberjack/device/rolling_log_file.1.rb          | COI        | killed    | 1 (of 34)  | 0.031785s |
| lumberjack/device/rolling_log_file.2.rb          | COI        | killed    | 1 (of 34)  | 0.031874s |
| lumberjack/device/rolling_log_file.3.rb          | COI        | survived  | 34 (of 34) | 1.080569s |
| lumberjack/device/rolling_log_file.4.rb          | COI        | survived  | 34 (of 34) | 0.569646s |
| lumberjack/device/rolling_log_file.5.rb          | COI        | killed    | 1 (of 34)  | 0.288139s |
| lumberjack/device/rolling_log_file.6.rb          | COI        | killed    | 1 (of 34)  | 0.097981s |
| lumberjack/device/rolling_log_file.7.rb          | COI        | survived  | 34 (of 34) | 0.76325s  |
| lumberjack/device/rolling_log_file.8.rb          | COI        | survived  | 34 (of 34) | 0.580644s |
| lumberjack/device/rolling_log_file.9.rb          | COI        | killed    | 1 (of 34)  | 0.046214s |
| lumberjack/device/rolling_log_file.10.rb         | COI        | survived  | 34 (of 34) | 0.537736s |
| lumberjack/device/rolling_log_file.11.rb         | COI        | killed    | 1 (of 34)  | 0.201654s |
| lumberjack/device/rolling_log_file.12.rb         | COI        | killed    | 1 (of 34)  | 0.02852s  |
| lumberjack/device/rolling_log_file.13.rb         | COI        | killed    | 1 (of 34)  | 0.02708s  |
| lumberjack/device/rolling_log_file.14.rb         | COI        | killed    | 7 (of 34)  | 0.112444s |
| lumberjack/device/rolling_log_file.15.rb         | COI        | survived  | 34 (of 34) | 0.925635s |
| lumberjack/device/rolling_log_file.16.rb         | COI        | killed    | 1 (of 34)  | 0.168414s |
| lumberjack/device/rolling_log_file.17.rb         | COI        | killed    | 1 (of 34)  | 0.067013s |
| lumberjack/device/rolling_log_file.18.rb         | COI        | killed    | 1 (of 34)  | 0.172034s |
| lumberjack/device/rolling_log_file.19.rb         | COI        | killed    | 1 (of 34)  | 0.030261s |
| lumberjack/device/rolling_log_file.20.rb         | COI        | killed    | 1 (of 34)  | 0.02662s  |
| lumberjack/device/rolling_log_file.21.rb         | COI        | killed    | 1 (of 34)  | 0.027866s |
| lumberjack/device/rolling_log_file.22.rb         | COI        | survived  | 34 (of 34) | 0.543692s |
| lumberjack/device/rolling_log_file.23.rb         | COI        | killed    | 1 (of 34)  | 0.036672s |
| lumberjack/device/rolling_log_file.24.rb         | COI        | killed    | 1 (of 34)  | 0.380485s |
| lumberjack/device/rolling_log_file.25.rb         | COI        | killed    | 11 (of 34) | 0.770433s |
| lumberjack/device/rolling_log_file.26.rb         | COR        | killed    | 1 (of 34)  | 0.132685s |
| lumberjack/device/rolling_log_file.27.rb         | COR        | killed    | 1 (of 34)  | 0.033743s |
| lumberjack/device/rolling_log_file.28.rb         | COR        | killed    | 1 (of 34)  | 0.027331s |
| lumberjack/device/rolling_log_file.29.rb         | COR        | survived  | 34 (of 34) | 0.471533s |
| lumberjack/device/rolling_log_file.30.rb         | COR        | killed    | 1 (of 34)  | 0.032238s |
| lumberjack/device/rolling_log_file.31.rb         | COR        | killed    | 1 (of 34)  | 0.135003s |
| lumberjack/device/rolling_log_file.32.rb         | COR        | killed    | 1 (of 34)  | 0.264796s |
| lumberjack/device/rolling_log_file.33.rb         | COR        | killed    | 1 (of 34)  | 0.060618s |
| lumberjack/device/rolling_log_file.34.rb         | COR        | killed    | 1 (of 34)  | 0.074715s |
| lumberjack/device/rolling_log_file.35.rb         | COR        | killed    | 1 (of 34)  | 0.026762s |
| lumberjack/device/rolling_log_file.36.rb         | RER        | killed    | 11 (of 34) | 0.664908s |
| lumberjack/device/rolling_log_file.37.rb         | RER        | killed    | 11 (of 34) | 0.927851s |
| lumberjack/device/rolling_log_file.38.rb         | RER        | killed    | 1 (of 34)  | 0.029861s |
| lumberjack/device/rolling_log_file.39.rb         | RER        | killed    | 1 (of 34)  | 0.027136s |
| lumberjack/device/rolling_log_file.40.rb         | RER        | killed    | 1 (of 34)  | 0.057392s |
| lumberjack/device/rolling_log_file.41.rb         | RER        | killed    | 1 (of 34)  | 0.033129s |
| lumberjack/device/rolling_log_file.42.rb         | RER        | killed    | 1 (of 34)  | 0.046486s |
| lumberjack/device/rolling_log_file.43.rb         | RER        | killed    | 1 (of 34)  | 0.030356s |
| lumberjack/device/rolling_log_file.44.rb         | RER        | survived  | 34 (of 34) | 0.646037s |
| lumberjack/device/rolling_log_file.45.rb         | RER        | killed    | 1 (of 34)  | 0.131319s |
| lumberjack/device/rolling_log_file.46.rb         | ROR        | killed    | 1 (of 34)  | 0.04677s  |
| lumberjack/device/rolling_log_file.47.rb         | ROR        | killed    | 11 (of 34) | 0.401994s |
| lumberjack/device/rolling_log_file.48.rb         | ROR        | killed    | 11 (of 34) | 0.794366s |
| lumberjack/device/rolling_log_file.49.rb         | ROR        | killed    | 1 (of 34)  | 0.037141s |
| lumberjack/device/rolling_log_file.50.rb         | ROR        | survived  | 34 (of 34) | 0.588223s |
| lumberjack/device/rolling_log_file.51.rb         | ROR        | killed    | 9 (of 34)  | 0.065204s |
| lumberjack/device/rolling_log_file.52.rb         | ROR        | killed    | 1 (of 34)  | 0.032888s |
| lumberjack/device/rolling_log_file.53.rb         | ROR        | killed    | 1 (of 34)  | 0.051102s |
| lumberjack/device/rolling_log_file.54.rb         | ROR        | killed    | 1 (of 34)  | 0.028958s |
| lumberjack/device/rolling_log_file.55.rb         | ROR        | killed    | 9 (of 34)  | 0.068774s |
| lumberjack/device/rolling_log_file.56.rb         | ROR        | killed    | 1 (of 34)  | 0.034955s |
| lumberjack/device/rolling_log_file.57.rb         | ROR        | killed    | 1 (of 34)  | 0.261927s |
| lumberjack/device/rolling_log_file.58.rb         | ROR        | killed    | 1 (of 34)  | 0.046212s |
| lumberjack/device/rolling_log_file.59.rb         | ROR        | survived  | 34 (of 34) | 0.784842s |
| lumberjack/device/rolling_log_file.60.rb         | ROR        | killed    | 1 (of 34)  | 0.050484s |
| lumberjack/device/rolling_log_file.61.rb         | ROR        | killed    | 1 (of 34)  | 0.059133s |
| lumberjack/device/rolling_log_file.62.rb         | ROR        | survived  | 34 (of 34) | 0.603923s |
| lumberjack/device/rolling_log_file.63.rb         | ROR        | killed    | 1 (of 34)  | 0.031285s |
| lumberjack/device/rolling_log_file.64.rb         | ROR        | killed    | 1 (of 34)  | 0.044876s |
| lumberjack/device/rolling_log_file.65.rb         | ROR        | killed    | 1 (of 34)  | 0.027427s |
| lumberjack/device/rolling_log_file.66.rb         | ROR        | killed    | 1 (of 34)  | 0.047251s |
| lumberjack/device/rolling_log_file.67.rb         | ROR        | killed    | 1 (of 34)  | 0.033048s |
| lumberjack/device/rolling_log_file.68.rb         | ROR        | killed    | 1 (of 34)  | 0.044292s |
| lumberjack/device/rolling_log_file.69.rb         | ROR        | survived  | 34 (of 34) | 0.747725s |
| lumberjack/device/rolling_log_file.70.rb         | ROR        | killed    | 1 (of 34)  | 0.151335s |
| lumberjack/device/rolling_log_file.71.rb         | LOI        | killed    | 1 (of 34)  | 0.046189s |
| lumberjack/device/rolling_log_file.72.rb         | LOI        | killed    | 1 (of 34)  | 0.045228s |
| lumberjack/device/rolling_log_file.73.rb         | LOI        | killed    | 2 (of 34)  | 0.050558s |
| lumberjack/device/rolling_log_file.74.rb         | LOI        | killed    | 1 (of 34)  | 0.049578s |
| lumberjack/device/rolling_log_file.75.rb         | LOI        | killed    | 1 (of 34)  | 0.142677s |
| lumberjack/device/rolling_log_file.76.rb         | LOI        | survived  | 34 (of 34) | 0.389625s |
| lumberjack/device/rolling_log_file.77.rb         | LOI        | killed    | 9 (of 34)  | 0.063395s |
| lumberjack/device/rolling_log_file.78.rb         | LOI        | killed    | 1 (of 34)  | 0.033276s |
| lumberjack/device/rolling_log_file.79.rb         | LOI        | killed    | 1 (of 34)  | 0.047845s |
| lumberjack/device/rolling_log_file.80.rb         | LOI        | killed    | 1 (of 34)  | 0.057987s |
| lumberjack/device/rolling_log_file.81.rb         | LOI        | killed    | 1 (of 34)  | 0.032857s |
| lumberjack/device/rolling_log_file.82.rb         | LOI        | killed    | 1 (of 34)  | 0.054717s |
| lumberjack/device/rolling_log_file.83.rb         | LOI        | killed    | 7 (of 34)  | 0.057101s |
| lumberjack/device/rolling_log_file.84.rb         | LOI        | survived  | 34 (of 34) | 0.684121s |
| lumberjack/device/rolling_log_file.85.rb         | LOI        | killed    | 1 (of 34)  | 0.033315s |
| lumberjack/device/rolling_log_file.86.rb         | LOI        | killed    | 1 (of 34)  | 0.043402s |
| lumberjack/device/rolling_log_file.87.rb         | LOI        | killed    | 1 (of 34)  | 0.1022s   |
| lumberjack/device/rolling_log_file.88.rb         | LOI        | killed    | 1 (of 34)  | 0.046027s |
| lumberjack/device/rolling_log_file.89.rb         | LOI        | killed    | 1 (of 34)  | 0.034126s |
| lumberjack/device/rolling_log_file.90.rb         | LOI        | killed    | 1 (of 34)  | 0.028292s |
| lumberjack/device/rolling_log_file.91.rb         | LOI        | killed    | 1 (of 34)  | 0.048014s |
| lumberjack/device/rolling_log_file.92.rb         | LOI        | killed    | 1 (of 34)  | 0.032865s |
| lumberjack/device/rolling_log_file.93.rb         | LOI        | killed    | 1 (of 34)  | 0.047379s |
| lumberjack/device/rolling_log_file.94.rb         | LOI        | killed    | 1 (of 34)  | 0.031602s |
| lumberjack/device/rolling_log_file.95.rb         | LOI        | killed    | 11 (of 34) | 0.720951s |
| lumberjack/device/rolling_log_file.96.rb         | UAOI       | killed    | 1 (of 34)  | 0.033804s |
| lumberjack/device/rolling_log_file.97.rb         | UAOI       | killed    | 1 (of 34)  | 0.211377s |
| lumberjack/device/rolling_log_file.98.rb         | UAOI       | killed    | 2 (of 34)  | 0.033097s |
| lumberjack/device/rolling_log_file.99.rb         | UAOI       | killed    | 11 (of 34) | 0.623285s |
| lumberjack/device/rolling_log_file.100.rb        | UAOI       | killed    | 1 (of 34)  | 0.029049s |
| lumberjack/device/rolling_log_file.101.rb        | UAOI       | killed    | 1 (of 34)  | 0.028131s |
| lumberjack/device/rolling_log_file.102.rb        | UAOI       | killed    | 1 (of 34)  | 0.028202s |
| lumberjack/device/rolling_log_file.103.rb        | UAOI       | killed    | 1 (of 34)  | 0.027344s |
| lumberjack/device/rolling_log_file.104.rb        | UAOI       | killed    | 1 (of 34)  | 0.027927s |
| lumberjack/device/rolling_log_file.105.rb        | UAOI       | killed    | 1 (of 34)  | 0.06907s  |
| lumberjack/device/rolling_log_file.106.rb        | UAOI       | killed    | 1 (of 34)  | 0.087839s |
| lumberjack/device/rolling_log_file.107.rb        | UAOI       | killed    | 11 (of 34) | 0.486091s |
| lumberjack/device/rolling_log_file.108.rb        | UAOI       | killed    | 7 (of 34)  | 0.198258s |
| lumberjack/device/rolling_log_file.109.rb        | UAOI       | killed    | 1 (of 34)  | 0.029623s |
| lumberjack/device/rolling_log_file.110.rb        | UAOI       | killed    | 1 (of 34)  | 0.026831s |
| lumberjack/device/rolling_log_file.111.rb        | UAOI       | killed    | 11 (of 34) | 0.531363s |
| lumberjack/device/rolling_log_file.112.rb        | UAOI       | killed    | 1 (of 34)  | 0.028937s |
| lumberjack/device/rolling_log_file.113.rb        | UAOI       | killed    | 1 (of 34)  | 0.029452s |
| lumberjack/device/rolling_log_file.114.rb        | UAOI       | killed    | 1 (of 34)  | 0.027645s |
| lumberjack/device/rolling_log_file.115.rb        | UAOI       | killed    | 1 (of 34)  | 0.032295s |
| lumberjack/device/rolling_log_file.116.rb        | UAOI       | killed    | 1 (of 34)  | 0.028414s |
| lumberjack/device/rolling_log_file.117.rb        | UAOI       | killed    | 1 (of 34)  | 0.029404s |
| lumberjack/device/rolling_log_file.118.rb        | UAOI       | killed    | 1 (of 34)  | 0.029535s |
| lumberjack/device/rolling_log_file.119.rb        | UAOI       | killed    | 11 (of 34) | 0.812782s |
| lumberjack/device/size_rolling_log_file.0.rb     | BAOR       | killed    | 1 (of 10)  | 0.062865s |
| lumberjack/device/size_rolling_log_file.1.rb     | BAOR       | killed    | 1 (of 10)  | 0.042104s |
| lumberjack/device/size_rolling_log_file.2.rb     | BAOR       | killed    | 1 (of 10)  | 0.030696s |
| lumberjack/device/size_rolling_log_file.3.rb     | BAOR       | killed    | 1 (of 10)  | 0.043871s |
| lumberjack/device/size_rolling_log_file.4.rb     | COI        | killed    | 1 (of 10)  | 0.028808s |
| lumberjack/device/size_rolling_log_file.5.rb     | COI        | killed    | 1 (of 10)  | 0.150623s |
| lumberjack/device/size_rolling_log_file.6.rb     | COI        | killed    | 1 (of 10)  | 0.031802s |
| lumberjack/device/size_rolling_log_file.7.rb     | COI        | killed    | 5 (of 10)  | 0.06088s  |
| lumberjack/device/size_rolling_log_file.8.rb     | COR        | survived  | 10 (of 10) | 0.014054s |
| lumberjack/device/size_rolling_log_file.9.rb     | COR        | killed    | 1 (of 10)  | 0.02919s  |
| lumberjack/device/size_rolling_log_file.10.rb    | RER        | killed    | 1 (of 10)  | 0.083682s |
| lumberjack/device/size_rolling_log_file.11.rb    | RER        | killed    | 1 (of 10)  | 0.046216s |
| lumberjack/device/size_rolling_log_file.12.rb    | RER        | killed    | 5 (of 10)  | 0.046881s |
| lumberjack/device/size_rolling_log_file.13.rb    | RER        | killed    | 1 (of 10)  | 0.052836s |
| lumberjack/device/size_rolling_log_file.14.rb    | ROR        | killed    | 1 (of 10)  | 0.027755s |
| lumberjack/device/size_rolling_log_file.15.rb    | ROR        | killed    | 1 (of 10)  | 0.057376s |
| lumberjack/device/size_rolling_log_file.16.rb    | ROR        | killed    | 1 (of 10)  | 0.030292s |
| lumberjack/device/size_rolling_log_file.17.rb    | ROR        | killed    | 1 (of 10)  | 0.053078s |
| lumberjack/device/size_rolling_log_file.18.rb    | ROR        | survived  | 10 (of 10) | 0.01222s  |
| lumberjack/device/size_rolling_log_file.19.rb    | ROR        | killed    | 5 (of 10)  | 0.053762s |
| lumberjack/device/size_rolling_log_file.20.rb    | ROR        | killed    | 1 (of 10)  | 0.054372s |
| lumberjack/device/size_rolling_log_file.21.rb    | ROR        | killed    | 5 (of 10)  | 0.048115s |
| lumberjack/device/size_rolling_log_file.22.rb    | ROR        | killed    | 5 (of 10)  | 0.057264s |
| lumberjack/device/size_rolling_log_file.23.rb    | ROR        | survived  | 10 (of 10) | 0.024262s |
| lumberjack/device/size_rolling_log_file.24.rb    | LOI        | killed    | 1 (of 10)  | 0.050876s |
| lumberjack/device/size_rolling_log_file.25.rb    | LOI        | killed    | 1 (of 10)  | 0.027266s |
| lumberjack/device/size_rolling_log_file.26.rb    | LOI        | killed    | 1 (of 10)  | 0.046582s |
| lumberjack/device/size_rolling_log_file.27.rb    | LOI        | killed    | 1 (of 10)  | 0.030728s |
| lumberjack/device/size_rolling_log_file.28.rb    | LOI        | killed    | 1 (of 10)  | 0.074993s |
| lumberjack/device/size_rolling_log_file.29.rb    | LOI        | killed    | 2 (of 10)  | 0.044646s |
| lumberjack/device/size_rolling_log_file.30.rb    | LOI        | killed    | 2 (of 10)  | 0.26777s  |
| lumberjack/device/size_rolling_log_file.31.rb    | LOI        | killed    | 1 (of 10)  | 0.059144s |
| lumberjack/device/size_rolling_log_file.32.rb    | LOI        | killed    | 3 (of 10)  | 0.059672s |
| lumberjack/device/size_rolling_log_file.33.rb    | LOI        | killed    | 3 (of 10)  | 0.054717s |
| lumberjack/device/size_rolling_log_file.34.rb    | LOI        | killed    | 4 (of 10)  | 0.043262s |
| lumberjack/device/size_rolling_log_file.35.rb    | LOI        | killed    | 1 (of 10)  | 0.059525s |
| lumberjack/device/size_rolling_log_file.36.rb    | SAOR       | killed    | 2 (of 10)  | 0.046202s |
| lumberjack/device/size_rolling_log_file.37.rb    | SAOR       | killed    | 2 (of 10)  | 0.057424s |
| lumberjack/device/size_rolling_log_file.38.rb    | SAOR       | killed    | 2 (of 10)  | 0.043147s |
| lumberjack/device/size_rolling_log_file.39.rb    | SAOR       | killed    | 1 (of 10)  | 0.058103s |
| lumberjack/device/size_rolling_log_file.40.rb    | SAOR       | killed    | 2 (of 10)  | 0.045296s |
| lumberjack/device/size_rolling_log_file.41.rb    | SAOR       | killed    | 2 (of 10)  | 0.123233s |
| lumberjack/device/size_rolling_log_file.42.rb    | SAOR       | killed    | 1 (of 10)  | 0.055991s |
| lumberjack/device/size_rolling_log_file.43.rb    | SAOR       | killed    | 2 (of 10)  | 0.033419s |
| lumberjack/device/size_rolling_log_file.44.rb    | SAOR       | killed    | 2 (of 10)  | 0.043839s |
| lumberjack/device/size_rolling_log_file.45.rb    | SAOR       | killed    | 2 (of 10)  | 0.03675s  |
| lumberjack/device/size_rolling_log_file.46.rb    | SAOR       | killed    | 1 (of 10)  | 0.149449s |
| lumberjack/device/size_rolling_log_file.47.rb    | SAOR       | killed    | 2 (of 10)  | 0.044978s |
| lumberjack/device/size_rolling_log_file.48.rb    | SAOR       | killed    | 3 (of 10)  | 0.054879s |
| lumberjack/device/size_rolling_log_file.49.rb    | SAOR       | killed    | 3 (of 10)  | 0.05065s  |
| lumberjack/device/size_rolling_log_file.50.rb    | SAOR       | killed    | 3 (of 10)  | 0.237451s |
| lumberjack/device/size_rolling_log_file.51.rb    | SAOR       | killed    | 3 (of 10)  | 0.053401s |
| lumberjack/device/size_rolling_log_file.52.rb    | SAOR       | killed    | 3 (of 10)  | 0.036828s |
| lumberjack/device/size_rolling_log_file.53.rb    | SAOR       | killed    | 1 (of 10)  | 0.058657s |
| lumberjack/device/size_rolling_log_file.54.rb    | SAOR       | killed    | 3 (of 10)  | 0.038537s |
| lumberjack/device/size_rolling_log_file.55.rb    | SAOR       | killed    | 3 (of 10)  | 0.049818s |
| lumberjack/device/size_rolling_log_file.56.rb    | SAOR       | killed    | 3 (of 10)  | 0.035811s |
| lumberjack/device/size_rolling_log_file.57.rb    | SAOR       | killed    | 1 (of 10)  | 0.059514s |
| lumberjack/device/size_rolling_log_file.58.rb    | SAOR       | killed    | 3 (of 10)  | 0.146324s |
| lumberjack/device/size_rolling_log_file.59.rb    | SAOR       | killed    | 3 (of 10)  | 0.058697s |
| lumberjack/device/size_rolling_log_file.60.rb    | SAOR       | killed    | 1 (of 10)  | 0.057007s |
| lumberjack/device/size_rolling_log_file.61.rb    | SAOR       | killed    | 4 (of 10)  | 0.045271s |
| lumberjack/device/size_rolling_log_file.62.rb    | SAOR       | killed    | 4 (of 10)  | 0.054083s |
| lumberjack/device/size_rolling_log_file.63.rb    | SAOR       | killed    | 4 (of 10)  | 0.266155s |
| lumberjack/device/size_rolling_log_file.64.rb    | SAOR       | killed    | 1 (of 10)  | 0.06644s  |
| lumberjack/device/size_rolling_log_file.65.rb    | SAOR       | killed    | 4 (of 10)  | 0.040116s |
| lumberjack/device/size_rolling_log_file.66.rb    | SAOR       | killed    | 4 (of 10)  | 0.050931s |
| lumberjack/device/size_rolling_log_file.67.rb    | SAOR       | killed    | 4 (of 10)  | 0.032189s |
| lumberjack/device/size_rolling_log_file.68.rb    | SAOR       | killed    | 1 (of 10)  | 0.057218s |
| lumberjack/device/size_rolling_log_file.69.rb    | SAOR       | killed    | 4 (of 10)  | 0.03812s  |
| lumberjack/device/size_rolling_log_file.70.rb    | SAOR       | survived  | 10 (of 10) | 0.013946s |
| lumberjack/device/size_rolling_log_file.71.rb    | SAOR       | killed    | 1 (of 10)  | 0.120233s |
| lumberjack/device/size_rolling_log_file.72.rb    | UAOI       | killed    | 1 (of 10)  | 0.029876s |
| lumberjack/device/size_rolling_log_file.73.rb    | UAOI       | killed    | 1 (of 10)  | 0.048737s |
| lumberjack/device/size_rolling_log_file.74.rb    | UAOI       | killed    | 1 (of 10)  | 0.027897s |
| lumberjack/device/size_rolling_log_file.75.rb    | UAOI       | killed    | 1 (of 10)  | 0.04633s  |
| lumberjack/device/size_rolling_log_file.76.rb    | UAOI       | killed    | 2 (of 10)  | 0.045797s |
| lumberjack/device/size_rolling_log_file.77.rb    | UAOI       | killed    | 2 (of 10)  | 0.056472s |
| lumberjack/device/size_rolling_log_file.78.rb    | UAOI       | killed    | 2 (of 10)  | 0.077556s |
| lumberjack/device/size_rolling_log_file.79.rb    | UAOI       | killed    | 1 (of 10)  | 0.059085s |
| lumberjack/device/size_rolling_log_file.80.rb    | UAOI       | killed    | 3 (of 10)  | 0.057336s |
| lumberjack/device/size_rolling_log_file.81.rb    | UAOI       | killed    | 4 (of 10)  | 0.040072s |
| lumberjack/device/size_rolling_log_file.82.rb    | UAOI       | killed    | 1 (of 10)  | 0.056949s |
| lumberjack/device/writer.0.rb                    | BAOR       | killed    | 10 (of 17) | 0.058585s |
| lumberjack/device/writer.1.rb                    | BAOR       | killed    | 10 (of 17) | 0.042514s |
| lumberjack/device/writer.2.rb                    | BAOR       | killed    | 10 (of 17) | 0.058177s |
| lumberjack/device/writer.3.rb                    | BAOR       | survived  | 17 (of 17) | 0.016218s |
| lumberjack/device/writer.4.rb                    | COI        | survived  | 17 (of 17) | 0.01278s  |
| lumberjack/device/writer.5.rb                    | COI        | survived  | 17 (of 17) | 0.017756s |
| lumberjack/device/writer.6.rb                    | COI        | survived  | 17 (of 17) | 0.015648s |
| lumberjack/device/writer.7.rb                    | COI        | survived  | 17 (of 17) | 0.01313s  |
| lumberjack/device/writer.8.rb                    | COI        | survived  | 17 (of 17) | 0.01406s  |
| lumberjack/device/writer.9.rb                    | COI        | killed    | 3 (of 17)  | 0.064838s |
| lumberjack/device/writer.10.rb                   | COI        | killed    | 1 (of 17)  | 0.049969s |
| lumberjack/device/writer.11.rb                   | COI        | survived  | 17 (of 17) | 0.014963s |
| lumberjack/device/writer.12.rb                   | COI        | survived  | 17 (of 17) | 0.013774s |
| lumberjack/device/writer.13.rb                   | COR        | killed    | 5 (of 17)  | 0.051729s |
| lumberjack/device/writer.14.rb                   | COR        | killed    | 1 (of 17)  | 0.06152s  |
| lumberjack/device/writer.15.rb                   | COR        | killed    | 1 (of 17)  | 0.039506s |
| lumberjack/device/writer.16.rb                   | COR        | killed    | 1 (of 17)  | 0.061859s |
| lumberjack/device/writer.17.rb                   | COR        | killed    | 1 (of 17)  | 0.02631s  |
| lumberjack/device/writer.18.rb                   | COR        | killed    | 11 (of 17) | 0.071694s |
| lumberjack/device/writer.19.rb                   | RER        | killed    | 1 (of 17)  | 0.051083s |
| lumberjack/device/writer.20.rb                   | RER        | killed    | 2 (of 17)  | 0.051364s |
| lumberjack/device/writer.21.rb                   | ROR        | killed    | 1 (of 17)  | 0.063878s |
| lumberjack/device/writer.22.rb                   | ROR        | killed    | 1 (of 17)  | 0.048682s |
| lumberjack/device/writer.23.rb                   | ROR        | killed    | 2 (of 17)  | 0.064174s |
| lumberjack/device/writer.24.rb                   | ROR        | killed    | 1 (of 17)  | 0.129283s |
| lumberjack/device/writer.25.rb                   | ROR        | survived  | 17 (of 17) | 0.013781s |
| lumberjack/device/writer.26.rb                   | LOI        | killed    | 4 (of 17)  | 0.041092s |
| lumberjack/device/writer.27.rb                   | LOI        | survived  | 17 (of 17) | 0.013922s |
| lumberjack/device/writer.28.rb                   | LOI        | survived  | 17 (of 17) | 0.044173s |
| lumberjack/device/writer.29.rb                   | LOI        | survived  | 17 (of 17) | 0.013687s |
| lumberjack/device/writer.30.rb                   | LOI        | killed    | 1 (of 17)  | 0.05101s  |
| lumberjack/device/writer.31.rb                   | LOI        | killed    | 1 (of 17)  | 0.056578s |
| lumberjack/device/writer.32.rb                   | LOI        | survived  | 17 (of 17) | 0.013644s |
| lumberjack/device/writer.33.rb                   | LOI        | survived  | 17 (of 17) | 0.016998s |
| lumberjack/device/writer.34.rb                   | LOI        | killed    | 5 (of 17)  | 0.060214s |
| lumberjack/device/writer.35.rb                   | LOI        | killed    | 3 (of 17)  | 0.054294s |
| lumberjack/device/writer.36.rb                   | LOI        | survived  | 17 (of 17) | 0.013668s |
| lumberjack/device/writer.37.rb                   | SAOR       | killed    | 2 (of 17)  | 0.047751s |
| lumberjack/device/writer.38.rb                   | SAOR       | killed    | 2 (of 17)  | 0.062165s |
| lumberjack/device/writer.39.rb                   | SAOR       | killed    | 2 (of 17)  | 0.050556s |
| lumberjack/device/writer.40.rb                   | SAOR       | killed    | 2 (of 17)  | 0.053013s |
| lumberjack/device/writer.41.rb                   | SAOR       | killed    | 2 (of 17)  | 0.055673s |
| lumberjack/device/writer.42.rb                   | SAOR       | killed    | 2 (of 17)  | 0.051677s |
| lumberjack/device/writer.43.rb                   | SAOR       | killed    | 2 (of 17)  | 0.066779s |
| lumberjack/device/writer.44.rb                   | SAOR       | killed    | 2 (of 17)  | 0.049809s |
| lumberjack/device/writer.45.rb                   | SAOR       | killed    | 2 (of 17)  | 0.055495s |
| lumberjack/device/writer.46.rb                   | SAOR       | killed    | 2 (of 17)  | 0.222802s |
| lumberjack/device/writer.47.rb                   | SAOR       | killed    | 2 (of 17)  | 0.062606s |
| lumberjack/device/writer.48.rb                   | SAOR       | killed    | 2 (of 17)  | 0.050596s |
| lumberjack/device/writer.49.rb                   | UAOI       | killed    | 4 (of 17)  | 0.053885s |
| lumberjack/device/writer.50.rb                   | UAOI       | survived  | 17 (of 17) | 0.013633s |
| lumberjack/device/writer.51.rb                   | UAOI       | survived  | 17 (of 17) | 0.015908s |
| lumberjack/device/writer.52.rb                   | UAOI       | survived  | 17 (of 17) | 0.011827s |
| lumberjack/device/writer.53.rb                   | UAOI       | killed    | 1 (of 17)  | 0.048166s |
| lumberjack/device/writer.54.rb                   | UAOI       | killed    | 1 (of 17)  | 0.061951s |
| lumberjack/device/writer.55.rb                   | UAOI       | killed    | 3 (of 17)  | 0.049556s |
| lumberjack/device/writer.56.rb                   | UAOI       | survived  | 17 (of 17) | 0.034172s |
| lumberjack/formatter.0.rb                        | RER        | stillborn | n/a        | n/a       |
| lumberjack/formatter.1.rb                        | RER        | stillborn | n/a        | n/a       |
| lumberjack/formatter.2.rb                        | ROR        | stillborn | n/a        | n/a       |
| lumberjack/formatter.3.rb                        | ROR        | stillborn | n/a        | n/a       |
| lumberjack/formatter.4.rb                        | ROR        | stillborn | n/a        | n/a       |
| lumberjack/formatter.5.rb                        | ROR        | stillborn | n/a        | n/a       |
| lumberjack/formatter.6.rb                        | ROR        | stillborn | n/a        | n/a       |
| lumberjack/formatter.7.rb                        | LOI        | stillborn | n/a        | n/a       |
| lumberjack/formatter.8.rb                        | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.9.rb                        | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.10.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.11.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.12.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.13.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.14.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.15.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.16.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.17.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.18.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.19.rb                       | SAOR       | stillborn | n/a        | n/a       |
| lumberjack/formatter.20.rb                       | UAOI       | stillborn | n/a        | n/a       |
| lumberjack/formatter/pretty_print_formatter.0.rb | LOI        | survived  | 6 (of 6)   | 0.007463s |
| lumberjack/formatter/pretty_print_formatter.1.rb | UAOI       | survived  | 6 (of 6)   | 0.0064s   |
| lumberjack/log_entry.0.rb                        | BAOR       | killed    | 9 (of 14)  | 0.046028s |
| lumberjack/log_entry.1.rb                        | BAOR       | killed    | 9 (of 14)  | 0.03789s  |
| lumberjack/log_entry.2.rb                        | BAOR       | killed    | 9 (of 14)  | 0.045772s |
| lumberjack/log_entry.3.rb                        | BAOR       | killed    | 9 (of 14)  | 0.043216s |
| lumberjack/log_entry.4.rb                        | COI        | survived  | 14 (of 14) | 0.010175s |
| lumberjack/log_entry.5.rb                        | COI        | killed    | 4 (of 14)  | 0.023405s |
| lumberjack/log_entry.6.rb                        | COI        | killed    | 9 (of 14)  | 0.039228s |
| lumberjack/log_entry.7.rb                        | COI        | killed    | 9 (of 14)  | 0.034186s |
| lumberjack/log_entry.8.rb                        | COI        | killed    | 9 (of 14)  | 0.040976s |
| lumberjack/log_entry.9.rb                        | COI        | killed    | 9 (of 14)  | 0.045885s |
| lumberjack/log_entry.10.rb                       | COI        | killed    | 9 (of 14)  | 0.04208s  |
| lumberjack/log_entry.11.rb                       | COI        | killed    | 9 (of 14)  | 0.033595s |
| lumberjack/log_entry.12.rb                       | COI        | killed    | 9 (of 14)  | 0.045112s |
| lumberjack/log_entry.13.rb                       | COI        | killed    | 9 (of 14)  | 0.033509s |
| lumberjack/log_entry.14.rb                       | LOI        | survived  | 14 (of 14) | 0.008998s |
| lumberjack/log_entry.15.rb                       | LOI        | killed    | 4 (of 14)  | 0.041213s |
| lumberjack/log_entry.16.rb                       | LOI        | killed    | 9 (of 14)  | 0.037634s |
| lumberjack/log_entry.17.rb                       | LOI        | killed    | 9 (of 14)  | 0.03329s  |
| lumberjack/log_entry.18.rb                       | LOI        | killed    | 9 (of 14)  | 0.033316s |
| lumberjack/log_entry.19.rb                       | LOI        | killed    | 9 (of 14)  | 0.033246s |
| lumberjack/log_entry.20.rb                       | LOI        | killed    | 9 (of 14)  | 0.043019s |
| lumberjack/log_entry.21.rb                       | LOI        | killed    | 9 (of 14)  | 0.03432s  |
| lumberjack/log_entry.22.rb                       | LOI        | killed    | 9 (of 14)  | 0.035744s |
| lumberjack/log_entry.23.rb                       | LOI        | killed    | 9 (of 14)  | 0.045988s |
| lumberjack/log_entry.24.rb                       | LOI        | killed    | 9 (of 14)  | 0.038666s |
| lumberjack/log_entry.25.rb                       | UAOI       | survived  | 14 (of 14) | 0.008523s |
| lumberjack/log_entry.26.rb                       | UAOI       | killed    | 4 (of 14)  | 0.042025s |
| lumberjack/log_entry.27.rb                       | UAOI       | killed    | 9 (of 14)  | 0.037924s |
| lumberjack/log_entry.28.rb                       | UAOI       | killed    | 9 (of 14)  | 0.034687s |
| lumberjack/log_entry.29.rb                       | UAOI       | killed    | 9 (of 14)  | 0.032845s |
| lumberjack/log_entry.30.rb                       | UAOI       | killed    | 9 (of 14)  | 0.036608s |
| lumberjack/log_entry.31.rb                       | UAOI       | killed    | 9 (of 14)  | 0.040664s |
| lumberjack/log_entry.32.rb                       | UAOI       | killed    | 9 (of 14)  | 0.033122s |
| lumberjack/log_entry.33.rb                       | UAOI       | killed    | 9 (of 14)  | 0.036054s |
| lumberjack/log_entry.34.rb                       | UAOI       | killed    | 9 (of 14)  | 0.04463s  |
| lumberjack/log_entry.35.rb                       | UAOI       | killed    | 9 (of 14)  | 0.038385s |
| lumberjack/log_entry.36.rb                       | UAOI       | killed    | 9 (of 14)  | 0.042035s |
| lumberjack/logger.0.rb                           | BAOR       | killed    | 30 (of 42) | 0.369993s |
| lumberjack/logger.1.rb                           | BAOR       | killed    | 30 (of 42) | 0.378206s |
| lumberjack/logger.2.rb                           | BAOR       | killed    | 30 (of 42) | 0.373693s |
| lumberjack/logger.3.rb                           | BAOR       | killed    | 30 (of 42) | 0.383526s |
| lumberjack/logger.4.rb                           | BAOR       | killed    | 19 (of 42) | 0.219262s |
| lumberjack/logger.5.rb                           | BAOR       | killed    | 19 (of 42) | 0.235074s |
| lumberjack/logger.6.rb                           | BAOR       | killed    | 19 (of 42) | 0.220498s |
| lumberjack/logger.7.rb                           | BAOR       | killed    | 19 (of 42) | 0.239162s |
| lumberjack/logger.8.rb                           | COI        | killed    | 30 (of 42) | 0.370531s |
| lumberjack/logger.9.rb                           | COI        | killed    | 30 (of 42) | 0.392605s |
| lumberjack/logger.10.rb                          | COI        | killed    | 30 (of 42) | 0.388109s |
| lumberjack/logger.11.rb                          | COI        | killed    | 30 (of 42) | 0.377914s |
| lumberjack/logger.12.rb                          | COI        | killed    | 30 (of 42) | 0.374336s |
| lumberjack/logger.13.rb                          | COI        | killed    | 30 (of 42) | 0.37722s  |
| lumberjack/logger.14.rb                          | COI        | killed    | 13 (of 42) | 0.072458s |
| lumberjack/logger.15.rb                          | COI        | killed    | 13 (of 42) | 0.070231s |
| lumberjack/logger.16.rb                          | COI        | killed    | 30 (of 42) | 0.373353s |
| lumberjack/logger.17.rb                          | COI        | killed    | 26 (of 42) | 0.377374s |
| lumberjack/logger.18.rb                          | COI        | killed    | 13 (of 42) | 0.059711s |
| lumberjack/logger.19.rb                          | COI        | killed    | 30 (of 42) | 0.375764s |
| lumberjack/logger.20.rb                          | COI        | killed    | 30 (of 42) | 0.391573s |
| lumberjack/logger.21.rb                          | COR        | killed    | 6 (of 42)  | 0.058464s |
| lumberjack/logger.22.rb                          | COR        | killed    | 6 (of 42)  | 0.068451s |
| lumberjack/logger.23.rb                          | COR        | killed    | 9 (of 42)  | 0.068908s |
| lumberjack/logger.24.rb                          | COR        | killed    | 9 (of 42)  | 0.073392s |
| lumberjack/logger.25.rb                          | COR        | killed    | 6 (of 42)  | 0.061064s |
| lumberjack/logger.26.rb                          | COR        | killed    | 6 (of 42)  | 0.075912s |
| lumberjack/logger.27.rb                          | COR        | killed    | 30 (of 42) | 0.375719s |
| lumberjack/logger.28.rb                          | COR        | killed    | 23 (of 42) | 0.374488s |
| lumberjack/logger.29.rb                          | COR        | killed    | 13 (of 42) | 0.061s    |
| lumberjack/logger.30.rb                          | COR        | killed    | 13 (of 42) | 0.067473s |
| lumberjack/logger.31.rb                          | COR        | killed    | 1 (of 42)  | 0.070465s |
| lumberjack/logger.32.rb                          | COR        | killed    | 4 (of 42)  | 0.054195s |
| lumberjack/logger.33.rb                          | RER        | killed    | 30 (of 42) | 0.384763s |
| lumberjack/logger.34.rb                          | RER        | killed    | 30 (of 42) | 0.374885s |
| lumberjack/logger.35.rb                          | RER        | killed    | 30 (of 42) | 0.398448s |
| lumberjack/logger.36.rb                          | RER        | killed    | 30 (of 42) | 0.37642s  |
| lumberjack/logger.37.rb                          | RER        | killed    | 30 (of 42) | 0.382471s |
| lumberjack/logger.38.rb                          | RER        | killed    | 30 (of 42) | 0.37356s  |
| lumberjack/logger.39.rb                          | RER        | killed    | 30 (of 42) | 0.40064s  |
| lumberjack/logger.40.rb                          | RER        | killed    | 30 (of 42) | 0.377017s |
| lumberjack/logger.41.rb                          | RER        | killed    | 30 (of 42) | 0.369194s |
| lumberjack/logger.42.rb                          | RER        | killed    | 30 (of 42) | 0.396413s |
| lumberjack/logger.43.rb                          | RER        | killed    | 30 (of 42) | 0.378195s |
| lumberjack/logger.44.rb                          | RER        | killed    | 10 (of 42) | 0.059824s |
| lumberjack/logger.45.rb                          | RER        | killed    | 30 (of 42) | 0.368754s |
| lumberjack/logger.46.rb                          | RER        | killed    | 10 (of 42) | 0.066534s |
| lumberjack/logger.47.rb                          | RER        | killed    | 13 (of 42) | 0.058283s |
| lumberjack/logger.48.rb                          | RER        | killed    | 13 (of 42) | 0.079731s |
| lumberjack/logger.49.rb                          | RER        | killed    | 3 (of 42)  | 0.064056s |
| lumberjack/logger.50.rb                          | RER        | killed    | 5 (of 42)  | 0.064657s |
| lumberjack/logger.51.rb                          | RER        | killed    | 30 (of 42) | 0.380784s |
| lumberjack/logger.52.rb                          | RER        | killed    | 19 (of 42) | 0.217525s |
| lumberjack/logger.53.rb                          | ROR        | killed    | 30 (of 42) | 0.398289s |
| lumberjack/logger.54.rb                          | ROR        | killed    | 30 (of 42) | 0.404972s |
| lumberjack/logger.55.rb                          | ROR        | killed    | 30 (of 42) | 0.38789s  |
| lumberjack/logger.56.rb                          | ROR        | killed    | 30 (of 42) | 0.376413s |
| lumberjack/logger.57.rb                          | ROR        | killed    | 30 (of 42) | 0.401023s |
| lumberjack/logger.58.rb                          | ROR        | killed    | 30 (of 42) | 0.39135s  |
| lumberjack/logger.59.rb                          | ROR        | killed    | 30 (of 42) | 0.386803s |
| lumberjack/logger.60.rb                          | ROR        | killed    | 30 (of 42) | 0.398402s |
| lumberjack/logger.61.rb                          | ROR        | killed    | 30 (of 42) | 0.374591s |
| lumberjack/logger.62.rb                          | ROR        | killed    | 30 (of 42) | 0.388513s |
| lumberjack/logger.63.rb                          | ROR        | killed    | 30 (of 42) | 0.373676s |
| lumberjack/logger.64.rb                          | ROR        | killed    | 30 (of 42) | 0.39853s  |
| lumberjack/logger.65.rb                          | ROR        | killed    | 30 (of 42) | 0.371348s |
| lumberjack/logger.66.rb                          | ROR        | killed    | 30 (of 42) | 0.389827s |
| lumberjack/logger.67.rb                          | ROR        | killed    | 30 (of 42) | 0.368357s |
| lumberjack/logger.68.rb                          | ROR        | killed    | 30 (of 42) | 0.395689s |
| lumberjack/logger.69.rb                          | ROR        | killed    | 30 (of 42) | 0.366746s |
| lumberjack/logger.70.rb                          | ROR        | killed    | 30 (of 42) | 0.367666s |
| lumberjack/logger.71.rb                          | ROR        | killed    | 30 (of 42) | 0.397901s |
| lumberjack/logger.72.rb                          | ROR        | killed    | 30 (of 42) | 0.369006s |
| lumberjack/logger.73.rb                          | ROR        | killed    | 30 (of 42) | 0.385692s |
| lumberjack/logger.74.rb                          | ROR        | killed    | 30 (of 42) | 0.369903s |
| lumberjack/logger.75.rb                          | ROR        | killed    | 30 (of 42) | 0.396288s |
| lumberjack/logger.76.rb                          | ROR        | killed    | 30 (of 42) | 0.36847s  |
| lumberjack/logger.77.rb                          | ROR        | killed    | 30 (of 42) | 0.384236s |
| lumberjack/logger.78.rb                          | ROR        | killed    | 10 (of 42) | 0.058373s |
| lumberjack/logger.79.rb                          | ROR        | killed    | 10 (of 42) | 0.066963s |
| lumberjack/logger.80.rb                          | ROR        | killed    | 10 (of 42) | 0.06593s  |
| lumberjack/logger.81.rb                          | ROR        | killed    | 30 (of 42) | 0.374199s |
| lumberjack/logger.82.rb                          | ROR        | killed    | 30 (of 42) | 0.391083s |
| lumberjack/logger.83.rb                          | ROR        | killed    | 10 (of 42) | 0.044381s |
| lumberjack/logger.84.rb                          | ROR        | killed    | 10 (of 42) | 0.065929s |
| lumberjack/logger.85.rb                          | ROR        | killed    | 10 (of 42) | 0.054843s |
| lumberjack/logger.86.rb                          | ROR        | killed    | 30 (of 42) | 0.391785s |
| lumberjack/logger.87.rb                          | ROR        | killed    | 30 (of 42) | 0.367785s |
| lumberjack/logger.88.rb                          | ROR        | killed    | 13 (of 42) | 0.074034s |
| lumberjack/logger.89.rb                          | ROR        | killed    | 13 (of 42) | 0.061249s |
| lumberjack/logger.90.rb                          | ROR        | killed    | 15 (of 42) | 0.052919s |
| lumberjack/logger.91.rb                          | ROR        | killed    | 13 (of 42) | 0.074435s |
| lumberjack/logger.92.rb                          | ROR        | killed    | 13 (of 42) | 0.064542s |
| lumberjack/logger.93.rb                          | ROR        | killed    | 3 (of 42)  | 0.074131s |
| lumberjack/logger.94.rb                          | ROR        | killed    | 3 (of 42)  | 0.047667s |
| lumberjack/logger.95.rb                          | ROR        | killed    | 3 (of 42)  | 0.072534s |
| lumberjack/logger.96.rb                          | ROR        | killed    | 3 (of 42)  | 0.051884s |
| lumberjack/logger.97.rb                          | ROR        | killed    | 3 (of 42)  | 0.063723s |
| lumberjack/logger.98.rb                          | ROR        | killed    | 19 (of 42) | 0.211426s |
| lumberjack/logger.99.rb                          | ROR        | killed    | 19 (of 42) | 0.231857s |
| lumberjack/logger.100.rb                         | ROR        | killed    | 19 (of 42) | 0.224898s |
| lumberjack/logger.101.rb                         | ROR        | killed    | 30 (of 42) | 0.376167s |
| lumberjack/logger.102.rb                         | ROR        | killed    | 30 (of 42) | 0.3812s   |
| lumberjack/logger.103.rb                         | LOI        | killed    | 17 (of 42) | 0.066705s |
| lumberjack/logger.104.rb                         | LOI        | killed    | 30 (of 42) | 0.37896s  |
| lumberjack/logger.105.rb                         | LOI        | killed    | 30 (of 42) | 0.377185s |
| lumberjack/logger.106.rb                         | LOI        | killed    | 30 (of 42) | 0.378877s |
| lumberjack/logger.107.rb                         | LOI        | killed    | 30 (of 42) | 0.386792s |
| lumberjack/logger.108.rb                         | LOI        | killed    | 30 (of 42) | 0.384307s |
| lumberjack/logger.109.rb                         | LOI        | killed    | 13 (of 42) | 0.061045s |
| lumberjack/logger.110.rb                         | LOI        | killed    | 17 (of 42) | 0.059316s |
| lumberjack/logger.111.rb                         | LOI        | killed    | 30 (of 42) | 0.383354s |
| lumberjack/logger.112.rb                         | LOI        | killed    | 30 (of 42) | 0.379619s |
| lumberjack/logger.113.rb                         | LOI        | killed    | 26 (of 42) | 0.374462s |
| lumberjack/logger.114.rb                         | LOI        | killed    | 13 (of 42) | 0.076201s |
| lumberjack/logger.115.rb                         | LOI        | killed    | 30 (of 42) | 0.385935s |
| lumberjack/logger.116.rb                         | LOI        | killed    | 30 (of 42) | 0.379952s |
| lumberjack/logger.117.rb                         | SAOR       | killed    | 13 (of 42) | 0.061966s |
| lumberjack/logger.118.rb                         | SAOR       | killed    | 13 (of 42) | 0.06411s  |
| lumberjack/logger.119.rb                         | SAOR       | killed    | 13 (of 42) | 0.054533s |
| lumberjack/logger.120.rb                         | SAOR       | killed    | 13 (of 42) | 0.062032s |
| lumberjack/logger.121.rb                         | SAOR       | killed    | 13 (of 42) | 0.058688s |
| lumberjack/logger.122.rb                         | SAOR       | killed    | 13 (of 42) | 0.059963s |
| lumberjack/logger.123.rb                         | SAOR       | killed    | 18 (of 42) | 0.074583s |
| lumberjack/logger.124.rb                         | SAOR       | killed    | 18 (of 42) | 0.073438s |
| lumberjack/logger.125.rb                         | SAOR       | killed    | 18 (of 42) | 0.077787s |
| lumberjack/logger.126.rb                         | SAOR       | killed    | 13 (of 42) | 0.059742s |
| lumberjack/logger.127.rb                         | SAOR       | killed    | 13 (of 42) | 0.057999s |
| lumberjack/logger.128.rb                         | SAOR       | killed    | 18 (of 42) | 0.073847s |
| lumberjack/logger.129.rb                         | UAOI       | killed    | 17 (of 42) | 0.066497s |
| lumberjack/logger.130.rb                         | UAOI       | killed    | 30 (of 42) | 0.380838s |
| lumberjack/logger.131.rb                         | UAOI       | killed    | 30 (of 42) | 0.374391s |
| lumberjack/logger.132.rb                         | UAOI       | killed    | 30 (of 42) | 0.397178s |
| lumberjack/logger.133.rb                         | UAOI       | killed    | 30 (of 42) | 0.375828s |
| lumberjack/logger.134.rb                         | UAOI       | killed    | 30 (of 42) | 0.37668s  |
| lumberjack/logger.135.rb                         | UAOI       | killed    | 13 (of 42) | 0.058884s |
| lumberjack/logger.136.rb                         | UAOI       | killed    | 17 (of 42) | 0.068345s |
| lumberjack/logger.137.rb                         | UAOI       | killed    | 26 (of 42) | 0.371022s |
| lumberjack/logger.138.rb                         | UAOI       | killed    | 13 (of 42) | 0.081864s |
| lumberjack/logger.139.rb                         | UAOI       | killed    | 13 (of 42) | 0.061045s |
| lumberjack/logger.140.rb                         | UAOI       | killed    | 30 (of 42) | 0.380246s |
| lumberjack/template.0.rb                         | BAOR       | killed    | 6 (of 10)  | 0.026612s |
| lumberjack/template.1.rb                         | BAOR       | killed    | 6 (of 10)  | 0.029727s |
| lumberjack/template.2.rb                         | BAOR       | killed    | 6 (of 10)  | 0.02714s  |
| lumberjack/template.3.rb                         | BAOR       | killed    | 6 (of 10)  | 0.026848s |
| lumberjack/template.4.rb                         | BAOR       | killed    | 6 (of 10)  | 0.025926s |
| lumberjack/template.5.rb                         | BAOR       | killed    | 6 (of 10)  | 0.028208s |
| lumberjack/template.6.rb                         | BAOR       | killed    | 6 (of 10)  | 0.026237s |
| lumberjack/template.7.rb                         | BAOR       | killed    | 6 (of 10)  | 0.032601s |
| lumberjack/template.8.rb                         | BAOR       | killed    | 6 (of 10)  | 0.027332s |
| lumberjack/template.9.rb                         | BAOR       | killed    | 6 (of 10)  | 0.027379s |
| lumberjack/template.10.rb                        | BAOR       | killed    | 6 (of 10)  | 0.034428s |
| lumberjack/template.11.rb                        | BAOR       | killed    | 6 (of 10)  | 0.026763s |
| lumberjack/template.12.rb                        | BAOR       | killed    | 7 (of 10)  | 0.028974s |
| lumberjack/template.13.rb                        | BAOR       | killed    | 7 (of 10)  | 0.032258s |
| lumberjack/template.14.rb                        | BAOR       | killed    | 7 (of 10)  | 0.055645s |
| lumberjack/template.15.rb                        | BAOR       | killed    | 7 (of 10)  | 0.028531s |
| lumberjack/template.16.rb                        | BAOR       | killed    | 6 (of 10)  | 0.025225s |
| lumberjack/template.17.rb                        | BAOR       | killed    | 6 (of 10)  | 0.030136s |
| lumberjack/template.18.rb                        | BAOR       | killed    | 6 (of 10)  | 0.023759s |
| lumberjack/template.19.rb                        | BAOR       | killed    | 6 (of 10)  | 0.028458s |
| lumberjack/template.20.rb                        | BAOR       | killed    | 6 (of 10)  | 0.037683s |
| lumberjack/template.21.rb                        | BAOR       | killed    | 6 (of 10)  | 0.032558s |
| lumberjack/template.22.rb                        | BAOR       | killed    | 6 (of 10)  | 0.036031s |
| lumberjack/template.23.rb                        | BAOR       | killed    | 6 (of 10)  | 0.038478s |
| lumberjack/template.24.rb                        | COR        | killed    | 6 (of 10)  | 0.029864s |
| lumberjack/template.25.rb                        | COR        | killed    | 6 (of 10)  | 0.024873s |
| lumberjack/template.26.rb                        | COR        | survived  | 10 (of 10) | 0.007697s |
| lumberjack/template.27.rb                        | COR        | killed    | 6 (of 10)  | 0.032504s |
| lumberjack/template.28.rb                        | COR        | killed    | 6 (of 10)  | 0.03798s  |
| lumberjack/template.29.rb                        | COR        | killed    | 6 (of 10)  | 0.030004s |
| lumberjack/template.30.rb                        | RER        | killed    | 7 (of 10)  | 0.034531s |
| lumberjack/template.31.rb                        | RER        | killed    | 6 (of 10)  | 0.039819s |
| lumberjack/template.32.rb                        | ROR        | killed    | 6 (of 10)  | 0.035005s |
| lumberjack/template.33.rb                        | ROR        | killed    | 7 (of 10)  | 0.036146s |
| lumberjack/template.34.rb                        | ROR        | killed    | 6 (of 10)  | 0.036642s |
| lumberjack/template.35.rb                        | ROR        | survived  | 10 (of 10) | 0.009347s |
| lumberjack/template.36.rb                        | ROR        | killed    | 6 (of 10)  | 0.030394s |
| lumberjack/template.37.rb                        | LOI        | killed    | 6 (of 10)  | 0.027855s |
| lumberjack/template.38.rb                        | UAOI       | killed    | 6 (of 10)  | 0.025358s |
| lumberjack/template.39.rb                        | UAOI       | killed    | 6 (of 10)  | 0.038565s |
+--------------------------------------------------+------------+-----------+------------+-----------+
```

\normalsize
