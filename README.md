# Bidding-Web-solution

An E-commerce website for Online Product Auctioning made in Django 3.2.6. It provides the user with a catalog of different products available for bidding in the E-store. In order to facilitate online bidding, the website provides secure bids and closing features for buyers and sellers.


## It has the following 7 features as of 20-05-2023:
1. **Models** - Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.
2. **Create Listing** - Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
3. **Active Listings Page** - The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
4. **Listing Page** - Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
- If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
- If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
- If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
- If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.
5. **Watchlist** - Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
6. **Categories** - Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
7. **Django Admin Interface** - Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.
<br>

To run this web app in your local machine, follow below steps:
- Clone this repository
- Open terminal/command prompt
- cd into the cloned repository containing the "manage.py" file via terminal
- Run ```python manage.py runserver```
- Open any web browser (google chrome is recommended)
- Open the url ```127.0.0.1:8000``` in the browser
