# ⏳🎵 Time Tunes  

*Music is a time machine. Let it take you back.*  

---

## 📖 About the Project  
**Time Tunes** is a Python project that lets you **travel back in time through music**.  
Pick any date in history (e.g., `1995-08-12`) and the app will:  
1. Scrape the **Billboard Hot 100** for that week  
2. Search those songs on **Spotify**  
3. Create a personalized Spotify playlist with the top hits from that era  

Because sometimes, the best way to relive a memory is to play the soundtrack from that moment. 🎧  

---

## 🌟 Why This Project is Great  
Music is more than sound — it’s memory, nostalgia, and emotion. Have you ever heard a song from high school and instantly remembered every detail of that moment?  
That’s what **Time Tunes** is built around.  

- 🎶 It combines **data + music + memory** in one simple app.  
- ⏳ It’s like having a **musical time capsule** at your fingertips.  
- 🛠️ It demonstrates real-world coding skills: scraping, APIs, authentication, and automation.  
- 📚 It’s a fantastic project for anyone building their **portfolio** — showing not only technical skills but also creativity and storytelling.  

Whether you’re a developer showcasing skills, a music lover building throwback playlists, or someone who just wants to relive the soundtrack of their favorite year — **Time Tunes makes it possible.**  

---

## 🚀 Features  
- 🔎 Scrapes Billboard Hot 100 charts for any given date  
- 🎶 Searches Spotify for matching tracks  
- 📂 Automatically builds a playlist in your account  
- 🕰️ Lets you experience “time travel” through music  

---

## 🛠️ Tech Stack  
- **Python**  
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) → for web scraping Billboard  
- [Spotipy](https://spotipy.readthedocs.io/) → for Spotify Web API integration  
- **dotenv** → for secure secret management  

---

## ⚙️ Setup & Usage  

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/time-tunes.git
   cd time-tunes
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root (never push this to GitHub!)  
   ```env
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   SPOTIFY_REDIRECT_URI=https://example.com
   SPOTIFY_SCOPES=playlist-modify-private
   ```

4. **Run the program**  
   ```bash
   python main.py
   ```

5. Enter a date (YYYY-MM-DD), log into Spotify once, and… 🎉 enjoy your freshly made throwback playlist!  

---

## 🎨 Example  
```bash
Enter date to time-travel to (YYYY-MM-DD): 2000-05-13
Found 100 songs for 2000-05-13.
Matched 96 tracks on Spotify; 4 not found.
Created playlist: "Billboard Hot 100 - 2000-05-13"
```

Open Spotify and find your **Time Tunes playlist** waiting for you!  

---

## 🧑‍💻 Why I Built This  
I’ve always believed that *music is a time machine*. One song can instantly take you back to a summer, a heartbreak, or the best night of your life.  

**Time Tunes** was made with this idea: pick a date, get the hits, and relive the moment.  

---

## 📸 Demo  
*(Add a screenshot or GIF of your playlist here)*  

---

## ⚠️ Note  
This project is for **personal use only**.  
Remember to keep your Spotify API credentials safe in your `.env` file.  

---

## ⭐ Like the Project?  
If you enjoy reliving memories through music, give this repo a ⭐ on GitHub and share your favorite throwback playlist with me!  

---

Made with ❤️ and a little bit of nostalgia by [Suhaas](https://github.com/yourusername).
