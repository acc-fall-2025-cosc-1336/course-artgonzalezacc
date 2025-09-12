import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.examples.a_example import tests_devprocess as tests_input_process_output

suite = unittest.TestLoader().loadTestsFromModule(tests_input_process_output)
unittest.TextTestRunner(verbosity=2).run(suite)
