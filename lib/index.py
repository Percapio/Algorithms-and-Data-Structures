from algorithms import binary_search

from testers import test_funcs

def run_all_functions():
  # Binary Search
  test_funcs.f_search( binary_search.binary_search_rec,  'Recursive Binary Search')
  test_funcs.f_search( binary_search.binary_search_iter, 'Iterative Binary Search')

if __name__ == "__main__":
  run_all_functions()