nric = input('Enter an NRIC number: ')
nric_num = nric[1:-1]
nric = nric.upper()

if len(nric) != 9:
  print('NRIC is invalid.')
elif not nric[0] in "STFG":
  print('NRIC is invalid.')
elif not nric_num.isdigit():
  print('NRIC is invalid.')
else:
  
  digit_weight = [2, 7, 6, 5, 4, 3, 2]
  sum_weight = 0
  i = 0
  
  for num in nric_num:
    num = int(num)
    weight = num * digit_weight[i]
    i += 1
    sum_weight += weight
  if nric[0] in 'TG':
    sum_weight += 4
  quo, rem = divmod(sum_weight, 11)
  
  start_ST = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
  start_FG = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
  
  alp = ''
  if nric[0] in 'ST':
    alp = start_ST[rem]
  elif nric[0] in 'FG':
    alp = start_FG[rem]
  
  if nric[-1] == alp:
    print('NRIC is valid.')
  else: 
    print('NRIC is invalid.')