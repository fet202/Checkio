def find_message(text: str) -> str:
    res = ''
    for let in text:
      if let.istitle():
            res = res + let
    return res

    print(res)





find_message("Heloooooo World")

