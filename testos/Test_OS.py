import pytest
import yaml


class TestOs:

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "dev" in env:
            print("it is ", env["dev"])
        elif "des" in env:
            print("", ["des"])
