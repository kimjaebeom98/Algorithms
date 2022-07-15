def solution(phone_book):
    chk = {}
    for i in phone_book:
      if i not in chk:
        chk[i] = 1

    for i in range(len(phone_book)):
      s = ''
      for j in range(len(phone_book[i])):
        s += phone_book[i][j]
        if s == phone_book[i]:
          break
        if s in chk:
          return False

      chk[i] = 1
    
    return True