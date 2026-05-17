# Retail Trends Analyzer

A powerful Python tool for analyzing retail sales data and identifying trends in the retail industry. This tool helps businesses understand their sales patterns, identify top-performing products, analyze category performance, and track growth over time.

## Features

- 📊 **Comprehensive Data Analysis**: Analyze retail sales data from CSV or JSON files
- 🏆 **Top Products Identification**: Identify best-selling products by revenue
- 📈 **Category Performance**: Analyze sales performance by product category
- 📉 **Growth Rate Calculation**: Track revenue growth over time
- 📋 **Detailed Reports**: Generate comprehensive summary reports
- 💻 **CLI Interface**: Easy-to-use command-line interface
- 🔍 **Git Integration**: View connected user and commit history

## Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/vijaysuda/megaagent.git
cd megaagent
```

2. No external dependencies required! The tool uses only Python standard libraries.

## Usage

### Basic Usage

Analyze a CSV file:
```bash
python retail_trends.py sample_data.csv
```

Analyze a JSON file:
```bash
python retail_trends.py sample_data.json --format json
```

### Command-Line Options

```
usage: retail_trends.py [-h] [--format {csv,json}] [--output OUTPUT] [--git-info] [input_file]

Retail Trends Analyzer - Analyze retail sales data and identify trends

positional arguments:
  input_file           Input data file (CSV or JSON format)

optional arguments:
  -h, --help           show this help message and exit
  --format {csv,json}  Input file format (default: csv)
  --output OUTPUT      Output file for the report (optional, prints to console if not specified)
  --git-info           Show git repository information (connected user and recent commits)
```

### Examples

1. **Analyze CSV data and display report**:
```bash
python retail_trends.py sample_data.csv
```

2. **Analyze JSON data**:
```bash
python retail_trends.py sample_data.json --format json
```

3. **Save report to file**:
```bash
python retail_trends.py sample_data.csv --output report.txt
```

4. **Show git repository information**:
```bash
python retail_trends.py --git-info
```

## Data Format

### CSV Format

Your CSV file should have the following columns:
- `date`: Date in YYYY-MM-DD format
- `product`: Product name
- `category`: Product category
- `quantity`: Quantity sold
- `revenue`: Revenue generated

Example:
```csv
date,product,category,quantity,revenue
2024-01-15,Laptop,Electronics,2,2400.00
2024-01-16,T-Shirt,Clothing,5,125.00
```

### JSON Format

Your JSON file should be an array of objects with the following fields:
```json
[
  {
    "date": "2024-01-15",
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 2,
    "revenue": 2400.00
  }
]
```

## Sample Data

The repository includes sample data files for testing:
- `sample_data.csv`: Sample retail data in CSV format
- `sample_data.json`: Sample retail data in JSON format

## Running Tests

Run the test suite to verify the installation:
```bash
python test_retail_trends.py
```

Or use Python's unittest module:
```bash
python -m unittest test_retail_trends
```

## Report Output

The analyzer generates a comprehensive report including:

- **Basic Statistics**: Total records, revenue, and quantity sold
- **Top 5 Products**: Highest revenue-generating products
- **Category Performance**: Revenue breakdown by category
- **Growth Analysis**: Revenue growth rate between time periods

Example output:
```
============================================================
RETAIL TRENDS ANALYSIS REPORT
============================================================

Total Records: 30
Total Revenue: $15,598.99
Total Quantity Sold: 76
Average Revenue per Transaction: $519.97

------------------------------------------------------------
TOP 5 PRODUCTS BY REVENUE
------------------------------------------------------------
1. Smartphone: $2,700.00
2. Laptop: $2,400.00
3. Gaming Laptop: $1,500.00
4. Tablet: $1,200.00
5. Monitor: $900.00

------------------------------------------------------------
CATEGORY PERFORMANCE
------------------------------------------------------------
Electronics: $11,679.00
Clothing: $1,370.00
Appliances: $1,144.99
Footwear: $580.00

------------------------------------------------------------
GROWTH ANALYSIS
------------------------------------------------------------
First Half Revenue: $7,604.99
Second Half Revenue: $7,994.00
Growth Rate: 5.12%

============================================================
```

## Use Cases

- **Retail Business Analysis**: Understand which products and categories drive the most revenue
- **Inventory Planning**: Identify top-selling products to optimize inventory
- **Sales Trend Monitoring**: Track sales growth and performance over time
- **Category Management**: Analyze category performance to make strategic decisions
- **Market Research**: Understand retail trends and consumer preferences

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created as part of the megaagent project for retail trends analysis.
