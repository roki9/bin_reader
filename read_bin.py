with open("input.txt", "rb") as fb:
    byte = list(fb.read())

byteOK = [byte[x] for x in range(len(byte)) if ((byte[x] >> 4) % 2 == (byte[x] & 1)) and (byte[x] >> 4 << 3 != byte[x] >> 1) ]

with open("output.txt", "w") as fw:
    fw.write(str(len(byte)) + "\n")
    fw.write(str(len(byte) - len(byteOK)) + "\n")

with open("output.txt", "ab") as fw:
    fw.write(bytearray(byteOK))
