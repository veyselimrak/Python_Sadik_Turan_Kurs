from bs4 import BeautifulSoup
 

html_code = """"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>

    <h1> Python </h1>

<div>
        <h2>Python</h2>
        <ul>
            <li>Menü 1</li>
 <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div>
        <h2>Modüller</h2>
<ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <a href="www.facebook.com">merhaba</a>
    <a href="www.github.com">
    </a><a href="www.twitter.com"></a>
    
</body>
</html>
"""

soup = BeautifulSoup(html_code, "html.parser")

result = soup.prettify()
result = soup.title
result = soup.body
result = soup.title.string
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1]

result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren()
result = soup.div.findNextSibling()

result = soup.find_all("a")

for link in result:
    print(link.string)

print(result)

