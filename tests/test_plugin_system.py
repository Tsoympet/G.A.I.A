import unittest
from unittest.mock import MagicMock
from gaia.core.plugin_registry import PluginRegistry, trigger_plugin_event

class TestPluginSystem(unittest.TestCase):
    def setUp(self):
        self.registry = PluginRegistry()
        self.mock_plugin_a = MagicMock()
        self.mock_plugin_b = MagicMock()

        # Register fake plugins for 'on_dream_event' and 'on_market_update'
        self.registry.register_plugin("on_dream_event", self.mock_plugin_a)
        self.registry.register_plugin("on_market_update", self.mock_plugin_b)

    def test_plugin_registration(self):
        """Ensure plugin registration works and stores properly."""
        plugins = self.registry.get_plugins("on_dream_event")
        self.assertIn(self.mock_plugin_a, plugins)

    def test_trigger_event_executes_plugins(self):
        """Verify that registered plugins are triggered with payload."""
        payload = {"topic": "test_topic"}
        trigger_plugin_event("on_dream_event", payload, registry=self.registry)
        self.mock_plugin_a.assert_called_once_with(payload)

    def test_unregistered_event_does_not_fail(self):
        """Ensure triggering an unknown event does nothing harmful."""
        try:
            trigger_plugin_event("on_unknown_event", {"foo": "bar"}, registry=self.registry)
        except Exception as e:
            self.fail(f"Triggering unknown event raised exception: {e}")

    def test_plugin_execution_order(self):
        """Ensure multiple plugins are triggered in order."""
        second_plugin = MagicMock()
        self.registry.register_plugin("on_market_update", second_plugin)

        payload = {"market": "BTC"}
        trigger_plugin_event("on_market_update", payload, registry=self.registry)

        self.mock_plugin_b.assert_called_once_with(payload)
        second_plugin.assert_called_once_with(payload)

    def test_plugin_removal(self):
        """Test removal of plugins and event cleanup."""
        self.registry.unregister_plugin("on_dream_event", self.mock_plugin_a)
        plugins = self.registry.get_plugins("on_dream_event")
        self.assertNotIn(self.mock_plugin_a, plugins)

    def test_trigger_with_no_plugins(self):
        """Triggering an event with no plugins should pass silently."""
        self.registry.clear_plugins("on_dream_event")
        try:
            trigger_plugin_event("on_dream_event", {"void": True}, registry=self.registry)
        except Exception as e:
            self.fail(f"Triggering empty event list raised exception: {e}")

if __name__ == '__main__':
    unittest.main()
