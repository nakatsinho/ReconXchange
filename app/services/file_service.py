import re
from app.config import Config
from app.utils.logger import log_info, log_error

def extract_fin_messages():
    """
    Extracts "Request Raw Fin Message" and "Response Fin Message" lines from the input file
    and saves them into a new output file.
    """
    # Patterns to match the required lines
    request_pattern = re.compile(r".*Request Raw Fin Message =><(.*)>")
    response_pattern = re.compile(r".*Response Fin Message is \[(.*)\]")

    try:
        # Open the input file for reading
        with open(Config.INPUT_FILE_PATH, "r") as infile:
            # Open the output file for writing
            with open(Config.OUTPUT_FILE_PATH, "w") as outfile:
                # Read the input file line by line
                for line in infile:
                    # Check for "Request Raw Fin Message"
                    request_match = request_pattern.match(line)
                    if request_match:
                        outfile.write(f"Request Raw Fin Message: {request_match.group(1)}\n")
                    
                    # Check for "Response Fin Message"
                    response_match = response_pattern.match(line)
                    if response_match:
                        outfile.write(f"Response Fin Message: {response_match.group(1)}\n")

        log_info(f"Extraction complete. Results saved to {Config.OUTPUT_FILE_PATH}")
    except Exception as e:
        log_error(f"An error occurred during file extraction: {e}")