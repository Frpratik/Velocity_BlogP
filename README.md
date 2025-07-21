# 🌟 Django DRF Blog Project

Welcome to the **Django DRF Blog Project**!  
This is a sleek, modern blog platform built with **Django** and **Django REST Framework (DRF)**.  
It offers a robust set of features including **user authentication**, **blog management**, **search**, and **dynamic content loading** with **AJAX**.  
Whether you're a developer or a blogger, this project is designed to be **user-friendly** and **scalable**.

---

## 🚀 Features

✅ **User Authentication**: Register, login, and manage sessions with JWT (JSON Web Tokens) and token refresh.  
✅ **Blog CRUD**: Create, read, update, and delete blog posts (restricted to post owners).  
✅ **Draft/Publish Status**: Mark posts as draft or published for flexible content management.  
✅ **Comment System**: Add and view comments on each blog post.  
✅ **Search Functionality**: Search blog posts by title or content.  
✅ **Pagination**: Load blog posts in batches for a smooth user experience.  
✅ **Dynamic Frontend**: Static HTML pages with AJAX-powered **Load More** functionality.  
✅ **Secure Configuration**: Store sensitive data like database credentials and secret key in a `.env` file.  
✅ **Clean Styling**: Custom `styles.css` and `script.js` for a polished look and feel.  
✅ **Version Control**: Includes a `.gitignore` file to keep your repository clean.

---

## 🛠️ Setup Instructions

**Get the project up and running locally in just a few steps:**

---

### ✅ 1️⃣ Clone the Repository

- git clone https://github.com/Frpratik/Velocity_BlogP.git
- cd blog_project

---

### ✅ 2️⃣ Create and Activate a Virtual Environment

python -m venv venv

- **On Windows:**
venv\Scripts\activate

- **On Mac/Linux:**
source venv/bin/activate

---

### ✅ 3️⃣ Install Dependencies

- pip install -r requirements.txt

---

### ✅ 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add the following:

- SECRET_KEY=your_secret_key_here
- DEBUG=True
- DB_NAME=your_database_name
- DB_USER=your_database_user
- DB_PASSWORD=your_database_password
- DB_HOST=localhost
- DB_PORT=3306

---

### ✅ 5️⃣ Run Migrations

- python manage.py makemigrations
- python manage.py migrate

---

### ✅ 6️⃣ Create a Superuser (Optional)

- python manage.py createsuperuser

---

### ✅ 7️⃣ Start the Development Server

- python manage.py runserver

---

### ✅ 8️⃣ Access the Application

- Open your browser and navigate to:  
🌐 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📽️ Video Walkthrough

👉 [Click here to watch the full project walkthrough!](https://youtu.be/s_Lii4R3xPM?si=5nqjHC4s-MVnifdG)

---

## 👨‍💻 Author

**Pratik Ghuge**  
📧 [LinkedIn](https://linkedin.com/in/pratik-ghuge1926)  
🐙 [GitHub](https://github.com/Frpratik)

---

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: Simple JWT  
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL  
- **Environment**: Managed via `.env` for secure configuration

---

## 📝 Notes

- Replace `your_secret_key_here` with a secure key for production use.
- Ensure MySQL is running and configured before starting the server.
- Update the repository URL in the clone command with your actual GitHub repository.

---

**Happy blogging! 🚀**
