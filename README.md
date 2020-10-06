# Stoichiometry-Helper-GUI

This is a GUI program that uses Tkinter to solve for the mass, molar mass and moles of various compounds in a chemical reaction using dimensional analysis. In AP chemistry, we are taught how to solve for the mass (g), molar mass (g/mol) and mole quantity of all of the compounds in a chemical reaction. This enables us to then discover the limiting reagent in the reaction based on the expected masses produced and the information in the question. This GUI streamlines the process, eliminating the need for tedious calculations while admittedly sacrificing some accuracy and respect for significant digits. It uses the molmass module for Python, which perform molar mass calculations with speed.

## Sample Outputs

![Sample output](https://github.com/satvick16/stoichiometry-helper-gui/blob/master/chem_sample_output.jpg?raw=true)

## Getting Started

In the top right corner are the input fields. One must input the unbalanced chemical equation, molar ratio (coefficients) and one quantity (mass or moles) for one of the compounds. Clicking "submit" will perform the calculations and display the numbers in the bottom left and provide percent composition of each compound in the top right. In the bottom right, you can input the symbol of an element and press "get description" to get the history and various facts about the provided element. For optimal experience, use in full screen mode.

### Downloads

* stoichiometry.py: main program
* chem_sample_output.jpg: sample output

## Built With

* [Tkinter](https://wiki.python.org/moin/TkInter) - GUI framework
* [molmass](https://pypi.org/project/molmass/) - specialized Python chemistry package
