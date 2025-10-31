import webbrowser

class WebOperations:
    def open_website(self, site):
        urls = {
            "google": "http://www.google.com",
            "youtube": "http://www.youtube.com"
        }
        if site in urls:
            webbrowser.open(urls[site])
            return True
        return False

    def search_web(self, query):
        webbrowser.open(f"https://www.google.com/search?q={query}")