# Precomputed Alice win outcomes for each initial stone count (50 down to 0).
_WINNER_MASK = (
    # [49, 50] stones: Bob fails turn 8 (needs 3).
    (0b11 << 49)
    # [45, 48] stones: Alice fails turn 7 (needs 4).
    | (0b0000 << 45)
    # [40, 44] stones: Bob fails turn 6 (needs 5).
    | (0b11111 << 40)
    # [34, 39] stones: Alice fails turn 5 (needs 6).
    | (0b000000 << 34)
    # [27, 33] stones: Bob fails turn 4 (needs 7).
    | (0b1111111 << 27)
    # [19, 26] stones: Alice fails turn 3 (needs 8).
    | (0b00000000 << 19)
    # [10, 18] stones: Bob fails turn 2 (needs 9).
    | (0b111111111 << 10)
    # [0, 9] stones: Alice fails turn 1 (needs 10).
    | 0b0000000000
)


class Solution:
    def canAliceWin(self, n: int) -> bool:
        # 1. Check if the starting stone count forces Bob to fail a turn.
        is_alice_winner = bool((_WINNER_MASK >> n) & 1)

        return is_alice_winner