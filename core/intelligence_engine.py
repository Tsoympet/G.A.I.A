import random
import sqlite3

class KnowledgeBase:
    def __init__(self, db_path='gaia/data/knowledge_base.db'):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self._initialize_db()

    def _initialize_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_entry(self, topic, content):
        self.cursor.execute("INSERT INTO knowledge (topic, content) VALUES (?, ?)", (topic, content))
        self.connection.commit()

    def get_entry(self, topic):
        self.cursor.execute("SELECT content FROM knowledge WHERE topic = ?", (topic,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def random_topic(self):
        self.cursor.execute("SELECT topic FROM knowledge ORDER BY RANDOM() LIMIT 1")
        result = self.cursor.fetchone()
        return result[0] if result else "unknown insight"

    def list_topics(self):
        self.cursor.execute("SELECT topic FROM knowledge")
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.connection.close()
