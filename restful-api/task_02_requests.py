#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """print the status code of the response"""
    response = requests.get(URL)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """fetches ll post from JSONPlaceholder"""
    response = requests.get(URL)
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": post["id"],
                 "title": post["title"],
                 "body": post["body"]} for post in posts]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
