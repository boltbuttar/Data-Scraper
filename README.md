# Data-Scraper
What Does This Code Do?
This code is designed to download research papers (PDFs) from the NeurIPS website. It looks for papers from the last five years and saves them on your computer.

Step-by-Step Breakdown:
Setting Up the Folder:
It first makes sure that there’s a folder (called scraper_python) on your computer to store the downloaded PDFs. If the folder doesn’t exist, the code will create it for you.

Fetching Web Pages:
It goes to the NeurIPS website and looks for a specific page that lists papers for each year (e.g., papers for 2023). If the website is down or there’s a problem loading the page, the code tries to fetch it a few more times before giving up.

Finding Paper Links:
After opening the page for a year, the code looks for all the links that lead to individual paper pages. It then opens each of those pages one by one.

Downloading PDFs:
For each paper, it checks if there’s a PDF available (the full-text version of the paper). If there is, it downloads the PDF. The download happens in small parts, and it shows a progress bar so you can see how much of the file has been downloaded.

Downloading at the Same Time:
To save time, the code downloads several PDFs at once instead of one by one. This is done using something called multi-threading. Think of it like having multiple people download files at the same time instead of just one person doing all the work.

Handling Errors:
If there’s an issue downloading a file (for example, if the internet connection is bad), the code tries again a few times before giving up. This way, it doesn’t stop the whole process if one thing goes wrong.

When Everything Is Done:
Once all the papers are downloaded, the code will let you know that the task is finished.

Why Is This Useful?
Convenience: You don’t have to visit each paper page and manually download the PDFs. The code does it all for you automatically.
Efficiency: The code downloads multiple PDFs at once, so you don’t have to wait too long.
Error-Handling: The code is smart enough to try again if something goes wrong, so it doesn’t leave things half-done.
In Short:
This program makes it easy to download a lot of research papers from NeurIPS by doing everything automatically: finding the papers, downloading them, and even showing you the download progress. All you have to do is run the code, and it handles the rest.
