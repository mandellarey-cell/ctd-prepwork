if name_input == myname:
...     print("welcome boss")
... else:
...     print("wrong name playa")
... 
wrong name playa
>>> print("what age are you ?")
what age are you ?
>>> try:
...     age_input = int(input())
...     if age_input == myage:
...         print("looks good on you boss")
...     else:
...         print("nah wrong age mate")
... except ValueError:
...     print("nah wrong age mate")
