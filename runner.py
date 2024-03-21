import pytest
import os
if __name__ == '__main__':
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    AllureReport = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureReport"
    AllureResult = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureResult"
    Screenshot = root_dir + os.path.sep + "TestReport" + os.path.sep + "Screenshot"
    pytest.main(["-v", "-s", '--reruns=0', f'--alluredir={AllureResult}', "--clean-alluredir"])
    os.system(f'allure generate {AllureResult} -o {AllureReport} --clean')