import random

done = {
    4: [],
    5: [],
    6: [],
    7: [8],
    8: [],
    9: [1],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: []
}

size = {
    4: 11,
    5: 20,
    6: 13,
    7: 13,
    8: 9,
    9: 16,
    10: 6,
    11: 10,
    12: 12,
    13: 12,
    14: 11,
    15: 10,
    16: 12,
    17: 8,
    18: 8
}


def gen():
    all_questions = []
    for cap in range(4, 19):
        for qn in range(1, size[cap] + 1):
            if qn not in done[cap]:
                all_questions.append(f"{cap}.{qn}")
    print(random.choice(all_questions))


gen()