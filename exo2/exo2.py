"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
def solution(string, ending):
    return string.endswith(ending)

# Boucle infinie pour tester un mot à la fois
while True:
    string = input("Entrez la chaîne de caractères : ")
    ending = input("Entrez la fin à vérifier : ")
    
    result = solution(string, ending)
    print(f"La chaîne '{string}' se termine-t-elle par '{ending}' ? {result}")

