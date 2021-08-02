ENCODING = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

MAX_IDX = 1073741824

def id_to_link(idx: int) -> str:
    assert (0 <= idx < MAX_IDX)
    s = ""
    mask = 0x3f
    for i in range(5):
        t = (idx & (mask << i*6)) >> (i*6)
        s += ENCODING[t]
    return s


def link_to_id(link: str) -> int:
    assert(len(link) == 5)
    res = 0
    for c in reversed(link):
        res = res << 6
        idx = ENCODING.index(c)
        res = res | idx

    return res

