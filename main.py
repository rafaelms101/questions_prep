import random

done = [7.8, 9.1, 16.11, 15.4]

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
            question = f"{cap}.{qn}"
            if question not in done:
                all_questions.append(question)
    print(random.choice(all_questions))


gen()