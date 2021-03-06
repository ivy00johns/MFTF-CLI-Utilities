# MFTF-Tools

## Description
1. Welcome to the *Prototype* version of my **personal and custom** MFTF CLI Tools.
2. PLEASE NOTE: 
    * This is my 1st Python project so I apologize in advance for any horrendous code that you may find.
    * This is a WIP with a lot of improvements planend.

----

## Dependencies
* Python 3
    * [Python 3](https://www.python.org/download/releases/3.0/)
        * ```brew install python3```
* Python 3 Modules:
    * [PyInquirer](https://github.com/CITGuru/PyInquirer)
        * ```pip3 install PyInquirer```
* Cloned Magento repo (i.e.):
    * [Magento 2 CE](https://github.com/magento/magento2ce.git)
    * [Magento 2 EE](https://github.com/magento/magento2ee)
    * [Magento 2 B2B](https://github.com/magento/magento2b2b)
    * [MSI](https://github.com/magento-engcom/msi)

----

## Setup
1. Clone the "MFTF-CLI-Utilities" repo:
    ```
    git clone https://github.com/ivy00johns/MFTF-Tools.git
    ```

## Running Tools
1. CD to a Magento repo:
    ```
    cd [MAGENTO_REPO]
    ```
2. Run the MFTF-Tools:
    ```
    python3 [MFTF_CLI_UTILITIES_DIRECTORY]/mftf-tools.py
    ```

----

## Examples
![Question #1](https://github.com/ivy00johns/MFTF-Tools/blob/master/Images/question-1.png?raw=true)
![Question #2](https://github.com/ivy00johns/MFTF-Tools/blob/master/Images/question-2.png?raw=true)
![Question #3](https://github.com/ivy00johns/MFTF-Tools/blob/master/Images/question-3.png?raw=true)
![Question #4](https://github.com/ivy00johns/MFTF-Tools/blob/master/Images/question-4.png?raw=true)
![Question #5](https://github.com/ivy00johns/MFTF-Tools/blob/master/Images/question-5.png?raw=true)

----

### Known Issues
2. The Search functions for all "Everything" items are not complete at this time.

### TODO Items
1. Add Progress bars.
3. Add support for CLI flags.
5. Add "element" search functions.
6. Add Unit Tests.
7. Add Progress Bars.
8. Add "Display" specific node.
9. Add "Open in Editor":
    * Nano, eMac, Sublime, PHPStorm, VS Code, etc...
11. Add addtional message wrappers (i.e. "Start Of"/"End Of"/"Counts").
12. Add option for displaying XML file pathes.
14. Try to make compatible with python 2.
15. Disable "Everything" only in areas where it's not availabe.
16. Add "File Path" search functions:
    * Find file pathes
    * Display:Absolute/Relative Pathes
17. Add "verbose" flag.
18. List entity Attributes.
19. Search for Custom Attributes:
    * Node Name (```<test/>```)
    * Child-Node Name (```<click/>```)
    * Attr Name (```name=```)
20. Add "print" functions for, by name:
    * Full XML Page - `print`
    * Full XML Node - `print`
    * Full File Path - `print`
    * Relative File Path - `print`
21. Add "exit" step to all Script steps.
22. Add Search for "Selector" => Used in "Action Groups".
23. Add proper list "Results" feature.
24. Counts of Nodes per Module.
25. Display the # of modules.
26. Add list "Suites" function.

----

### COMPLETED - Known Issues
1. ~~The Search functionality is case-sensitive currently.~~ (FIXED)
3. ~~The Search functions for all "Metadata" items are not complete at this time.~~ (FIXED)

### COMPLETED - TODO Items
2. ~~Add counters to the "List Duplicate" functions.~~ (ADDED)
4. ~~Add "keys" to the Question options.~~ (ADDED)
10. ~~Rename the Utils to make them less redundent.~~ (DONE)
13. ~~Add ```#!/usr/bin/env python3``` to scripts.~~ (ADDED)
