""" 
  FreeCodeCamp -  boilerplate-arithmetic-formatter
  author: Cornelius Brooks (cbedroid) 
  github: https://github.com/cbedroid
  twitter: http://twitter.com/cbedroid
"""

def arithmetic_arranger(problems,show_answers=False):
  
  accepted_operation = ['-','+']
  col_1   = "" # First numbers
  col_2   = "" # Second numbers
  col_3   = "" # Dash divider
  answers = "" # Answer results
  
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    numbers = None
    for operator in accepted_operation:
      if operator in problem:
        numbers = problem.split(operator)

        ##- CHECKING FOR ERRORS -##
        for x in numbers:
          x = x.strip()
          if len(x) > 4:
            return "Error: Numbers cannot be more than four digits."
          if not x.isnumeric():
            return "Error: Numbers must only contain digits."

        # Cleaning data 
        fn = numbers[0].strip()
        sn = numbers[1].strip()

        ##- SETTING THE LENGTH OF EACH NUMBERS -##
        fnl = len(fn)
        snl = len(sn)
        spaces = fnl + 2 if fnl > snl else snl + 2 

        ##-- CALCULATING RESULTS(ANSWERS) -##
        if operator == "-":
          results = int(fn) - int(sn)
        else:
          results = int(fn) + int(sn)
        results = str(results)

        ##- SPACING FORMAT ALGORITHM -##
        ts = 2 if fnl >= snl else snl + 1 # first number 
        bs = 1  if snl >= fnl else fnl - snl + 1 # second number
        rs = " " if "-" in results else " " * 2 # answers  

        ##- COMBINING SPACES AND RESULTS  -##
        if show_answers: 
          # add extra padding to the back
          col_1 += " " * (ts-1) + fn +" " * 5
        else: 
          # add extra padding to the front 
          col_1 += " " * ts + fn + " " * 4

        col_2  += operator + " " * bs + sn +" " * 4
        col_3  += "-" * spaces +"    " 
        answers += rs + results + " " * 4

        continue

    if numbers is None: #Check for none in the first loop 
      return "Error: Operator must be '+' or '-'."
      

  ##- COMBINING FORMATTED RESULTS -##
  if show_answers:
    return "\n".join((col_1.rstrip(),col_2.rstrip(),col_3.rstrip(),answers.rstrip()))
  else:
    return "\n".join((col_1.rstrip(),col_2.rstrip(),col_3.rstrip()))
