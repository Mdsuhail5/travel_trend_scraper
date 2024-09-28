# models/trend_analyzer.py

from collections import Counter

def analyze_trends(processed_data):
    all_locations = []
    all_keywords = []
    
    for item in processed_data:
        all_locations.extend(item['text_analysis']['locations'])
        all_keywords.extend(item['text_analysis']['keywords'])
    
    location_trends = Counter(all_locations)
    keyword_trends = Counter(all_keywords)
    
    return {
        'top_locations': location_trends.most_common(10),
        'top_keywords': keyword_trends.most_common(20)
    }