\clearpage

# Appendix 4: Schema for JSON reports {-}

The schema below follows the specification given at http://json-schema.org/documentation.html.

\footnotesize

```{.json}
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Schema for MultiMutiny reports",
  "type": "object",
  "properties": {
    "killed_mutants": {
      "type": "integer"
    },
    "total_mutants": {
      "type": "integer"
    },
    "percentage_score": {
      "type": "integer"
    },
    "timestamp": {
      "type": "integer"
    },
    "ci": {
        "type": ["boolean", "object"],
        "properties": {
            "passed": {
                "type": "boolean"
            },
            "threshold": {
                "type": "integer"
            }
        },
        "additionalProperties": false
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "operator": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "pattern": "^(killed|survived|stillborn)$"
          },
          "tests": {
            "type": ["integer", "null"]
          },
          "total_tests": {
            "type": ["integer", "null"]
          },
          "time": {
            "type": ["number", "null"]
          },
          "target": {
            "type": "string"
          },
          "original": {
            "type": "string"
          },
          "mutant": {
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false,
  "required": ["timestamp", "killed_mutants", "total_mutants", "results", "percentage_score", "ci"]
}
```

\normalsize
