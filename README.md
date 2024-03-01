# qa_python
1. def test_add_new_book_add_3_books - checks that after adding a new book, it appears in the books_genre dictionary
2. def test_add_new_book_add_book_name_length_is_41_ -  checks that a book whose name consists of 41 characters has not been added in the books_genre dictionary
3. def test_add_new_book_add_one_book_twice - checks that one book cannot be added twice to the books_genre dictionary
4. def test_set_book_genre_add_one_book_with_genre - checks that after setting the book genre, the book genre is updated in the books_genre dictionary
5. def test_get_book_genre_and_book_has_no_genre - checks that method get_book_genre returns empty string if book has no genre
6. def test_get_books_with_specific_genre_3_genres_specified - verifies that the get_books_with_specific_genre method returns a valid list of books with the given genre
7. def test_get_books_for_children - verifies that the get_books_for_children method returns the correct list of children-friendly books 
8. def test_add_book_in_favorites_add_1_book - checks that 1 favorite book has been added to the favorites dictionary
9. def test_delete_book_in_favorites_delete -  checks that book has been deleted from favorites dictionary