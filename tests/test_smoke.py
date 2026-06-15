import unittest
from unittest.mock import patch


class SmokeTests(unittest.TestCase):
    def test_import_app(self):
        import app  # noqa: F401

    def test_system_switch_mode(self):
        from commands.system import SystemCommandHandler

        outputs = []
        result = SystemCommandHandler().handle("switch mode", outputs.append)

        self.assertTrue(result.handled)
        self.assertEqual(result.action, "switch_mode")

    def test_wake_phrase_response(self):
        from commands.system import SystemCommandHandler

        outputs = []
        result = SystemCommandHandler().handle("Hey Mini", outputs.append)

        self.assertTrue(result.handled)
        self.assertIn("Owner verified", outputs[-1])

    def test_project_status_response(self):
        from commands.system import SystemCommandHandler

        outputs = []
        result = SystemCommandHandler().handle("what remains in my mini project", outputs.append)

        self.assertTrue(result.handled)
        self.assertIn("Okay Sir.", outputs[-1])

    def test_show_menu_eof_defaults_to_text_mode(self):
        from app import AssistantApp

        assistant = AssistantApp()
        with patch("builtins.input", side_effect=EOFError):
            self.assertFalse(assistant.show_menu())

    def test_text_mode_eof_exits_cleanly(self):
        from app import AssistantApp

        assistant = AssistantApp()
        with patch("builtins.input", side_effect=EOFError):
            with self.assertRaises(SystemExit):
                assistant.text_mode()


if __name__ == "__main__":
    unittest.main()
