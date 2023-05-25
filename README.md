# PDF Document Query Experiment
This is an experiment to query a locally stored PDF document using llama-index and chatgpt.

## Setup
To run this experiment, you'll need to set up a Python 3 environment using Miniconda and install the required packages from requirements.txt via pip.

### Setting up a Python 3 environment using Miniconda
1. Download and install Miniconda from the official website: https://docs.conda.io/en/latest/miniconda.html
2. Open a terminal or command prompt and create a new Python 3 environment using the following command:
    ```
    conda create --name pdf-query python=3
    ```
3. Activate the new environment using the following command: `conda activate pdf-query`

### Installing packages from requirements.txt via pip

1. Clone or download the project repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required packages from requirements.txt using the following command:
    ```
    pip install -r requirements.txt
    ```

    This will install the following packages:

    - openai
    - llama-index

# Usage

To run the experiment, run the main.py script using the following command:

```
python main.py
```

This will prompt you to enter a query string. Enter your query and press Enter to see the results.


