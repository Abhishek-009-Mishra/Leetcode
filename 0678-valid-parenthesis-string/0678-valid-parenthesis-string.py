class Solution:
  def checkValidString(self, s: str) -> bool:
    opens, stars = [], []

    for i, ch in enumerate(s):
      if ch == '(':
        opens.append(i)
      elif ch == '*':
        stars.append(i)
      elif opens: # ch is ')', close the nearest '('
        opens.pop()
      elif stars: # no '(' available, use a star as '('
        stars.pop()
      else:
        return False

    # leftover '(' must be closed by a later '*'
    while opens and stars and opens[-1] < stars[-1]:
      opens.pop()
      stars.pop()

    return not opens