import requests
from bs4 import BeautifulSoup



def get_yangiliklar():
    url = 'https://www.ngmk.uz/uz/home/blog/matbuot-markazi/yangilik-va-voqealar'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
        yangiliklar = []
        for item in soup.find_all('div', class_='yangilik'):  
            sarlavha = item.find('h2').text.strip()
            matn = item.find('p').text.strip()
            yangiliklar.append({'sarlavha': sarlavha, 'matn': matn})
        
        return yangiliklar
    else:
        print(f"Error: Failed to retrieve data, status code {response.status_code}")
        return []

yangiliklar = get_yangiliklar()
for yangilik in yangiliklar:
    print(f"Sarlavha: {yangilik['sarlavha']}")
    print(f"Matn: {yangilik['matn']}\n")
    
def split_text(text, max_length):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]