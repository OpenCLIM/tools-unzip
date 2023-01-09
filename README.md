# tools-unzip
Extracts data from an archive, making available all files and sub-directories that existed within the archive. Any archives in the main archive will not be extracted. 

## Inputs
### Variables
None

### Data
* a data archive
  * Description: A archive, or multiple archives (zip files)
  * Format: .zip
  * Location: data/inputs

## Outputs
* folder of data
  * Description: A folder containing the contents of the archive
  * Format: a folder
  * Location: data/outputs/#name of archive#
* log file
  * Description: A logfile recording the process
  * Format: .txt
  * Location: data/outputs
  * Name: tools-unzip.txt

## Running
### DAFNI
Run as part of a workflow. Requires an archive in the single data slot. No other inputs are required. Can accept multiple archives in the data slot.

### Docker
* docker build . -t unzip && docker run -v $PWD/data:/data -t unzip