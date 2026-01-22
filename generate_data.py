import sqlite3
import random
from datetime import datetime, timedelta

# Create database
conn = sqlite3.connect('data/netflix_india.db')
cursor = conn.cursor()

# Table 1: Indian Market Subscribers
cursor.execute('''
CREATE TABLE subscribers (
    subscriber_id INTEGER PRIMARY KEY,
    country TEXT,
    city_tier TEXT,
    signup_date TEXT,
    plan_type TEXT,
    monthly_price REAL,
    status TEXT,
    language_preference TEXT,
    content_hours_per_month REAL,
    acquisition_channel TEXT
)
''')

# Table 2: Competitors
cursor.execute('''
CREATE TABLE competitors (
    competitor_id INTEGER PRIMARY KEY,
    competitor_name TEXT,
    pricing_model TEXT,
    monthly_price REAL,
    annual_price REAL,
    users_millions REAL,
    market_share_pct REAL,
    ad_supported TEXT,
    languages_count INTEGER,
    original_content_count INTEGER,
    year INTEGER
)
''')

# Table 3: Market Data by Segment
cursor.execute('''
CREATE TABLE market_segments (
    segment_id INTEGER PRIMARY KEY,
    segment_name TEXT,
    city_tier TEXT,
    internet_users_millions REAL,
    video_viewers_millions REAL,
    avg_income_usd INTEGER,
    english_speakers_pct REAL,
    mobile_only_pct REAL,
    willingness_to_pay_usd REAL
)
''')

# Table 4: Content Investment
cursor.execute('''
CREATE TABLE content_investment (
    investment_id INTEGER PRIMARY KEY,
    company TEXT,
    year INTEGER,
    india_investment_usd_millions REAL,
    original_shows_count INTEGER,
    languages_supported INTEGER,
    hours_of_content INTEGER
)
''')

# Table 5: Pricing Experiments
cursor.execute('''
CREATE TABLE pricing_tests (
    test_id INTEGER PRIMARY KEY,
    price_point REAL,
    plan_type TEXT,
    signups INTEGER,
    conversions INTEGER,
    churn_rate REAL,
    avg_viewing_hours REAL,
    month TEXT
)
''')

print("Tables created successfully!")

# Generate Subscribers Data (5000 records)
cities = {
    'Tier_1': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'],
    'Tier_2': ['Pune', 'Jaipur', 'Lucknow', 'Kochi', 'Indore'],
    'Tier_3': ['Nagpur', 'Vadodara', 'Rajkot', 'Vishakhapatnam', 'Bhopal']
}

plans = {
    'Mobile': 2.85,
    'Basic': 7.16,
    'Standard': 9.31,
    'Premium': 11.46
}

languages = ['Hindi', 'English', 'Tamil', 'Telugu', 'Bengali', 'Marathi', 'Gujarati', 'Kannada', 'Malayalam', 'Punjabi']
channels = ['Organic', 'Paid Social', 'Content Marketing', 'Referral', 'Influencer', 'TV Ads']

subscribers_data = []
base_date = datetime(2019, 1, 1)

for i in range(1, 5001):
    tier = random.choice(['Tier_1', 'Tier_2', 'Tier_3'])
    city = random.choice(cities[tier])
    
    if tier == 'Tier_1':
        plan = random.choices(list(plans.keys()), weights=[0.3, 0.25, 0.25, 0.2])[0]
    elif tier == 'Tier_2':
        plan = random.choices(list(plans.keys()), weights=[0.5, 0.3, 0.15, 0.05])[0]
    else:
        plan = random.choices(list(plans.keys()), weights=[0.7, 0.2, 0.08, 0.02])[0]
    
    days_offset = random.randint(0, 1460)
    signup = base_date + timedelta(days=days_offset)
    
    churn_prob = {'Mobile': 0.12, 'Basic': 0.08, 'Standard': 0.06, 'Premium': 0.05}
    status = 'Churned' if random.random() < churn_prob[plan] else 'Active'
    
    if tier == 'Tier_1':
        language = random.choices(languages, weights=[0.4, 0.35, 0.05, 0.05, 0.03, 0.03, 0.03, 0.03, 0.02, 0.01])[0]
    else:
        language = random.choices(languages, weights=[0.5, 0.1, 0.1, 0.1, 0.05, 0.05, 0.03, 0.03, 0.02, 0.02])[0]
    
    content_hours = random.uniform(20, 100) if status == 'Active' else random.uniform(5, 30)
    
    subscribers_data.append((
        i,
        'India',
        tier,
        signup.strftime('%Y-%m-%d'),
        plan,
        plans[plan],
        status,
        language,
        round(content_hours, 1),
        random.choice(channels)
    ))

cursor.executemany('INSERT INTO subscribers VALUES (?,?,?,?,?,?,?,?,?,?)', subscribers_data)
print("Subscribers data inserted: 5,000 records")

competitors_data = [
    (1, 'Netflix', 'Subscription', 2.85, 34.20, 2.0, 1.5, 'No', 10, 87, 2020),
    (2, 'Hotstar', 'Freemium', 4.29, 14.33, 129.0, 70.0, 'Yes', 8, 7, 2020),
    (3, 'Amazon Prime', 'Subscription', 1.19, 14.33, 26.0, 14.0, 'No', 6, 15, 2020),
    (4, 'ZEE5', 'Freemium', 2.86, 28.60, 26.0, 8.0, 'Yes', 12, 87, 2020),
    (5, 'Sony LIV', 'Freemium', 2.86, 28.60, 18.0, 4.5, 'Yes', 5, 12, 2020),
    (6, 'ALTBalaji', 'Subscription', 1.43, 4.30, 13.0, 1.8, 'No', 6, 42, 2020),
    (7, 'ErosNow', 'Freemium', 1.42, 13.63, 16.0, 2.2, 'Yes', 9, 40, 2020),
    (8, 'Voot', 'Freemium', 0.0, 0.0, 35.0, 3.0, 'Yes', 4, 8, 2020),
    (9, 'MX Player', 'Ad-supported', 0.0, 0.0, 45.0, 5.0, 'Yes', 7, 5, 2020),
    (10, 'YouTube Premium', 'Subscription', 1.90, 22.80, 12.0, 1.0, 'No', 1, 0, 2020)
]

cursor.executemany('INSERT INTO competitors VALUES (?,?,?,?,?,?,?,?,?,?,?)', competitors_data)
print("Competitors data inserted: 10 records")

segments_data = [
    (1, 'Premium Urban', 'Tier_1', 50, 35, 12000, 45, 30, 10.0),
    (2, 'Mid Urban', 'Tier_1', 80, 55, 6000, 25, 50, 5.0),
    (3, 'Value Urban', 'Tier_2', 120, 80, 3500, 15, 70, 2.5),
    (4, 'Small City', 'Tier_3', 180, 90, 2000, 8, 85, 1.5),
    (5, 'Rural Digital', 'Rural', 170, 40, 1200, 5, 95, 0.8)
]

cursor.executemany('INSERT INTO market_segments VALUES (?,?,?,?,?,?,?,?,?)', segments_data)
print("Market segments data inserted: 5 records")

investment_data = [
    (1, 'Netflix', 2017, 70, 5, 2, 120),
    (2, 'Netflix', 2018, 180, 12, 3, 350),
    (3, 'Netflix', 2019, 320, 35, 5, 680),
    (4, 'Netflix', 2020, 420, 87, 10, 1200),
    (5, 'Hotstar', 2020, 17, 7, 8, 200),
    (6, 'Amazon Prime', 2020, 85, 15, 6, 450),
    (7, 'ZEE5', 2020, 65, 87, 12, 890),
    (8, 'ErosNow', 2020, 50, 40, 9, 520)
]

cursor.executemany('INSERT INTO content_investment VALUES (?,?,?,?,?,?,?)', investment_data)
print("Content investment data inserted: 8 records")

pricing_data = []
test_id = 1
months = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06']
price_tests = [1.99, 2.85, 3.99, 4.99, 7.16, 9.31]

for month in months:
    for price in price_tests:
        signups = random.randint(800, 3000)
        conversion = random.uniform(0.12, 0.35)
        
        if price < 3:
            conversion = random.uniform(0.25, 0.35)
            churn = random.uniform(0.08, 0.14)
        elif price < 5:
            conversion = random.uniform(0.18, 0.28)
            churn = random.uniform(0.06, 0.10)
        else:
            conversion = random.uniform(0.10, 0.18)
            churn = random.uniform(0.04, 0.08)
        
        conversions = int(signups * conversion)
        viewing = random.uniform(30, 85)
        
        plan = 'Mobile' if price < 3 else 'Basic' if price < 7 else 'Standard'
        
        pricing_data.append((
            test_id,
            price,
            plan,
            signups,
            conversions,
            round(churn, 3),
            round(viewing, 1),
            month
        ))
        test_id += 1

cursor.executemany('INSERT INTO pricing_tests VALUES (?,?,?,?,?,?,?,?)', pricing_data)
print(f"Pricing test data inserted: {len(pricing_data)} records")

conn.commit()
conn.close()

print("\n✅ Database created successfully!")
print("Location: data/netflix_india.db")
print("\nTables created:")
print("1. subscribers (5,000 records)")
print("2. competitors (10 records)")
print("3. market_segments (5 records)")
print("4. content_investment (8 records)")
print("5. pricing_tests (36 records)")