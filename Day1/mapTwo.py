'''
    map()
'''

def fun(arg):
   return f'{arg} passed to fun()'



if __name__ == '__main__':
  res = map(fun,list(range(1,101)))
  for i in res:
      print(i)


