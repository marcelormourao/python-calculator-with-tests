Feature: Calculator behave

  Scenario: Sum 0.2 and 0.04
    Given the numbers 0.2 and 0.04
     When sum thoses numbers
     Then the result should be 0.24!

  Scenario: Subtract 2.5 and 2.0
    Given the numbers 2.5 and 2.0
     When subtract thoses numbers
     Then the result should be 0.5!

  Scenario: Multiply 2.5 and 2.0
    Given the numbers 2.5 and 2.0
     When multiply thoses numbers
     Then the result should be 5.0!

  Scenario: Divide 4.3 and 3.0
    Given the numbers 4.3 and 3.0
     When divide thoses numbers
     Then the result should be 1.43!