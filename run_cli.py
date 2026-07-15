import sys
import os

# Append the directory containing your packages
sys.path.append(os.path.join(os.getcwd(), "src"))

# Import from the specific path inside src
from cli.main import main

if __name__ == "__main__":
    main()
