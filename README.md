# 🌐 Real-Time Sentiment Analysis Application

## 📝 Project Overview
This application provides a real-time sentiment analysis platform that combines both **standard** and **fine-grain sentiment analysis** using Natural Language Processing (NLP) and **distributed computing**. The system is designed to handle varying loads by leveraging distributed algorithms and is tested under simulated user conditions.

## 🚀 Features
- **Real-Time Sentiment Analysis:** Provides both standard and detailed sentiment insights.
- **NLP Integration:** Utilizes Natural Language Processing techniques for sentiment extraction.
- **Distributed Computing:** Applies different distributed algorithms to various clones of the application using NGINX.
- **Load Testing:** Simulates user load using Apache Bench to evaluate performance under different circumstances.
- **Scalable Architecture:** Designed to scale with increasing numbers of users.

## 🛠️ Technology Stack
- **Frontend:** HTML, CSS Javascript, Bootstrap
- **Backend:** Flask, Gunicorn, NGINX (for serving the application)
- **NLP Libraries:** NLTK, spaCy, Transformers
- **Distributed Computing:** NGINX for load balancing and distributing algorithms
- **Testing Tools:** Apache Bench for performance testing
- **Version Control:** Git

## 🔧 How It Works
1. **NLP Processing:** The application analyzes text input to determine sentiment using NLP techniques.
2. **Distributed Algorithms:** NGINX routes requests to different clones of the application, each running various distributed algorithms.
3. **Sentiment Analysis:** Both standard and fine-grain sentiment analysis are performed to provide detailed insights.
4. **Load Simulation:** Apache Bench simulates different user loads to test the application’s performance and scalability.

## 📸 Screenshots
- **Login Page**
  
  ![image](https://github.com/user-attachments/assets/5bcc6562-3646-4b17-99bb-d6be4c320ca2)
  
- **Home Page**
  
  ![image](https://github.com/user-attachments/assets/feb4f655-9614-4606-abb0-6c776edf291b)
  ![image](https://github.com/user-attachments/assets/713ea3af-bed9-425c-9bf8-03c9a937061d)

- **Standard Sentiment Analysis Interface**
  
  ![image](https://github.com/user-attachments/assets/5fb01663-743d-4108-b9b0-792ac661eda6)

  - **Fine-Grain Sentiment Analysis Interface**
  
  ![image](https://github.com/user-attachments/assets/0f20757f-5adb-4c66-9ccd-3f13d430155e)

- **Load Testing Results**
  
  ![image](https://github.com/user-attachments/assets/5f62d582-0cd0-48a9-a2bd-05b9587923a2)

