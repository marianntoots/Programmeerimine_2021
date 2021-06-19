
w, h, d = map(int, input("Sisesta kujundi mõõdud -> Laius x Kõrgus x Sügavus: ").split("x"))

move_right = True
right_space = 0

print(" " * h + "_" * (2 * w + 1))
for i in range(0, h):
    filler = "_" if i == h-1 else " "
    print(" " * (h - i - 1) + "/" + filler*(2*w) + "/", end="")
    if d-i > 0:
        print(" " * (2*i) + "\\", end="")
    else:
        print(" " * (2*d-1) + "/", end="")
    print()

for i in range(0, d):
    filler = "_" if i == d-1 else " "
    print(" " * i + "\\" + filler * (2 * w) + "\\", end="")
    if d > h + i:
        print(" " * (2*h-1) + "\\", end="")
    else:
        print(" " * 2*(d-i-1) + "/", end="")
    print()
