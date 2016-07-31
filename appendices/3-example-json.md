\clearpage

# Appendix 3: Example JSON report for the Mutiny demo application {-}

A rather heavily abbreviated version of the JSON report sent to the cloud component after testing the Mutiny demo application (as described in Appendix 2) is given below. Only a representative sample of the 19 mutants generated are given, and, within the entry for each mutant, the full contents of the original and mutant files have been elided. The schema governing this document follows in Appendix 4.

```{.json}
{
    "timestamp": 1461060110,
    "results": [
        {
            "total_tests": 5,
            "time": 0.039179,
            "target": "Demo::Palindrome",
            "status": "killed",
            "name": "demo/palindrome.0.rb",
            "original": "[removed for brevity]",
            "mutant": "[removed for brevity]",
            "operator": "COI",
            "tests": 1
        },
        {
            "total_tests": 5,
            "time": 0.038299,
            "target": "Demo::Palindrome",
            "status": "killed",
            "name": "demo/palindrome.1.rb",
            "original": "[removed for brevity]",
            "mutant": "[removed for brevity]",
            "operator": "COR",
            "tests": 2
        },
        {
            "total_tests": 5,
            "time": 0.037137,
            "target": "Demo::Palindrome",
            "status": "killed",
            "name": "demo/palindrome.2.rb",
            "original": "[removed for brevity]",
            "mutant": "[removed for brevity]",
            "operator": "COR",
            "tests": 4
        },
        {
            "total_tests": 5,
            "time": 0.002894,
            "target": "Demo::Palindrome",
            "status": "survived",
            "name": "demo/palindrome.7.rb",
            "original": "[removed for brevity]",
            "mutant": "[removed for brevity]",
            "operator": "ROR",
            "tests": 5
        }
    ],
    "killed_mutants": 17,
    "total_mutants": 19,
    "percentage_score": 89,
    "ci": false
}
```
