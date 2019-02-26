
# TDD - Test Driven Development 

[![step](https://img.shields.io/badge/step-1-red.svg)]()
[![step](https://img.shields.io/badge/step-2-red.svg)](https://travis-ci.org/prthomas/split-unzipper)
[![Build Status](https://travis-ci.org/prthomas/split-unzipper.svg?branch=master)](https://travis-ci.org/prthomas/split-unzipper)

This is a repo, to demostrate TDD.
TDD refresher [Lynda.com](https://www.lynda.com/Python-tutorials/Unit-Testing-Test-Driven-Development-Python/746314-2.html).

## Description

TDD is a development process that moves through the following [stages](https://en.wikipedia.org/wiki/Test-driven_development#/media/File:TDD_Global_Lifecycle.png).
Here we will follow these [steps](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_work)

## Use Cases
[ ] Create a SplitUnzipper object with only `FileStream` parameter.
[ ] SplitUnzipper default `SplitSize` is 128MB, default `HeaderIncl` is False.
[ ] Create a SplitUnzipper object with `FileStream` and `SplitSize` parameters.
[ ] Create a SplitUnzipper object with `FileStream`, `SplitSize`, and `HeaderIncl'.
[ ] SplitUnzipper throws exception if not a zip stream.
[ ] SplitUnzipper unzips files and create individual gz files.
[ ] SplitUnzipper splits files into chunks.


## Commits
Each commit in this repo will represents either steps 1, 3, or 5 of the [test-driven work](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_work).

## Build Status
The build badge against each commit should represent either steps 2, 4, or 6 of the [test-driven work](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_work).
