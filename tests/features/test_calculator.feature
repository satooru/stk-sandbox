@calculator

Feature: calculator

    Scenario: sum
        When summing 1 and 1
        Then result should be 2
    
    Scenario: subtract
        When subtracting 1 and 1
        Then result should be 0