
# TDD - Test Driven Development 

[![step](https://img.shields.io/badge/step-3-brightgreen.svg)]()
[![step](https://img.shields.io/badge/step-4-brightgreen.svg)](https://travis-ci.org/prthomas/split-unzipper)
[![Build Status](https://travis-ci.org/prthomas/split-unzipper.svg?branch=master)](https://travis-ci.org/prthomas/split-unzipper)

This is a repo, to demostrate TDD.  
TDD refresher [Lynda.com](https://www.lynda.com/Python-tutorials/Unit-Testing-Test-Driven-Development-Python/746314-2.html).  

## Description

TDD is a development process as represented in this state diagram:   
![stages](https://upload.wikimedia.org/wikipedia/commons/0/0b/TDD_Global_Lifecycle.png "TDD workflow")  
[Steps](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_work) for TDD.  

1. Add a test
1. Run all tests
1. Write some code
1. Run tests
1. Refactor code
1. Repeat

## Use Cases
* [x] Create a SplitUnzipper object with only `FileStream` parameter.  
* [x] SplitUnzipper default `SplitSize` is 128MB, default `HeaderIncl` is False.  
* [x] Create a SplitUnzipper object with `FileStream` and `SplitSize` parameters.  
* [x] Create a SplitUnzipper object with `FileStream`, `SplitSize`, and `HeaderIncl'.  
* [x] SplitUnzipper throws exception if not a zip stream.  
* [ ] SplitUnzipper unzips files and create individual gz files.  
* [ ] SplitUnzipper splits files into chunks.  


## Commits
Each commit in this repo will represents either steps 1, 3, or 5.

## Build Status
The build badge against each commit should represent either steps 2 and 4.
