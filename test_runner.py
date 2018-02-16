import unittest
import xmlrunner


if __name__ == '__main__':
	runner = xmlrunner.XMLTestRunner(output='test-reports')
	loader = unittest.TestLoader()
	suite = loader.discover('unittests')
	result = runner.run(suite)
