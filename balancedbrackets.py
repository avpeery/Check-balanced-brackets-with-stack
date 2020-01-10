"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""

def has_balanced_brackets(phrase):
  """Does a given string have balanced pairs of brackets?

  Given a string as input, return True or False depending on whether the
  string contains balanced (), {}, [], and/or <>.
  """
  
  #create dictionary of closers as keys with openers as values
  closers_to_openers = {")":"(", "}":"{", "]":"[", ">":"<"}
  
  #early exit
  if len(phrase) == 1 or phrase == "":
    return False

  #make a set of openers for quick matching
  openers_set = set(closers_to_openers.values())

  #create empty list to use as a stack
  openers_seen = []

  for char in phrase:
  
    #push openers in stack
    if char in openers_set:
      openers_seen.append(char)

    elif char in closers_to_openers:
      #fail fast if nothing in openers
      if openers_seen == []:
        return False

      #if last in openers_seen matches the closer's opener
      if openers_seen[-1] == closers_to_openers.get(char):
        #pop off from openers_seen
        openers_seen.pop()

      else:
        return False

  #if stack empty at end of for loop, means brackets are balanced
  return openers_seen == []


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")
