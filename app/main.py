from app.services.file_service import extract_fin_messages
from app.utils.logger import log_info

def main():
    log_info("Starting ReconXchange...")
    extract_fin_messages()
    log_info("Process completed.")

if __name__ == "__main__":
    main()