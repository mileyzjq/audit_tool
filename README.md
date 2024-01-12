## Auto Report Generator

A Python tool to generate formal Solidity Smart Contract audit reports from GitHub issues automatically

A pipeline process that fetches data from Github, parses data to specific styles, converts it to PDF, and uploads it to GitHub

This project can only be run with a formal Solidity contract with audit issues.

A sample outcome called report.pdf is generated for reference under the root directory.

Commands:
- run `make` to generate a new report
- run `make clean` to clean up locally generated files
