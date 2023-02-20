a = str(input("Masukan kata kata: "))

kata = dict()

for key in a.split():
    if key in kata:
        kata.update({
            key: kata[key] + 1
        })
    else:
        kata[key] = 1

print("Output:")


kataUNIK = 0
for x in kata:
    kataUNIK = kataUNIK + kata[x]
    print(f"{x} = {kata[x]}")

print(f"total kata  = {kataUNIK}")
print(f"total kata unik = {len(kata)}")
