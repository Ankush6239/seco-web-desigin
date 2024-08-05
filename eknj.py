import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
[
    {
      "keys": ["ctrl+s"], "command": "browser_refresh", "args": {
        "auto_save": true,
        "delay": 0.0,
        "activate": true,
        "browsers" : ["chrome"]
      }
    }
  ]