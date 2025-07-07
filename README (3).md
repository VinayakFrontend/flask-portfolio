
# 🌐 Vinayak Gupta - Portfolio Website

A personal portfolio website built using **Flask** to showcase skills, projects, and provide a contact form that stores user messages in a local file (`message.txt`).

---

## 📌 Features

- ✅ Responsive and modern UI  
- ✅ Flask backend to handle form submissions  
- ✅ Contact form with validation  
- ✅ Stores form data in `message.txt`  
- ✅ SEO-friendly meta tags  
- ✅ Chatbot UI (VinayakBot)

---

## 🚀 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python)  
- **Form Handling**: Flask routes with POST request  

---

## 📁 Folder Structure

```
/your-project
│
├── static/
│   ├── css/
│   ├── img/
│   └── js/
│
├── templates/
│   └── index.html
│
├── app.py
├── message.txt         ← (Auto-created on first form submit)
└── README.md
```

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/portfolio-flask.git
cd portfolio-flask
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate       # For Windows
```

### 3. Install Dependencies

```bash
pip install Flask
```

### 4. Run the Application

```bash
python app.py
```

Visit **http://127.0.0.1:5000** in your browser.

---

## 📬 Contact Form Flow

- Form submits to `/contact` route via POST.  
- Data is saved in `message.txt`.  
- Flash message is shown:  
  `"Thank you! Your message has been received."`

---

## 📄 Example `message.txt` Content

```
--- New Message ---
Name: John Doe
Email: john@example.com
Phone: 9876543210
Message: Hello! I liked your projects.
```

---

## 👨‍💻 Author

**Vinayak Gupta**  
📧 vinayakgupta1614@gmail.com  
🌐 Portfolio Link Coming Soon

---

## 📃 License

This project is **open-source** and free to use under the **MIT License**.
