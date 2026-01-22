-- ============================================================================
-- NETFLIX INDIA CASE STUDY - SQL ANALYSIS
-- MIT Case Study: Netflix Goes to Bollywood
-- ============================================================================

-- SECTION 1: MARKET OVERVIEW & OPPORTUNITY
-- ============================================================================

-- 1.1 Total Addressable Market by Segment
SELECT 
    segment_name,
    city_tier,
    internet_users_millions,
    video_viewers_millions,
    ROUND(video_viewers_millions / internet_users_millions * 100, 1) AS penetration_pct,
    willingness_to_pay_usd,
    ROUND(video_viewers_millions * willingness_to_pay_usd * 12, 2) AS annual_revenue_potential_millions
FROM market_segments
ORDER BY annual_revenue_potential_millions DESC;

-- 1.2 Current Netflix Subscriber Base Analysis
SELECT 
    city_tier,
    plan_type,
    COUNT(*) AS subscribers,
    ROUND(AVG(monthly_price), 2) AS avg_price,
    ROUND(SUM(monthly_price), 2) AS monthly_revenue,
    ROUND(AVG(content_hours_per_month), 1) AS avg_viewing_hours
FROM subscribers
WHERE status = 'Active'
GROUP BY city_tier, plan_type
ORDER BY city_tier, subscribers DESC;

-- 1.3 Market Share Analysis
SELECT 
    competitor_name,
    users_millions,
    market_share_pct,
    monthly_price,
    annual_price,
    ad_supported,
    languages_count,
    ROUND(users_millions / NULLIF(monthly_price, 0), 2) AS users_per_dollar
FROM competitors
ORDER BY market_share_pct DESC;

-- SECTION 2: PRICING ANALYSIS
-- ============================================================================

-- 2.1 Revenue by Plan Type
SELECT 
    plan_type,
    monthly_price,
    COUNT(*) AS active_subscribers,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct_of_base,
    ROUND(SUM(monthly_price), 2) AS monthly_revenue,
    ROUND(SUM(monthly_price) * 100.0 / SUM(SUM(monthly_price)) OVER (), 1) AS pct_of_revenue
FROM subscribers
WHERE status = 'Active'
GROUP BY plan_type, monthly_price
ORDER BY monthly_revenue DESC;

-- 2.2 Pricing Test Results - Conversion Analysis
SELECT 
    price_point,
    plan_type,
    ROUND(AVG(conversions * 1.0 / signups), 3) AS avg_conversion_rate,
    ROUND(AVG(churn_rate), 3) AS avg_churn_rate,
    ROUND(AVG(avg_viewing_hours), 1) AS avg_viewing_hours,
    SUM(conversions) AS total_conversions
FROM pricing_tests
GROUP BY price_point, plan_type
ORDER BY price_point;

-- 2.3 Optimal Price Point Analysis
SELECT 
    price_point,
    SUM(signups) AS total_signups,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(conversions) * 1.0 / SUM(signups), 3) AS conversion_rate,
    ROUND(SUM(conversions) * price_point, 2) AS monthly_revenue,
    ROUND(AVG(churn_rate), 3) AS avg_churn
FROM pricing_tests
GROUP BY price_point
ORDER BY monthly_revenue DESC;

-- SECTION 3: CUSTOMER SEGMENTATION & BEHAVIOR
-- ============================================================================

-- 3.1 Subscriber Distribution by City Tier and Language
SELECT 
    city_tier,
    language_preference,
    COUNT(*) AS subscribers,
    ROUND(AVG(monthly_price), 2) AS avg_price,
    ROUND(AVG(content_hours_per_month), 1) AS avg_hours,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY city_tier), 1) AS pct_within_tier
FROM subscribers
WHERE status = 'Active'
GROUP BY city_tier, language_preference
HAVING subscribers >= 10
ORDER BY city_tier, subscribers DESC;

-- 3.2 Churn Analysis by Plan and Tier
SELECT 
    city_tier,
    plan_type,
    COUNT(*) AS total_subscribers,
    SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) AS churned,
    SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) AS active,
    ROUND(SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM subscribers
GROUP BY city_tier, plan_type
ORDER BY churn_rate_pct DESC;

-- 3.3 High-Value vs Low-Engagement Segments
SELECT 
    CASE 
        WHEN content_hours_per_month >= 60 THEN 'High Engagement'
        WHEN content_hours_per_month >= 30 THEN 'Medium Engagement'
        ELSE 'Low Engagement'
    END AS engagement_level,
    plan_type,
    COUNT(*) AS subscribers,
    ROUND(AVG(monthly_price), 2) AS avg_price,
    ROUND(AVG(content_hours_per_month), 1) AS avg_hours,
    SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) AS churned_count
FROM subscribers
GROUP BY engagement_level, plan_type
ORDER BY engagement_level, plan_type;

-- SECTION 4: COMPETITIVE ANALYSIS
-- ============================================================================

-- 4.1 Content Investment ROI Comparison
SELECT 
    company,
    year,
    india_investment_usd_millions,
    original_shows_count,
    languages_supported,
    ROUND(india_investment_usd_millions / NULLIF(original_shows_count, 0), 2) AS cost_per_show_millions,
    ROUND(india_investment_usd_millions / NULLIF(languages_supported, 0), 2) AS investment_per_language
FROM content_investment
WHERE year = 2020
ORDER BY india_investment_usd_millions DESC;

-- 4.2 Netflix Content Investment Trend
SELECT 
    year,
    india_investment_usd_millions,
    original_shows_count,
    languages_supported,
    hours_of_content,
    ROUND(india_investment_usd_millions / NULLIF(hours_of_content, 0) * 1000, 2) AS cost_per_hour_thousands
FROM content_investment
WHERE company = 'Netflix'
ORDER BY year;

-- 4.3 Competitor Pricing vs Market Share
SELECT 
    competitor_name,
    pricing_model,
    CASE WHEN monthly_price = 0 THEN annual_price/12 ELSE monthly_price END AS effective_monthly_price,
    users_millions,
    market_share_pct,
    ad_supported,
    ROUND(users_millions / market_share_pct, 2) AS users_per_share_point
FROM competitors
ORDER BY users_millions DESC;

-- SECTION 5: STRATEGIC INSIGHTS
-- ============================================================================

-- 5.1 Customer Lifetime Value Components
SELECT 
    plan_type,
    COUNT(*) AS active_subs,
    ROUND(AVG(monthly_price), 2) AS avg_monthly_revenue,
    ROUND(AVG(content_hours_per_month), 1) AS avg_engagement
FROM subscribers
WHERE status = 'Active'
GROUP BY plan_type
ORDER BY avg_monthly_revenue DESC;

-- 5.2 Language Preference vs Willingness to Pay
SELECT 
    language_preference,
    COUNT(*) AS subscribers,
    ROUND(AVG(monthly_price), 2) AS avg_price_paid,
    ROUND(AVG(content_hours_per_month), 1) AS avg_hours,
    ROUND(SUM(CASE WHEN status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM subscribers
GROUP BY language_preference
HAVING subscribers >= 50
ORDER BY subscribers DESC;

-- 5.3 Acquisition Channel Effectiveness
SELECT 
    acquisition_channel,
    COUNT(*) AS total_acquired,
    SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) AS active,
    ROUND(SUM(CASE WHEN status = 'Active' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS retention_rate,
    ROUND(AVG(CASE WHEN status = 'Active' THEN monthly_price ELSE 0 END), 2) AS avg_active_price,
    ROUND(AVG(CASE WHEN status = 'Active' THEN content_hours_per_month ELSE 0 END), 1) AS avg_engagement
FROM subscribers
GROUP BY acquisition_channel
ORDER BY retention_rate DESC;

-- 5.4 Growth Opportunity by Segment
SELECT 
    m.segment_name,
    m.video_viewers_millions AS potential_viewers,
    m.willingness_to_pay_usd AS avg_willingness_to_pay,
    ROUND(m.video_viewers_millions * m.willingness_to_pay_usd * 12, 2) AS annual_opportunity_millions
FROM market_segments m
ORDER BY annual_opportunity_millions DESC;