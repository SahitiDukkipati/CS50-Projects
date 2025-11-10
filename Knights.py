## Part of CS50’s AI project: Knights
## This section includes my implementation for the logical reasoning setup.
## Only my written logic is shared here, not the full project framework.


knowledge1 = And(Or(AKnight,AKnave),
                 Or(BKnight,BKnave),
                 Not(And(AKnight,AKnave)),
                 Not(And(BKnight,BKnave)),
Implication(AKnight,And(AKnave,BKnave)),
Implication(AKnave,Not(And(AKnave,BKnave)))               
)              

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(Or(AKnight,AKnave),Or(BKnight,BKnave),
                 Not(And(AKnight, AKnave)),
                 Not(And(BKnight, BKnave)),
# A's statement: "We are the same kind."
    # → means (A and B are both knights) OR (A and B are both knaves)
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # B's statement: "We are of different kinds."
    # → means (A is knight, B is knave) OR (A is knave, B is knight)
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
) 


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."


knowledge3 =  And(
    # Base rules: each is either a knight or knave, not both
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # A says either "I am a knight" or "I am a knave"
    # Represent both possibilities
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # B’s statements:
    # 1. "A said 'I am a knave'"
    # 2. "C is a knave"
    # So if B is a knight → both must be true.
    Implication(BKnight, And(AKnave, CKnave)),
    # If B is a knave → at least one of them must be false.
    Implication(BKnave, Not(And(AKnave, CKnave))),

    # C’s statement: "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)
