import pytest

from api.neo4j import get_driver
from api.dao.people import PeopleDAO

id_coppola = "1776"

def test_should_find_person_by_id(app):
    with app.app_context():
        # Get Neo4j Driver
        driver = get_driver()

        # Create DAO
        dao = PeopleDAO(driver)

        # Get Francis Ford Coppola
        output = dao.find_by_id(id_coppola)

        assert output["tmdbId"] == id_coppola
        assert output["name"] == "Francis Ford Coppola"
        assert output["directedCount"] == 16
        assert output["actedCount"] == 2


def test_should_return_paginated_list_of_similar_people(app):
    with app.app_context():
        # Get Neo4j Driver
        driver = get_driver()

        # Create DAO
        dao = PeopleDAO(driver)

        # Get Similar People
        limit = 6
        output = dao.get_similar_people(id_coppola, limit)

        assert len(output) == limit

        # Test Pagination
        second = dao.get_similar_people(id_coppola, limit, limit)

        assert len(second) == limit

        print("\n\n")
        print("Here is the answer to the quiz question on the lesson:")
        print("According to our algorithm, who is the most similar person to Francis Ford id_coppola?")
        print("Copy and paste the following answer into the text box: \n\n")

        print(output[0]["name"])
