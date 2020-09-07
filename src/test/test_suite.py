import sys
import unittest
from os.path import dirname, realpath

# Set mock libraries and original libraries to path
folder_path = dirname(realpath(__file__))
parent_folder_path = folder_path[:folder_path.rfind('/')]
libs_path = "{test_folder}".format(test_folder=parent_folder_path)

paths = [libs_path]

# list out additional scripts to be tested (by filename)
test_modules = [
    {
        'paths': paths,

        'unit': [],
        'integration': ['integration.mgr.display_mgr_test',
                        'integration.mgr.download_mgr_test',
                        'integration.mgr.get_files_mgr_test',
                        'integration.mgr.stats_mgr_test',
                        'integration.mgr.upload_mgr_test'],
        'system': []

    }
]


def setup(paths):
    i = 0
    for path in paths:
        sys.path.insert(i, path)
        i += 1


def reset(paths):
    for path in paths:
        sys.path.remove(path)


def run(test_module):
    for t in test_module:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suite_fn = getattr(mod, 'suite')
            suite.addTest(suite_fn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))


total_test_count = 0
for test_module in test_modules:
    suite = unittest.TestSuite()
    paths = test_module['paths']
    unit = test_module['unit']
    integration = test_module['integration']
    system = test_module['system']
    setup(paths)
    run(unit)
    run(integration)
    run(system)

    result = unittest.TextTestRunner().run(suite)
    total_test_count = total_test_count + result.testsRun
    reset(paths)
    if not result.wasSuccessful():
        sys.exit(1)
    print('Completed tests in suite {}'.format(test_module['unit']))
    print('Completed tests in suite {}'.format(test_module['integration']))
    print('Completed tests in suite {}'.format(test_module['system']))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
print('Successfully ran {} tests in total.'.format(total_test_count))
