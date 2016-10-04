from testtools import TestCase

from charmfixtures.juju.hooktools import (
    ConfigGet,
    StatusSet,
    JujuLog,
)


class ConfigGetTest(TestCase):

    def setUp(self):
        super().setUp()
        self.config = {}
        self.process = ConfigGet(self.config)

    def test_invoke(self):
        self.config["foo"] = "bar"
        result = self.process({})
        self.assertEqual(b'{"foo": "bar"}\n', result["stdout"].getvalue())


class JujuLogTest(TestCase):

    def setUp(self):
        super().setUp()
        self.log = []
        self.process = JujuLog(self.log)

    def test_no_entries(self):
        self.assertEqual([], self.log)

    def test_first_entry(self):
        self.process({"args": ["juju-log", "hello world"]})
        self.assertEqual("INFO: hello world", self.log[0])


class StatusSetTest(TestCase):

    def setUp(self):
        super().setUp()
        self.status = []
        self.process = StatusSet(self.status)

    def test_no_entries(self):
        self.assertEqual([], self.status)

    def test_first_entry(self):
        self.process({"args": ["state", "msg"]})
        self.assertEqual("state: msg", self.status[0])
