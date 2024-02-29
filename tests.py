import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['Хоббит', 'Маленький принц', 'Властелин колец'])
    def test_add_new_book_add_3_books(self, book_name):
        collector = BooksCollector()
        initial_books_count = len(collector.get_books_genre())
        for i in range(3):
            collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == initial_books_count + 1

    def test_add_new_book_add_book_name_length_is_41_(self):
        collector = BooksCollector()
        book_name = "a" * 41
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_new_book_add_one_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Человек в поисках смысла')
        collector.add_new_book('Человек в поисках смысла')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_and_set_book_genre_add_one_book_with_genre(self):
        collector = BooksCollector()
        book_name = 'Институт'
        genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_and_book_has_no_genre(self):
        collector = BooksCollector()
        book_name = 'Библия'
        collector.add_new_book(book_name)
        assert len(collector.get_book_genre('Библия')) == 0

    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Хоббит', 'Властелин колец']),
        ('Мультфильмы', ['Маленький принц']),
        ('Комедии', []),
    ])
    def test_set_book_genre_and_set_book_genre_add_1_book_with_genre(self, genre, expected_books):
        collector = BooksCollector()
        book_name = 'Институт'
        genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre', [
        ('Кот в сапогах', 'Мультфильмы'),
        ('Незнайка на Луне', 'Мультфильмы'),
        ('Мистер Мерседес', 'Ужасы'),
    ])
    def test_get_books_for_children_2_books_for_children_added(self, book_name, genre):
        collector = BooksCollector()
        book_name = 'Кот в сапогах'
        genre = 'Мультфильмы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        expected_children_books = []
        for name, genre in collector.get_books_genre().items():
            if genre not in collector.genre_age_rating and genre in collector.genre:
                expected_children_books.append(book_name)
        assert collector.get_books_for_children() == expected_children_books

    @pytest.mark.parametrize('book_name', ['Повесть о двух городах', 'Дон Кихот', 'Цитаты председателя Мао Цзэдуна'])
    def test_add_book_in_favorites_add_1_book(self, book_name):
        collector = BooksCollector()
        book_name = 'Повесть о двух городах'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_in_favorites_delete(self):
        collector = BooksCollector()
        book_name = "Коран"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites
