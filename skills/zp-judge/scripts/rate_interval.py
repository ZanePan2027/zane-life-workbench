#!/usr/bin/env python3
"""Wilson 95% interval for a small-sample rate, so a few clicks are not read as a trend.

    python3 rate_interval.py 5 115              # 5 likes out of 115 plays
    python3 rate_interval.py 5 115 --baseline 1 # also say whether a 1% reference line is inside the interval
"""
import math, sys

def wilson(k, n, z=1.96):
    if n <= 0 or k < 0 or k > n:
        raise ValueError("need 0 <= k <= n and n > 0")
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, max(0.0, c - m), min(1.0, c + m)

def main(a):
    base = None
    if "--baseline" in a:
        i = a.index("--baseline"); base = float(a[i + 1]) / 100; del a[i:i + 2]
    k, n = int(a[0]), int(a[1])
    p, lo, hi = wilson(k, n)
    print(f"{k}/{n} = {p:.1%}，95% 区间 {lo:.1%}～{hi:.1%}")
    if n < 300:
        print("样本 < 300：区间很宽。只有整个区间都落在参照线的同一侧，结论才算数；否则只能说“没有坏信号”或“分不出”。")
    if base is not None:
        if lo > base: print(f"区间下限高于参照线 {base:.1%}：高于参照线的判断站得住（仍是单条、短窗口）。")
        elif hi < base: print(f"区间上限低于参照线 {base:.1%}：低于参照线的判断站得住。")
        else: print(f"参照线 {base:.1%} 落在区间内：这条数据分不出高低。")

if __name__ == "__main__":
    if len(sys.argv) < 3: sys.exit(__doc__)
    main(sys.argv[1:])
