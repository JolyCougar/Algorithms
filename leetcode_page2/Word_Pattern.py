class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        w2p, p2w = {}, {}
        for p, w in zip(pattern, words):
            if w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                return False
        return True


# -----------------------------------------
# s = s.split()
# return (len(set(pattern)) ==
#         len(set(s)) ==
#         len(set(zip_longest(pattern, s))))
