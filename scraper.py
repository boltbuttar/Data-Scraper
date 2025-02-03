import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

# Define constants
BASE_URL = "https://papers.nips.cc"
SAVE_DIR = "C:\\scraper_python"
NUM_YEARS = 5
THREAD_POOL_SIZE = 5  # Number of concurrent downloads

# Ensure save directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

def fetch_document_with_retries(url, retries=3):
    """Fetch document with retries on failure"""
    while retries > 0:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"⚠ Failed to fetch {url}. Retrying... ({retries} left)")
            retries -= 1
    return None

def download_file_with_progress(url, save_path):
    """Download file with a progress bar"""
    if os.path.exists(save_path):
        print(f"✔ Already downloaded: {save_path}")
        return
    
    response = requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
    file_size = int(response.headers.get('Content-Length', 0))
    
    with open(save_path, "wb") as file, tqdm(
        desc=f"Downloading {os.path.basename(save_path)}",
        total=file_size, 
        unit='B', unit_scale=True
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))
    print(f"✅ Downloaded: {os.path.basename(save_path)}")

def scrape_papers(year):
    """Scrape papers for a specific year"""
    print(f"📡 Scraping: {BASE_URL}/paper_files/paper/{year}")
    
    # Fetch the year page
    year_url = f"{BASE_URL}/paper_files/paper/{year}"
    page_content = fetch_document_with_retries(year_url)
    if not page_content:
        print(f"❌ Failed to fetch year {year}")
        return
    
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Find paper links (links to individual paper pages)
    paper_links = soup.find_all('a', href=True)
    paper_links = [urljoin(BASE_URL, link['href']) for link in paper_links if '/paper_files/paper/' in link['href']]
    
    if not paper_links:
        print(f"⚠ No paper links found for {year}")
        return
    
    print(f"📄 Found {len(paper_links)} paper links for {year}")
    
    # Scrape each paper page
    for paper_url in paper_links:
        print(f"📝 Scraping paper page: {paper_url}")
        
        paper_page_content = fetch_document_with_retries(paper_url)
        if not paper_page_content:
            print(f"❌ Failed to fetch paper page {paper_url}")
            continue
        
        soup = BeautifulSoup(paper_page_content, 'html.parser')
        
        # Find PDF links in the paper page
        pdf_links = soup.find_all('a', href=True)
        pdf_links = [urljoin(BASE_URL, link['href']) for link in pdf_links if link['href'].endswith('.pdf')]
        
        if not pdf_links:
            print(f"⚠ No PDFs found for paper {paper_url}")
            continue
        
        # Download PDFs using threading
        with ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as executor:
            for pdf_url in pdf_links:
                pdf_name = os.path.basename(pdf_url)
                save_path = os.path.join(SAVE_DIR, pdf_name)
                executor.submit(download_file_with_progress, pdf_url, save_path)

def main():
    # Scrape papers for the last NUM_YEARS years
    for year in range(2023, 2023 - NUM_YEARS, -1):
        scrape_papers(year)

    print("✅ All downloads completed.")

if __name__ == "__main__":
    main()
