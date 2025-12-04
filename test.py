import unittest
from unittest.mock import patch, MagicMock, call
import io
from main import welcome, main 


class TestMain(unittest.TestCase):

    #mocking sys.stdout to capture console output.
    @patch('sys.stdout', new_callable=io.StringIO)
    #mocking 'input' to inject automatic responses.
    @patch('builtins.input')
    #mocking time.sleep to avoid real time delay.
    @patch('time.sleep', return_value=None)
    #return value "none" because we don't want to wait for real time delay.
    def test_main(self, mock_sleep, mock_input, mock_stdout):
        
        # When called Maple, y, s, m, x.
        mock_input.side_effect = ['Maple', 'y', 's', 'm', 'x']
        
        # Executing the main function.
        main()
        
        # Verification of results, Capturing all console output during main execution.
        captured_output = mock_stdout.getvalue().strip()
        
        # Verifying that the specific text is present in the total output.
        expected_phrase = "Printer sound."
        
        self.assertIn(expected_phrase, captured_output)
if __name__ == "__main__":
    unittest.main()



# with open('test.txt', 'w') as file:
#     file.write('testing!')