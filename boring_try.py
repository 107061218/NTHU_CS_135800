輸入 = input
印出 = print
字元編碼 = ord

原始字串 = 輸入()
字串分離 = 原始字串.split()
for 單一字串 in 字串分離:
    if 字元編碼('A') <= 字元編碼(單一字串[0]) <= 字元編碼('Z'):
        if '.' in 單一字串:
            印出(單一字串[:-1])
        else:
            印出(單一字串)
