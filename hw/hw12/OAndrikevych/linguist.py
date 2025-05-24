import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Create database connection
engine = create_engine("sqlite:///linguist2.db")  # Using SQLite for simplicity
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    decks = relationship("Deck", back_populates="user")

# Deck Model
class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="decks")
    cards = relationship("Card", back_populates="deck")

# Card Model
class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    deck_id = Column(Integer, ForeignKey("decks.id"))
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    tip = Column(String)
    deck = relationship("Deck", back_populates="cards")

# Create tables in the database
Base.metadata.create_all(engine)

# User Functions
def user_create(name, email, password):
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print(f"Warning: A user with email {email} already exists. Returning existing user.")
        return existing_user
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    return user

def user_get_by_id(user_id):
    return session.query(User).filter_by(id=user_id).first()

def user_update_name(user_id, name):
    user = user_get_by_id(user_id)
    if user:
        user.name = name
        session.commit()
    return user

def user_change_password(user_id, old_password, new_password):
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id):
    user = user_get_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

# Deck Functions
def deck_create(name, user_id):
    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    return deck

def deck_get_by_id(deck_id):
    return session.query(Deck).filter_by(id=deck_id).first()

def deck_update(deck_id, name):
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
        session.commit()
    return deck

def deck_delete_by_id(deck_id):
    deck = deck_get_by_id(deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False

# Card Functions
def card_create(user_id, deck_id, word, translation, tip):
    card = Card(user_id=user_id, deck_id=deck_id, word=word, translation=translation, tip=tip)
    session.add(card)
    session.commit()
    return card

def card_get_by_id(card_id):
    return session.query(Card).filter_by(id=card_id).first()

def card_filter(sub_word):
    return session.query(Card).filter(
        (Card.word.contains(sub_word)) |
        (Card.translation.contains(sub_word)) |
        (Card.tip.contains(sub_word))
    ).all()

def card_update(card_id, word=None, translation=None, tip=None):
    card = card_get_by_id(card_id)
    if card:
        if word:
            card.word = word
        if translation:
            card.translation = translation
        if tip:
            card.tip = tip
        session.commit()
    return card

def card_delete_by_id(card_id):
    card = card_get_by_id(card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False

# Functions to Load Data from Excel
def load_users_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name="Users")
    for _, row in df.iterrows():
        user_create(row["Name"], row["Email"], row["Password"])

def load_decks_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name="Decks")
    for _, row in df.iterrows():
        deck_create(row["Name"], row["User_ID"])

def load_cards_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name="Cards")
    for _, row in df.iterrows():
        card_create(row["User_ID"], row["Deck_ID"], row["Word"], row["Translation"], row["Tip"])

# Load data from Excel
file_path = "linguist_data.xlsx"
load_users_from_excel(file_path)
load_decks_from_excel(file_path)
load_cards_from_excel(file_path)

print("Data successfully imported from Excel!")

# Display Database Contents
def display_users():
    users = session.query(User).all()
    print("\nUsers in the database:")
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

def display_decks():
    decks = session.query(Deck).all()
    print("\nDecks in the database:")
    for deck in decks:
        print(f"ID: {deck.id}, Name: {deck.name}, User ID: {deck.user_id}")

def display_cards():
    cards = session.query(Card).all()
    print("\nCards in the database:")
    for card in cards:
        print(f"ID: {card.id}, Word: {card.word}, Translation: {card.translation}, Tip: {card.tip}, Deck ID: {card.deck_id}")

# Test Functions
display_users()
display_decks()
display_cards()

# Test User Functions
user = user_get_by_id(1)
if user:
    print(f"\nRetrieved User: ID {user.id}, Name: {user.name}, Email: {user.email}")

updated_user = user_update_name(1, "Dasha-2")
if updated_user:
    print(f"\nUser name updated: {updated_user.name}")

password_changed = user_change_password(1, "password_dasha", "password_dasha_new")
if password_changed:
    print("\nPassword updated successfully!")

user_deleted = user_delete_by_id(2)
if user_deleted:
    print("\nUser deleted successfully.")

# Test Deck Functions
deck = deck_get_by_id(1)
if deck:
    print(f"\nRetrieved Deck: ID {deck.id}, Name: {deck.name}, User ID: {deck.user_id}")

deck_update(1, "Desk_1_Update")
display_decks()

deck_delete_by_id(2)
display_decks()

# Test Card Functions
filtered_cards = card_filter("hello")
print(f"\nFiltered Cards: {len(filtered_cards)} found.")

card_update(1, word="hi", translation="привіт")
display_cards()

card_delete_by_id(2)
display_cards()
