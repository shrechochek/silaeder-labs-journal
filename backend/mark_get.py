import psycopg2

# Параметры подключения
DB_CONFIG = {
    "dbname": "marks",
    "user": "test_superuser",
    "password": "password",
    "host": "localhost",
    "port": 5432
}

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    cursor = conn.cursor()

    # Создаём таблицу, если её нет
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        );
    """)

    # Данные для вставки
    user_data = ("Иван", "ivan@example.com", 30)

    # Добавляем данные (если такой email уже есть — не добавляем)
    cursor.execute("""
        INSERT INTO users (name, email, age)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
    """, user_data)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
