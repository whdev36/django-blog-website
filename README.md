# Django Blog Website

A simple blog website built with Django that allows users to create, read, and interact with blog posts. It features a post "clapping" system, a search feature, and the ability to view trending posts based on interaction metrics (views and claps). 

## Features

- **Home Page:** Displays trending blog posts based on views and claps.
- **Post Page:** Shows a single post and allows users to "clap" (like) posts.
- **Search Functionality:** Allows users to search posts by title, content, and tags.
- **Categories and Tags:** Blog posts can be categorized and tagged.
- **Claps System:** Users can clap for posts, which is tracked and displayed.
- **Views Tracking:** Displays how many times a post has been viewed.
- **Markdown Rendering:** Converts Markdown content into HTML for better formatting.

## Technologies Used

- **Django**: Web framework for building the application.
- **SQLite**: Default database for development (can be replaced with PostgreSQL in production).
- **Markdown**: For rich content formatting.
- **Bleach**: For sanitizing HTML content.
- **HTML/CSS**: Frontend for styling the blog pages.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/whdev36/django-blog-website.git
```

2. Navigate to the project directory:

```bash
cd django-blog-website
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

4. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run migrations:

```bash
python manage.py migrate
```

7. Create a superuser (optional for admin access):

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Usage

Once the server is running, you can:

- View the **home page** with trending posts.
- View individual **posts** by clicking on them.
- Search for posts using the **search bar**.
- Interact with posts by clapping (liking) them.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- **Icons**: [Document icons created by Roman Káčerek - Flaticon](https://www.flaticon.com/free-icons/document)
