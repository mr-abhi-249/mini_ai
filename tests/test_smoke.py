import unittest


class SmokeTests(unittest.TestCase):
    def test_import_app(self):
        import app  # noqa: F401

    def test_system_switch_mode(self):
        from commands.system import SystemCommandHandler

        outputs = []
        result = SystemCommandHandler().handle("switch mode", outputs.append)

        self.assertTrue(result.handled)
        self.assertEqual(result.action, "switch_mode")


if __name__ == "__main__":
    unittest.main()
