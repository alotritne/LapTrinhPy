def cipherText2PlainText(cipherText: str) -> str:
    plainText: str = ""
    cnt: int = 0
    isCipherText: bool = False
    for i in range(0, len(cipherText)):
        if cipherText[i] == "#":
            isCipherText = True
            continue
        if isCipherText:
            cnt = int(cipherText[i])
            for _ in range(1, cnt):
                plainText += str(cipherText[i + 1])
                isCipherText = False
        else:
            plainText += str(cipherText[i])
            isCipherText = False
    return plainText

print(cipherText2PlainText("XY#6Z1#4023"))