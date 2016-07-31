#!/usr/bin/env python3

mutant_times = [
    0.041930,
    0.042936,
    0.044003,
    0.039877,
    0.040465,
    0.041161,
    0.038068,
    0.036082,
    0.039850,
    0.035455,
    0.038636,
    0.038325,
    0.039776,
    0.046286,
    0.039437,
    0.027894,
    0.040467,
    0.032095,
    0.027813,
    0.027666,
    0.042332,
    0.027737,
    0.028771,
    0.028366,
    0.029405,
    0.029342,
    0.026229,
    0.028093,
    0.030884,
    0.027865,
    0.026223,
    0.027676,
    0.026059,
    0.026222,
    0.029065,
    0.032234,
    0.027367,
    0.028659,
    0.026948,
    0.028032,
    0.027033,
    0.028182,
    0.028905,
    0.028302,
    0.027506,
    0.027445,
    0.026962,
    0.026493,
    0.027020,
    0.029148,
    0.028640
]

allocation = [[], [], [], []]
totals = [0, 0, 0, 0]

def proc_with_soonest_finish():
    proc = 0
    current_lowest = totals[0]
    for index, total in enumerate(totals[1:]):
        if total < current_lowest:
            proc = index + 1
            current_lowest = total
    return proc

descending_mutants = sorted(list(enumerate(mutant_times)), reverse=True, key=lambda x: x[1])

for m in descending_mutants:
    proc = proc_with_soonest_finish()
    allocation[proc].append(m[0])
    totals[proc] += m[1]

for a in allocation:
    a.sort()

print("Total time: {}".format(max(totals)))
print("Allocation:")
print(allocation)
