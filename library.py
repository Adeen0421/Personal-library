import streamlit as st

if "library" not in st.session_state:
    st.session_state.library = []

def add_book(title, author, year):
    st.session_state.library.append({"title": title, "author": author, "year": year})

def search_books(keyword):
    return [book for book in st.session_state.library if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]

st.title("Personal Library Manager")

with st.form("add_book"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.text_input("Year")
    submitted = st.form_submit_button("Add Book")
    if submitted and title and author and year:
        add_book(title, author, year)
        st.success("Book added")

st.header("All Books")
for book in st.session_state.library:
    st.write(f"{book['title']} by {book['author']} ({book['year']})")

keyword = st.text_input("Search books")
if keyword:
    st.header("Search Results")
    results = search_books(keyword)
    if results:
        for book in results:
            st.write(f"{book['title']} by {book['author']} ({book['year']})")
    else:
        st.write("No matching books found.")
