import sys
import os

# Force add the src folder to the python path
sys.path.append(os.path.join(os.getcwd(), "src"))

from cli.main import main

if __name__ == "__main__":
    main()
