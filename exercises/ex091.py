#Beecrowd | 
def anos(days):
  result = days // 365
  return f'{result} ano(s)'

def months(days):
  n_days = days % 365
  result = n_days // 30
  return f'{result} mes(es)'

def day(days):
  n_days = days % 365
  result = n_days % 30
  return f'{result} dia(s)'

days = int(input())

print(anos(days))
print(months(days))
print(day(days))