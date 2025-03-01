import unittest
from app.services.file_service import extract_fin_messages
from app.config import Config

class TestFileService(unittest.TestCase):
    def test_extract_fin_messages(self):
        # Run the extraction function
        extract_fin_messages()

        # Verify the output file was created
        with open(Config.OUTPUT_FILE_PATH, "r") as outfile:
            content = outfile.read()
            self.assertIn("Request Raw Fin Message", content)
            self.assertIn("Response Fin Message", content)

if __name__ == "__main__":
    unittest.main()