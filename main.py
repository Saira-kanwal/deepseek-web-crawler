import asyncio

from crawl4ai import AsyncWebCrawler
from dotenv import load_dotenv

from config import BASE_URL, CSS_SELECTOR, REQUIRED_KEYS
from utils.data_utils import (
    save_products_to_csv,
)
from utils.scraper_utils import (
    fetch_and_process_page,
    get_browser_config,
    get_llm_strategy,
)

load_dotenv()


async def crawl_products():
    """
    Main function to crawl product data from the website.
    """
    # Initialize configurations
    browser_config = get_browser_config()
    llm_strategy = get_llm_strategy()
    session_id = "product_crawl_session"

    # Initialize state variables
    page_number = 1
    all_products = []
    seen_names = set()

    # Start the web crawler context
    # https://docs.crawl4ai.com/api/async-webcrawler/#asyncwebcrawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        while True:
            # Fetch and process data from the current page
            products, no_results_found = await fetch_and_process_page(
                crawler,
                page_number,
                BASE_URL,
                CSS_SELECTOR,
                llm_strategy,
                session_id,
                REQUIRED_KEYS,
                seen_names,
            
            )

            if no_results_found:
                print("No more products found. Ending crawl.")
                break  # Stop crawling when "No Results Found" message appears

            if not products:
                print(f"No products extracted from page {page_number}.")
                break  # Stop if no products are extracted

            # Add the products from this page to the total list
            all_products.extend(products)
            page_number += 1  # Move to the next page


            # Pause between requests to be polite and avoid rate limits
            await asyncio.sleep(5)  # Adjust sleep time as needed


#TODO : file name

    # Save the collected products to a CSV file
    if all_products:
        save_products_to_csv(all_products, "complete_products.csv")
        print(f"Saved {len(all_products)} products to 'complete_products.csv'.")
    else:
        print("No products were found during the crawl.")

    # Display usage statistics for the LLM strategy
    llm_strategy.show_usage()


async def main():
    """
    Entry point of the script.
    """
    await crawl_products()


if __name__ == "__main__":
    asyncio.run(main())