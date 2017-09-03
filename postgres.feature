Feature: Installing postgres into a ubuntu container.

    Scenario: Installing postgres
        Given I have a docker container running
        When I run my scripts with ansible they should install postgres into the container
        Then Postgres should be running on post 5432