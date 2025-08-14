import matplotlib.pyplot as plt
import seaborn as sns

def plot_word_freq(word_freq, top_n=20):
    common_words = word_freq.most_common(top_n)
    words, counts = zip(*common_words)
    plt.figure(figsize=(10,6))
    sns.barplot(x=list(counts), y=list(words))
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.tight_layout()
    plt.show()

def plot_topic_distribution(topics):
    plt.figure(figsize=(8,5))
    sns.countplot(x=topics)
    plt.title("Topic Distribution")
    plt.xlabel("Topic")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
