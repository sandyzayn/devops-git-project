
# main.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def main():
    logging.info("Hello, DevOps World!")

if __name__ == "__main__":
    main()
