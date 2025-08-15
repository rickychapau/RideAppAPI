from database import Base, engine
import models

def create_all_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    create_all_tables()
