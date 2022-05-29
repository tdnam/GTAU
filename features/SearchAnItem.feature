Feature:  Searching function

    Scenario Outline: Scenario Outline name: Search an item
        Given user accesses Gumtree
        When user searches for "<search_keyword>" with catergory "<search_category>", distance "<search_distance>" and area "<search_area>"
        And user opens a random result
        Then user verifies the ad details page open
        And user ensures a numeric ad id is displayed in the breadcrumbs and verify at least one similar ad is displayed in the page


        Examples:
            | search_keyword        | search_category        | search_distance | search_area        |
            | Sennheiser Headphones | Electronics & Computer | 20km            | Sydney Region, NSW |