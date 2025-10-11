🏦 Mozayede — Online Auction Platform (Django REST Framework)

A complete online auction platform built with Django REST Framework, featuring user profiles, bidding logic, and automatic auction closing.

🚀 Features
👤 User System

Each user has a UserProfile

Admins can ban users (is_ban, ban_until)

Banned users cannot create or bid in auctions

🏢 Companies & Auctions

Every auction belongs to a specific company

Each auction contains:

start_price: initial price

current_price: live highest bid

target_price: target value to auto-close auction

end_time: end timestamp

winner: current highest bidder

Auctions automatically close when:

The end_time is reached ⏰

OR target_price is met 💰

💸 Offers (Bids)

Each offer is created by an authenticated user

The system updates:

current_price

winner

If the bid is lower than the current price → it’s rejected

When an auction closes, no further bids are accepted

🧠 How It Works

1️⃣ A user logs in 🔑
2️⃣ User views all open auctions (is_closed=False)
3️⃣ User places a bid using an authenticated POST request
4️⃣ If bid amount > current_price:

The system updates the current_price and winner

If target_price or end_time reached → the auction closes

🧰 API Endpoints
Method	Endpoint	Description	Permission
GET	/auctions/	List all open auctions	Authenticated
POST	/auctions/create/	Create a new auction	Admin
POST	/auctions/<id>/offer/	Place a bid	Authenticated

Example request:

{
  "amount": 120000
}

🧾 Example Response
{
  "id": 1,
  "title": "MacBook Air M3 Auction",
  "current_price": 120000,
  "winner": "ramin",
  "is_closed": false
}

🧾 Example Workflow

Admin creates an auction

Users place bids

System automatically updates current_price

When auction reaches target_price or end_time, it auto-closes

Winner is displayed

🧰 Tech Stack
Tool	Purpose
🐍 Python	Backend Language
🦄 Django	Web Framework
⚙️ Django REST Framework	API Layer
🗄️ SQLite	Database
🧪 Postman	API Testing
