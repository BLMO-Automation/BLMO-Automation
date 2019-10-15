Feature : Login to portl
    Scenario: Login and logout
        When I open lmo website
        And I login with username "admin" and password "admin"
        Then I verify that I successfully logged in by logging out