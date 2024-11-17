from bs4 import BeautifulSoup
import csv
import requests


def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def add_head_to_html(soup: BeautifulSoup):
    meta = soup.new_tag('meta')
    meta.attrs['http-equiv'] = 'Content-Type'
    meta.attrs['content'] = 'text/html; charset=utf-8'
    style = soup.new_tag('style')
    style.string = '* {font-family: courier}'
    soup.head.append(meta)
    soup.head.append(style)

def write_posts_to_html(posts):
    soup = BeautifulSoup('''<html><head><title>Parsed JSON data</title></head><body></body></html>''', 'html.parser')
    add_head_to_html(soup)

    posts_list = soup.new_tag('ul', id='posts')
    for post in posts:
        li = soup.new_tag('li', id=f"{post['id']}li")
        li.string = f"Post №{post['id']}"
        li['style'] = 'font-weight: bold'

        sub_ul = soup.new_tag('ul', id=f"{post['id']}sub_ul")
        sub_ul['style'] = 'list-style-type: "— "; margin-bottom: 1em'
        for key, value in post.items():
            sub_li = soup.new_tag('li', id=f"{post['id']}{key}")
            sub_li.string = f"{key}: {value}\n"
            sub_ul.append(sub_li)

        posts_list.append(li)
        posts_list.append(sub_ul)

    soup.body.append(posts_list)
    return soup.prettify()


def parse_html_data_into_file(html):
    with open("sixth_task_result.html", "w", encoding="utf-8") as file:
        file.write(html)


posts = get_posts()
posts_html = write_posts_to_html(posts)
parse_html_data_into_file(posts_html)