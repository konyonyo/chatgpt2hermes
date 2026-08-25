import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from chatgpt_to_hermes import load_conversations


class LoadConversationsTests(unittest.TestCase):
    def test_loads_numbered_split_conversation_files_in_order(self):
        with tempfile.TemporaryDirectory() as directory:
            zip_path = Path(directory) / "export.zip"
            with zipfile.ZipFile(zip_path, "w") as archive:
                archive.writestr(
                    "conversations-10.json",
                    json.dumps([{"id": "second"}]),
                )
                archive.writestr(
                    "conversations-2.json",
                    json.dumps([{"id": "first"}]),
                )
                archive.writestr(
                    "conversations-20.json",
                    json.dumps([{"id": "third"}]),
                )

            conversations = load_conversations(zip_path)

        self.assertEqual(
            [conversation["id"] for conversation in conversations],
            ["first", "second", "third"],
        )


if __name__ == "__main__":
    unittest.main()
