# main.py

from data_collection.image_processor import process_images
from analysis.text_analyzer import analyze_text
from models.trend_analyzer import analyze_trends
from visualization.visualizer import visualize_trends

def main():
    # Process images
    processed_data = process_images('travel_images')
    
    # Analyze text from images
    for item in processed_data:
        item['text_analysis'] = analyze_text(item['text'])
    
    # Analyze trends
    trend_analysis = analyze_trends(processed_data)
    
    # Visualize trends
    visualize_trends(trend_analysis)
    
    print("Trend analysis complete. Check the visualization folder for results.")

if __name__ == "__main__":
    main()