# Log Metrics Calculator

The Log Metrics Calculator is a Python script that reads input from stdin, computes metrics, and prints statistics based on the log lines provided. It calculates the total file size and counts the number of lines by status code.

## Input Format

The script expects the input to follow the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```


If a line does not adhere to this format, it will be skipped.

## Usage

1. Make sure you have Python installed on your system.

2. Clone this repository:

   ```bash
   git clone https://github.com/afkzoro/log-parsing.git
   ```

3. Navigate to the project directory:

    ```bash
        cd 0x03-log_parsing
     ```
4. Run the script:

    ```bash
     python 0-stats.py | 
    ```
Provide the input log lines through stdin. You can either type the log lines manually or redirect input from a file:

bash
Copy code
python log_metrics_calculator.py < log_file.txt
The script will process the input lines and calculate the metrics. It will print statistics every 10 lines and also when you interrupt the script using CTRL + C.