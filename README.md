# KEGG_Modules_Fetcher

Introduction:
kegg_modules_fetcher.py is a Python script designed to extract detailed information about biological modules from the KEGG database. This script takes a list of KEGG module IDs, fetches data for each module, and extracts relevant details, including entries, symbols, names, pathway IDs, and pathway names associated with each module. It's particularly useful for bioinformatics research where detailed module information is crucial.

Features:
Fetches module details from KEGG database using module IDs.
Extracts entries, symbols, names, pathway IDs, and pathway names.
Handles API rate limits by introducing a delay between requests.
Outputs data in a tab-separated values (TSV) file for easy analysis.

Requirements:
Python 3
'requests' library

Usage:
Prepare a text file (module_ids.txt) with a list of KEGG module IDs, each ID on a new line.

Run the script: python kegg_modules_fetcher.py

Citation:
If you are using the kegg_modules_fetcher.py script, please cite it as follows:
Sharma, V. (2023). kegg_modules_fetcher.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/kegg_modules_fetcher
