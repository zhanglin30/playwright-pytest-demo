import os

import pytest

import config

if __name__ == '__main__':

    pytest.main(["-v", "-s", '--reruns=0', f'--alluredir={config.AllureResult}', "--clean-alluredir"])
    os.system(f'allure generate {config.AllureResult} -o {config.AllureReport} --clean')