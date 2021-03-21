# Datset Analyzer
 
<br />
<p align="center">
  <p align="center">
    <img src="https://github.com/shreeratn/datset-analyzer/blob/main/Icon.svg" width = "300" height = "300">
    </p>
  <h3 align="center">
    Minimal dataset analyzer</h3>
  <p align="center">
    Minimal dataset analyzer
    <br />
  </p>
</p>


### [![version](https://img.shields.io/github/v/tag/shreeratn/datset-analyzer?color=ef4041&label=Latest%20Version&logo=Latest%20release&style=for-the-badge)](https://github.com/shreeratn/datset-analyzer/releases) **[![Roadmap](https://img.shields.io/badge/ROADMAP%20here-red?style=for-the-badge&color=5d9741)](https://github.com/users/shreeratn/projects/1)**



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Dataset analyzer](#human-typing-simulator)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About the Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Although there are many packages which can be used to anayze the data, this repo keeps in mind the minimalism and low key usages without displaying any overwhelming feature which also keeps the resource usage to minimum

Here's detail which are shown as column-wise:

* Datatype
* Total number of Values
* Total number of Null values
* Total number of Unique values
* Percent of Unique values 
* Determine that given column might be categorical
* Determine that given column might be ignored


## [![forthebadgepython](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites and Installations

List of things you need to use the software and how to install them:


[![pandas-icon](https://img.shields.io/badge/Package%20needed-pandas-blue?style=for-the-badge&labelColor=00c7ff&color=009fef)](https://pypi.org/project/pandas/)

```sh
pip install pandas --user
```

[![tabulate-icon](https://img.shields.io/badge/Package%20needed-tabulate-blue?style=for-the-badge&labelColor=00c7ff&color=009fef)](https://pypi.org/project/tabulate/)

```sh
pip install tabulate --user
```

<!-- USAGE EXAMPLES -->

## Usage

1. Run the analyzer.py in terminal
2. Keep the files to be specified in same folder or specify full path to file
3. First Argument[optional]- determination:
    * nll - is used to view only the columns which have null values >=1 
    * cat - is used to view only the columns which might be changed to categorical or is categorical
    * ign - is used to view only the columns which might be ignored, since they have high uniqueness
4. Second Argument[optional]- threshold:
    * In order to determine which columns can be possibly ignored depending upon the uniqueness percentage, this asks for the percentage of uniqueness

<br />


<!-- CONTRIBUTING -->
<!-- ## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Shree Ratn 

[<img src="https://img.shields.io/badge/ShreeRatn%20-%231DA1F2.svg?&style=for-the-badge&logo=Twitter&logoColor=white"/>](https://twitter.com/ratn_shree)
[<img src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>](https://linkedin.com/in/shreeratn)
[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>](https://github.com/shreeratn/)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* This was made by me and is not copied from any other sources