import unittest
from unittest.mock import patch, MagicMock, call
import io
from main import Taxi


class TestTaxiApp(unittest.TestCase):
    #mocking sys.stdout to capture console output.
    @patch('sys.stdout', new_callable=io.StringIO)
    #mocking 'input' to inject automatic responses.
    @patch('builtins.input')
    #mocking time.sleep to avoid real time delay.
    @patch('time.sleep', return_value=None)
    def test_main(self, mock_sleep, mock_input, mock_stdout):
        
        mock_input.side_effect = ['22', 'Maple', 'y', 's', 'm', 'x']
        #Creating an instance of Taxi.
        taxi_app = Taxi()
        taxi_app.welcome_passenger()
        #Checking if the journey should continue.
        if taxi_app.continue_journey:
            taxi_app.start_journey_loop()
            taxi_app.end_journey()
    
        #Capturing the console output.
        captured_output = mock_stdout.getvalue().strip()
        
        #Checking if the expected phrases are present in the output.
        self.assertIn("Printer sound.", captured_output)
        self.assertIn("Traffic lights, good heavens!!", captured_output)
        self.assertIn("here we go!", captured_output)
        self.assertIn("JOURNEY SUMMARY", captured_output)
        

if __name__ == "__main__":
    unittest.main()
