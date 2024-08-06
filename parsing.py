from bs4 import BeautifulSoup
import requests

count_news = 0
with open('news.txt', 'w', encoding='utf=8') as file:
    for page in range(1, 11):
        url = f'https://24.kg/page_{page}'
        response = requests.get(url=url)
        print(response)
        soup = BeautifulSoup(response.text, 'lxml')
        all_news = soup.find_all('div', class_='title')
        # print(all_news)

        for news in all_news:
            count_news += 1
            file.write(f'{count_news}. {news.text}\n')
            # print(count_news, news.text)


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    news TEXT
                )
            """)
            
    def add_news(self, news_text):
        with self.connection:
            self.cursor.execute("INSERT INTO news (news) VALUES (?)", (news_text,))
    
    def get_all_news(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM news")
            return self.cursor.fetchall()

db = Database('news.db')
db.create_table()

def parse_news():
    news_list = []
    for page in range(1, 2): 
        url = f'https://24.kg/page_{page}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_news = soup.find_all('div', class_='one')

        for news in all_news:
            title = news.find('div', class_='title').get_text(strip=True)
            news_list.append(title)

    return news_list
tocen='7414989713:AAFgoakiyyPL-ZVtIstDSjK-x9SAUfomHIM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands='news')
async def send_news(message: types.Message):
    news_list = parse_news()
    for news in news_list:
        db.add_news(news)
    
    for idx, news in enumerate(news_list, 1):
        await message.answer(f"{idx}. {news}")

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
