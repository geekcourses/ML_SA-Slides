# absolute import
import packA.A_functions
from packA.packB import B_functions

print("__name__ in main: ", __name__)

packA.A_functions.packA_function1()
B_functions.packB_function1()


