#! /usr/bin/python3
# coding=utf-8
# @Time: 2023/7/31 16:27
# @Author:

from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:
    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是scope的class级别")

    @pytest.fixture(scope="function")
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    def test_open_bing(self,driver,scope_class):
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self,driver,scope_class):
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()
