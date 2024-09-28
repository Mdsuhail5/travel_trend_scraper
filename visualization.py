# visualization/visualizer.py

import matplotlib.pyplot as plt

def plot_trends(trends, title, filename):
    labels, values = zip(*trends)
    plt.figure(figsize=(12, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'visualization/{filename}.png')
    plt.close()

def visualize_trends(trend_analysis):
    plot_trends(trend_analysis['top_locations'], 'Top 10 Trending Locations', 'top_locations')
    plot_trends(trend_analysis['top_keywords'], 'Top 20 Trending Keywords', 'top_keywords')